from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.

# FormView를 상속해 기본적인 Form이 있는 View 만들어주기
# forms.py의 RegisterForm을 지정해서 구성이 가능

class RegisterView(FormView):
    template_name = 'register.html'
    form_class=RegisterForm
    success_url="/"

    def form_valid(self, form):
        user = User(
                    email = form.data.get('email'),
                    password = make_password(form.data.get('password'))
                )
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class=LoginForm
    success_url="/"

    # LoginForm에서 모든 유효성 검사가 성공적으로 끝났을 때 호출됨
    def form_valid(self, form):
        self.request.session['user'] = form.user_id

        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect("/")
