from django.urls import path
from .views import *

urlpatterns = [
    path('', map_view, name='map')
]