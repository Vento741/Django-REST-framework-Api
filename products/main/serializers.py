from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductListSerializer(serializers.Serializer):
    
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']


class ProductFilteredReviews(serializers.Serializer):
    class Meta:
        model = Review
        fields = '__all__'

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        mark = self.context.get('request').query_params.get('mark')
        if mark is not None and representation['mark'] != int(mark):
            return {}
        return representation