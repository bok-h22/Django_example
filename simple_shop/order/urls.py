from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderCreate.as_view()),
    path('', views.OrderList.as_view()),
]