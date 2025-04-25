from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Enquiry(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    address=models.TextField()
    contact=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)

class Adminlogin(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Registration(models.Model):
    uid=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    address=models.TextField()
    usertype=models.CharField(max_length=15)
    password=models.CharField(max_length=50)
    conpassword=models.CharField(max_length=50)
    registerdate=models.CharField(max_length=30)

class rentOTP(models.Model):
    rentOTPid = models.IntegerField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    houseID = models.CharField(max_length=6)
    ownerID = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)

    def is_valid(self):
        return now() <= self.created_at + datetime.timedelta(minutes=5)
    
class AddSell(models.Model):
    hid=models.IntegerField(primary_key=True,auto_created=True)
    image = models.ImageField(upload_to='')  # Directory to store images
    price = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimages = models.FileField(upload_to='')  # Optional images
    emailId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    add_date=models.DateField()

    def __str__(self):
        return f"{self.apartment} - {self.location}"