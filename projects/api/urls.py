from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

from .views import *

urlpatterns = [
    path('registerIAMToken', RegisterIAMToken.as_view(), name='RegisterIAMToken'),
    path('verifyIAM', VerifyIAM.as_view(), name='verifyIAM'),
    path('verifyOTP', VerifyOTP.as_view(), name='verifyOTP'),

]
