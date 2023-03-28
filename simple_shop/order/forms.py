from django import forms


class OrderForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    order_qty = forms.CharField(
        error_messages={'required': '수량을 입력해주세요'}, label="주문 수량")

    product = forms.IntegerField(
        error_messages={'required': '수량을 입력해주세요'},
        widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()

        order_qty = cleaned_data.get('order_qty')
        product_id = cleaned_data.get('product')

        if not (order_qty and product_id):
            self.add_error('product', '값이 없습니다.')
            self.add_error('order_qty', "값이 없습니다.")
            self.product = product_id