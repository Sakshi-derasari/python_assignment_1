from django.urls import path
from .views import get_student, get_faculty, reg
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("student/", get_student),
    path("faculty/", get_faculty),
    path("reg/", reg),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]