from django.urls import path, include
from . import views
app_name = 'renter_buyer_app'
urlpatterns=[
    path('sellerhome/',views.sellerhome,name='sellerhome'),
    path('addForSell/',views.addForSell,name='addForSell'),
    path('viewsell/', views.viewsell, name='viewsell'),
    path('sellerViewEnquiry/',views.sellerViewEnquiry,name='sellerViewEnquiry'),
]