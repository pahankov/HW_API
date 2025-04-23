from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Product, Review
from .serializers import ProductListSerializer, ProductDetailsSerializer, ReviewSerializer


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetails(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)


class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        reviews = Review.objects.filter(product_id=product_id)
        mark = request.query_params.get('mark')

        if mark:
            reviews = reviews.filter(mark=mark)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)