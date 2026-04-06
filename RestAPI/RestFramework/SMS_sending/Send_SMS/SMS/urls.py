from django.urls import path
from .views import sendsms

urlpatterns = [
    path('', sendsms, name='sendsms'),
]