# import serializer to serialize models
from rest_framework import serializers

# import models to serialize it
from test_app.models import Merchant, Product


class MerchantSerializer(serializers.ModelSerializer):
    '''Сериализуем модель продавца'''
    class Meta:
        model = Merchant
        fields = ('business_name', 'merchant_id', 'rating',
                  'review_count', 'address', 'node_id', 'merchant_url')


class ProductSerializer(serializers.ModelSerializer):
    '''Сериализуем модель продукта'''
    merchant_id = serializers.CharField(max_length=32)
    date_scrapped = serializers.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Product
        fields = ('date_scrapped', 'product_name', 'merchant_id', 'price',
                  'num_of_reviews', 'num_of_elements', 'rating')

    def create(self, validated_data):
        merchant_id = validated_data.pop('merchant_id')
        merchant_instance = Merchant.objects.get(merchant_id=merchant_id)
        product_instance = Product.objects.create(**validated_data, merchant=merchant_instance)
        return product_instance
