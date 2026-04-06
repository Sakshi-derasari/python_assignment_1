from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('show', views.show),
    path('delete', views.delete),
    path('getone', views.get_one),
    path('update', views.update),
]