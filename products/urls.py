from django.urls import path
from .views import product_list, ProductDetails, ProductFilteredReviews

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', ProductDetails.as_view()),
    path('products/<int:product_id>/reviews/', ProductFilteredReviews.as_view()),
]