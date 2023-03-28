from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from .models import Product
from .forms import ProductRegisterForm
from order.forms import OrderForm

from django.utils.decorators import method_decorator
from user.decorators import is_admin


# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'product_list'

@method_decorator(is_admin, name='dispatch')
class ProductRegister(FormView):
    form_class=ProductRegisterForm
    template_name = 'product_reg.html'
    success_url="/product/"

    def form_valid(self, form):
        product = Product(
                product_name = form.data.get('product_name'),
                product_price = form.data.get('product_price'),
                product_desc = form.data.get('product_desc'),
                product_stock = form.data.get('product_stock'))

        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = OrderForm(self.request)
        return context
