from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductView.as_view(), name='product'),
]
