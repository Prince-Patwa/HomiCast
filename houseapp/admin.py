from django.contrib import admin

# Register your models here.

from .models import Post,Enquiry,Adminlogin,Registration,rentOTP,AddSell

admin.site.register(Post)
admin.site.register(Enquiry)
admin.site.register(Adminlogin)
admin.site.register(Registration)
admin.site.register(rentOTP)
admin.site.register(AddSell)