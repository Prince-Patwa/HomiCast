from django.shortcuts import render,redirect
from django.http import HttpResponse
from houseapp.models import Enquiry,Registration
from django.utils import timezone
from django.views.decorators.cache import cache_control
import datetime
from joblib import load

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def adminhome(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            enq_count=Enquiry.objects.all().count()
            users_count=Registration.objects.all().count()
            return render(req,'adminhome.html',{'adminid':adminid,'enq_count':enq_count,'users_count':users_count})
    except KeyError:
        return redirect('login')
    # return render(req,'adminhome.html')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def adminlogout(req):
    try:
        if req.session['adminid']!=None:
            del req.session['adminid']
            return redirect('login')
    except KeyError:
        return redirect('login')

model = load('adminapp/prediction/Dragon.joblib')
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def prediction(req):
    if req.method == "POST":
        # Convert form input to the appropriate types
        try:
            CRIM = float(req.POST['CRIM'])
            ZN = float(req.POST['ZN'])
            INDUS = float(req.POST['INDUS'])
            CHAS = float(req.POST['CHAS'])  # or int if it's a binary variable
            NOX = float(req.POST['NOX'])
            RM = float(req.POST['RM'])
            AGE = float(req.POST['AGE'])
            DIS = float(req.POST['DIS'])
            RAD = float(req.POST['RAD'])  # assuming this is a discrete integer
            TAX = float(req.POST['TAX'])  # assuming this is an integer
            PTRATIO = float(req.POST['PTRATIO'])
            B = float(req.POST['B'])
            LSTAT = float(req.POST['LSTAT'])
        except ValueError:
            # Handle invalid input (in case of non-numeric data)
            return render(req, 'prediction.html', {'error': 'Invalid input. Please enter valid numbers.'})
        # Prepare the input data for prediction
        input_data = [[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]]
        # Model prediction
        predicted_price = model.predict(input_data)[0]
        # Return the result page with the predicted price
        return render(req, 'prediction.html', {'predicted_price': predicted_price})
    # If it's a GET request, render the prediction form
    return render(req, 'prediction.html')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewenquiry(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            enq=Enquiry.objects.all()
            return render(req,'viewenquiry.html',{'adminid':adminid,'enq':enq})
    except KeyError:
        return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def delenq(req,id):
    try:
        if req.session['adminid']!=None:
            Enquiry.objects.get(id=id).delete()
            return redirect('adminapp:viewenquiry')
    except KeyError:
        return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def viewuser(req):
    try:
        if req.session['adminid']!=None:
            adminid=req.session['adminid']
            user=Registration.objects.all()
            return render(req,'viewuser.html',{'adminid':adminid,'user':user})
    except KeyError:
        return redirect('login')