from django.urls import path
from . import views

urlpatterns=[
    path('ownerhome/',views.ownerhome,name='ownerhome'),
    path('addrent/',views.addrent,name='addrent'),
    path('viewrent/',views.viewrent,name='viewrent'),
    path('ownerViewEnquiry/',views.ownerViewEnquiry,name='ownerViewEnquiry'),
]