from rest_framework import serializer
from .models import Product

class ProductSerializer(serializer.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__" #모든 필드를 직렬화

        #pk, 상품명, 가격
        #fields = ["pk", "product_name", "product_price"]
