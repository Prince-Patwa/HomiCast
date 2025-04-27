from django.shortcuts import render,redirect
import datetime
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from . models import Enquiry,Registration,Adminlogin,rentOTP
from owner_seller_app.models import AddRent
from renter_buyer_app.models import AddSell
from django.core.mail import send_mail
from django.contrib import messages
from smtplib import SMTPAuthenticationError
import random
from django.utils.timezone import now
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse

def index(req):
    sells = AddSell.objects.all()
    rents = AddRent.objects.all()
    paginator = Paginator(rents,3)
    pageNumber = req.GET.get('page')
    serviceDataFinal = paginator.get_page(pageNumber)
    data={
        'rents':serviceDataFinal,
        'sells':sells,
    }
    return render(req, 'index.html',data)

def about(req):
    return render(req,"about.html")

def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        gender=req.POST['gender']
        address=req.POST['address']
        contact=req.POST['contact']
        emailaddress=req.POST['emailaddress']
        enquirytext=req.POST['enquirytext']
        enquirydate=datetime.datetime.today()
        enq=Enquiry(name=name,gender=gender,address=address,contact=contact,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        msg="Your enquiry is submitted successfully"
        return render(req,"contact.html",{'msg':msg})      # locals()   or   dictionary
    return render(req,"contact.html")

def login(req):
    return render(req,"login.html")

def registration(req):
    if req.method=="POST":
        name=req.POST['name']
        gender=req.POST['gender']
        contact=req.POST['contact']
        emailaddress=req.POST['emailaddress']
        address=req.POST['address']
        usertype=req.POST['usertype']
        password=req.POST['password']
        conpassword=req.POST['conpassword']
        registerdate=datetime.datetime.today()
        if password==conpassword:
            register=Registration(name=name,gender=gender,contact=contact,emailaddress=emailaddress,address=address,usertype=usertype,password=password,conpassword=conpassword,registerdate=registerdate)
            register.save()
            msg="Your registration successfully"
            return render(req,"registration.html",{'msg':msg}) 
        msg="Your both password is diffrent. Plese enter same password." 
        return render(req,"registration.html",{'msg':msg})
    return render(req,"registration.html")

def logcode(req):
    if req.method == "POST":
        usertype=req.POST['usertype']
        userid=req.POST['userid']
        password=req.POST['password']
        if usertype=="admin":
            try:
                user=Adminlogin.objects.get(userid=userid,password=password)
                if user is not None:
                    req.session['adminid']=userid
                    return redirect('adminapp:adminhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
        
        elif usertype=="owner":
            try:
                owner = Registration.objects.get(emailaddress=userid, password=password, usertype="owner")
                if owner is not None:
                    req.session['ownerid']=userid
                    return redirect('owner_seller_app:ownerhome')
            except Registration.DoesNotExist:
                # Handle the case where no matching owner is found
                return render(req, 'login.html', {'msg': 'Invalid User'})
            except Registration.MultipleObjectsReturned:
                # Handle the case where multiple owners match the query
                return render(req, 'login.html', {'msg': 'Multiple accounts found. Contact support.'})
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})

        elif usertype=="seller":
            try:
                seller = Registration.objects.get(emailaddress=userid, password=password, usertype="seller")
                if seller is not None:
                    req.session['sellerid']=userid
                    return redirect('renter_buyer_app:sellerhome')
            except Registration.DoesNotExist:
                # Handle the case where no matching owner is found
                return render(req, 'login.html', {'msg': 'Invalid User'})
            except Registration.MultipleObjectsReturned:
                # Handle the case where multiple owners match the query
                return render(req, 'login.html', {'msg': 'Multiple accounts found. Contact support.'})
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
        else:
            return render(req,'login.html',{'msg':'Invalid user type'})

def rent(req):
    rents = AddRent.objects.all()
    #for searching operation
    if req.method=="POST":
        st=req.POST['search']
        if st != None:
            rents = AddRent.objects.filter(location__icontains=st) #wher __icontains is searching from left & right both in a string "location" or given from DB
    #for pagination
    paginator = Paginator(rents,6)
    pageNumber = req.GET.get('page')
    serviceDataFinal = paginator.get_page(pageNumber)
    totalpage = serviceDataFinal.paginator.num_pages 
    data={
        'rents':serviceDataFinal,
        'lastpage':totalpage,
        'totalPageList':[n+1 for n in range(totalpage)]
    }
    return render(req,'rent.html',data)

def sell(req):
    sells = AddSell.objects.all()
    #for searching operation
    if req.method=="POST":
        st=req.POST['search']
        if st != None:
            sells = AddSell.objects.filter(location__icontains=st) #wher __icontains is searching from left & right both in a string "location" or given from DB
    return render(req,'sell.html',{'sells':sells})

def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))

def rentSendOtp(req):
    # owner = Registration.objects.get(hid=houseID,emailaddress=ownerID)
    if req.method == 'POST':
        name = req.POST['name']
        phone = req.POST['phone']
        email = req.POST['email']
        houseID = req.POST['houseID']
        ownerID = req.POST['ownerID']
        if email:
            otp = generate_otp()
            # Save OTP to the database
            rentOTP.objects.update_or_create(name=name, phone=phone, email=email, defaults={'otp': otp}, houseID=houseID, ownerID=ownerID)
            # Save email in the session
            req.session['email'] = email
            # Send OTP to the email
            try:
                send_mail('Your OTP Code', f'Your OTP is: {otp}', 'bajrangipatwa9@gmail.com', [email], fail_silently=False,)
                messages.success(req, 'OTP sent to your email!')
            except SMTPAuthenticationError:
                messages.error(req, 'Failed to send email. Check your email credentials or enable app passwords.')
            except Exception as e:
                messages.error(req, f'An error occurred: {e}')
            return redirect('rentVerifyOtp')
    return render(req,'rentSendOtp.html')

def rentVerifyOtp(req):
    email = req.session.get('email')
    if not email:
        messages.error(req, 'Session expired. Please request a new OTP.')
        return redirect('rentSendOtp')
    if req.method == 'POST':
        otp = req.POST.get('otp')
        if otp:
            try:
                otp_record = rentOTP.objects.get(email=email, otp=otp)
                if otp_record.is_valid():
                    messages.success(req, 'OTP verified successfully!')
                    return render(req, 'rentVerifyOtp.html', {'msg': 'OTP verified successfully!'})
                else:
                    messages.error(req, 'OTP has expired.')
            except rentOTP.DoesNotExist:
                messages.error(req, 'Invalid OTP.')
    return render(req,'rentVerifyOtp.html')

def rentResendOtp(req):
    email = req.session.get('email')
    if not email:
        messages.error(req, 'Session expired. Please request a new OTP.')
        return redirect('rentSendOtp')
    otp = generate_otp()
    try:
        # Update the OTP in the database
        rentOTP.objects.update_or_create(
            email=email,
            defaults={'otp': otp, 'created_at': now()}
        )
        # Send the new OTP
        send_mail(
            'Your Resent OTP Code',
            f'Your new OTP is: {otp}',
            'bajrangipatwa9@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(req, 'A new OTP has been sent to your email.')
    except Exception as e:
        messages.error(req, f'Failed to resend OTP: {e}')
    return redirect('rentVerifyOtp')