from rest_framework import generics

from test_app.models import Merchant, Product
from .serializers import MerchantSerializer, ProductSerializer


class MerchantListView(generics.ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''Класс для работы с информацией об определенном продавце'''
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
