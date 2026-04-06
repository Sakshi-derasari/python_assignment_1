from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="index"),
    path("sendmail",sendmail,name="sendmail"),
    path("sendfile",sendfile,name="sendfile"),
    path("sendsms",sendsms,name="sendsms"),
    path("payment",payment,name="payment"),
]