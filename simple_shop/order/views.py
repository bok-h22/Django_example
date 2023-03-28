from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from django.utils.decorators import method_decorator
from .forms import OrderForm
from .models import Order
from user.decorators import is_authorized

from product.models import Product
from user.models import User
from django.db import transaction

# Create your views here.
@method_decorator(is_authorized, name='dispatch')
class OrderCreate(FormView):
    form_class=OrderForm
    success_url="/product/"

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
    
    def form_valid(self, form):
        with transaction.atomic():
                order = Order(
                    order_qty=form.data.get('order_qty'),
                    product=Product.objects.get(pk=form.data.get('product')),
                    user = User.objects.get(pk=self.request.session.get('user'))
                )

                prod = Product.objects.get(pk=form.data.get('product'))
                prod.product_stock -= int(form.data.get('order_qty'))

                order.save()
                prod.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return redirect(f"/product/detail/{form.product}")

@method_decorator(is_authorized, name='dispatch')
class OrderList(ListView):
    
    template_name = 'order_list.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(user__pk=self.request.session.get('user'))
        return queryset