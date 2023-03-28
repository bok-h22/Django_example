from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer

#상품 목록 API
class ProductList(generics.ListCreateAPIView):
    quaryset = Product.objects.all() #quaryset에는 serialize 할 데이터를 넣기
    serializer_class = ProductSerializer

#상품 상세 API
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
