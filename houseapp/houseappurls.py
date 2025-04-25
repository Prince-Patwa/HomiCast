from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import send_otp, verify_otp

urlpatterns = [
    path('', views.index, name='index'),  # Default route
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('logcode/',views.logcode,name='logcode'),
    path('registration/',views.registration,name='registration'),
    path('rent/',views.rent,name='rent'),
    path('rentSendOtp/',views.rentSendOtp,name='rentSendOtp'),
    path('rentVerifyOtp/',views.rentVerifyOtp,name='rentVerifyOtp'),
    path('rentResendOtp/',views.rentResendOtp,name='rentResendOtp'),
    path('sell/',views.sell,name='sell'),
    # path('addsell/',views.addsell,name='addsell'),
    # path('viewsell/',views.viewsell,name='viewsell'),
    # path('houseapp/', include(('houseapp.houseappurls', 'houseapp'), namespace='houseapp')),
    # path('houseapp/', include(('houseapp.urls', 'houseapp'), namespace='houseapp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)