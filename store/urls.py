from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductView.as_view(), name='product'),
    path('images/<int:pk>', views.get_image_for, name='image-for')
]
