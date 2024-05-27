from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from .models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)



class ProductDetailsView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)


    # доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        mark = request.query_params.get('mark')
        if mark is not None:
            reviews = get_list_or_404(Review, product_id=product_id, mark=mark)
        else:
            reviews = get_list_or_404(Review, product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)