from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("profile/<int:id>/",profile, name="profile"),
    path("profile/<int:id>/",profile, name="profile"),
    path("contact/", contact, name="contact"),
    path("update/<int:id>/",update_doctor, name="update"),
    path("delete/<int:id>/",delete_doctor, name="delete"),
]