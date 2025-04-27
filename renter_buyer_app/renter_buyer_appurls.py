from django.urls import path
from . import views
app_name = 'renter_buyer_app'
urlpatterns=[
    path('sellerhome/',views.sellerhome,name='sellerhome'),
    path('addForSell/',views.addForSell,name='addForSell'),
    path('sellerViewEnquiry/',views.sellerViewEnquiry,name='sellerViewEnquiry'),
    path('viewAddedHome/',views.viewAddedHome,name='viewAddedHome'),
]