from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",add_to_cart,name="add_to_cart"),
    path("cart",cart,name="cart"),
    path("delete",delete,name="delete"),
    path("update",update,name="update"),
    path("payment",payment,name="payment"),
    path("success",success,name="success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
