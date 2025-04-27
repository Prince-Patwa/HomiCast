from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from houseapp.models import Enquiry,Registration,rentOTP
from renter_buyer_app.models import AddSell
from django.utils import timezone
from django.views.decorators.cache import cache_control
import datetime

def sellerhome(req):
    return render(req,'sellerhome.html')

def addForSell(req):
    try:
        if req.session['sellerid']!=None:
            sellerid=req.session['sellerid']
            seller=Registration.objects.get(emailaddress=sellerid)
            if req.method=="POST":
                image=req.FILES['image']
                price=req.POST['price']
                apartment=req.POST['apartment']
                area=req.POST['area']
                location=req.POST['location']
                pimages=req.FILES['pimages']
                add_date=timezone.now()
                if not image:
                    return render(req, 'addsell.html', {'error': 'Image is required'})
                addsell=AddSell(image=image,price=price,apartment=apartment,area=area,location=location,pimages=pimages,add_date=add_date,emailId=seller.emailaddress,name=seller.name)
                addsell.save()
                return redirect('renter_buyer_app:viewAddedHome')
            return render(req,'addForSell.html')
    except KeyError:
        return redirect('login')
    # return render(req,'addForSell.html')

def viewAddedHome(req):
    return render(req,'viewAddedHome.html')

# def sellerViewEnquiry(req):
#     try:
#         sellerid = req.session.get('sellerid')  # Safely get session data
#         if sellerid:
#             sell_otp_entry = rentOTP.objects.filter(sellerID=sellerid).first()
#             if sell_otp_entry:
#                 enq = rentOTP.objects.filter(sellerID=sellerid)  # Filter by sellerid
#                 return render(req, 'sellerViewEnquiry.html', {'sellerid': sellerid, 'enq': enq})
#             else:
#                 # No entries found, redirect or show an empty response
#                 return render(req, 'sellerViewEnquiry.html', {'sellerid': sellerid, 'enq': []})
#         else:
#             # If sellerid is not in the session, redirect to login
#             return redirect('login')
#     except Exception as e:
#         # Log the exception (optional)
#         # print(f"Error in sellerViewEnquiry: {e}")
#         return redirect('sellerhome')  # Redirect to seller home in case of any error
#     # return render(req,'sellerViewEnquiry.html')

def sellerViewEnquiry(req):
    return render(req,'sellerViewEnquiry.html')