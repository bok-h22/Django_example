from django.shortcuts import render
from .models import User

# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        user_id = request.POST['user_id']
        user_email = request.POST['user_email']
        password = request.POST['password']
        re_password = request.POST['re-password']

        user = User(user_id=user_id, user_email=user_email, password=password)
        user.save()
        
        return render(request, "register.html")