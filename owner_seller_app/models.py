from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.
class AddRent(models.Model):
    hid=models.IntegerField(primary_key=True,auto_created=True)
    image = models.ImageField(upload_to='static/images/')  # Directory to store images
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