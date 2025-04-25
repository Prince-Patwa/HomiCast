from django.urls import path
from . import views
urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('prediction/',views.prediction,name='prediction'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('delenq/<int:id>/',views.delenq,name='delenq'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('viewuser/',views.viewuser,name='viewuser'),
]