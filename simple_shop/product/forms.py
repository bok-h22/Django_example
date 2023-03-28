from django import forms

class ProductRegisterForm(forms.Form):
    product_name = forms.CharField(
        error_messages={'required': '상품명을 입력해주세요'}, label="상품명")

    product_price = forms.IntegerField(
        error_messages={'required': '상품가격을 입력해주세요'}, label="상품가격")

    product_desc = forms.CharField(
        error_messages={'required': '상품설명을 입력해주세요'}, label="상품설명")

    product_stock = forms.IntegerField(
        error_messages={'required': '상품재고을 입력해주세요'}, label="상품재고")