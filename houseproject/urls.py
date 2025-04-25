"""
URL configuration for houseproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('houseapp.houseappurls')),
    # path('', include('houseapp.urls')),
    path('adminapp/',include(('adminapp.adminappurls','adminapp'),namespace='adminapp')),
    path('owner_seller_app/',include(('owner_seller_app.owner_seller_appurls','owner_seller_app'),namespace='owner_seller_app')),
    path('renter_buyer_app/',include(('renter_buyer_app.renter_buyer_appurls','renter_buyer_app'),namespace='renter_buyer_app')),
]
