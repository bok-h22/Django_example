from django.shortcuts import redirect
from .models import User


def is_authorized(callback):

    def wrapper(request, *args, **kwargs):
        user = request.session.get('user')

        if user is None or not user:
            return redirect("/user/login")

        return callback(request, *args, **kwargs)

    return wrapper


def is_admin(callback):

    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user')

        if user_id is None or not user_id:
            return redirect("/user/login")
        user = User.objects.get(pk=user_id)
        if user.level != 'admin':
            return redirect("/")

        return callback(request, *args, **kwargs)

    return wrapper
