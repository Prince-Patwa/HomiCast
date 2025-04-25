from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from houseapp.models import Enquiry,Registration,rentOTP
from django.utils import timezone
from django.views.decorators.cache import cache_control
import datetime
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from .models import AddRent

def ownerhome(req):
    return render(req,'ownerhome.html')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def addrent(req):
    try:
        if req.session['ownerid']!=None:
            ownerid=req.session['ownerid']
            owner=Registration.objects.get(emailaddress=ownerid)
            if req.method=="POST":
                image=req.FILES['image']
                price=req.POST['price']
                apartment=req.POST['apartment']
                area=req.POST['area']
                location=req.POST['location']
                pimages=req.FILES['pimages']
                add_date=timezone.now()
                if not image:
                    return render(req, 'addrent.html', {'error': 'Image is required'})
                addrent=AddRent(image=image,price=price,apartment=apartment,area=area,location=location,pimages=pimages,add_date=add_date,emailId=owner.emailaddress,name=owner.name)
                addrent.save()
                return redirect('owner_seller_app:viewrent')
            return render(req,'addrent.html')
    except KeyError:
        return redirect('login')
    # return render(req,'addrent.html')

def viewrent(req):
    return render(req,'viewrent.html')

def ownerViewEnquiry(req):
    try:
        ownerid = req.session.get('ownerid')  # Safely get session data
        if ownerid:
            rent_otp_entry = rentOTP.objects.filter(ownerID=ownerid).first()
            if rent_otp_entry:
                enq = rentOTP.objects.filter(ownerID=ownerid)  # Filter by ownerid
                return render(req, 'ownerViewEnquiry.html', {'ownerid': ownerid, 'enq': enq})
            else:
                # No entries found, redirect or show an empty response
                return render(req, 'ownerViewEnquiry.html', {'ownerid': ownerid, 'enq': []})
        else:
            # If ownerid is not in the session, redirect to login
            return redirect('login')
    except Exception as e:
        # Log the exception (optional)
        # print(f"Error in ownerViewEnquiry: {e}")
        return redirect('ownerhome')  # Redirect to owner home in case of any error