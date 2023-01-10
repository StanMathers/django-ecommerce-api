from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('product/<int:pk>', views.get_product, name='product'),
    path('product/<int:pk>/image', views.get_image_for, name='image'),
    path('product_category/<int:pk>', views.get_product_category, name='product_category')
]
