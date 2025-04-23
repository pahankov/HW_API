from django.urls import path
from .views import product_list, ProductDetails

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', ProductDetails.as_view()),
]
