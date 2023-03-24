from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')), # user App의 urls.py에 등록된 url 포함시키기
    path('board/', include('board.urls')),
    path('', home),
]