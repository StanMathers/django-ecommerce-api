from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('product/<int:pk>', views.get_product, name='product')
]
