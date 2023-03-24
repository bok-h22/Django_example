from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm

# Create your views here.
# FBV 방식으로 View 구현
#  Function Based View


def register(request):
    # method에 따라서 기능을 다르게 수행
    # GET 방식 : 화면 보여주기
    # POST 방식 : 회원가입 기능 수행

    # 사용자가 GET 방식으로 요청한 경우
    if request.method == 'GET':
        # register.html 렌더링
        return render(request, 'register.html')

    # 사용자가 POST 방식으로 요청한 경우
    elif request.method == 'POST':
        # 두 비밀번호가 일치하는지
        # 모든 필드를 입력 했는지

        user_id = request.POST.get("user_id", None)  # user_id가 없으면 None
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # 원래라면 비밀번호 일치하는지 검사는 백엔드에서 하지 않고, 프론트엔드에서 한다.
        res_data = {}  # response data -> attribute

        # 무슨 문제가 있을지 각자 생각해 봅시다.
        if not (user_id and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '두 비밀번호가 다릅니다.'
        else:
            user = User(
                user_id=user_id,
                password=make_password(password),
                useremail=useremail
            )

            user.save()

        # 에러가 있던 없던 무조건 'register.html'을 띄워준다.
        return render(request, 'register.html', res_data)


def login(request):

    if request.method == 'POST':
        # 사용자가 입력한 값으로 채워진 폼
        form = LoginForm(request.POST)

        # is_valid : 유효성 검증
        #  - 값을 전부다 제대로 입력 했는지 검사
        #  + clean 메소드를 오버라이드 하므로 인해서 아이디와 패스워드 일치 여부까지 검사
        if form.is_valid():
            # form.is_valid()가 True다 -> 아이디, 패스워드 입력 잘 했고, 입력한 내용이 데이터베이스에도 존재한다.
            request.session['user'] = form.uid

            return redirect("/")

    else:  # GET으로 요청했을 때

        # 데이터가 입력되지 않은 폼
        form = LoginForm()

    return render(request, 'login.html', {"form": form})


def logout(request):
    # 세션에 로그인한 사용자의 정보가 있으면
    if request.session.get("user"):
        del (request.session['user'])  # 로그인한 사용자의 정보를 세션에서 제거

    # 로그아웃 끝났으면 메인 페이지로("/")
    return redirect("/")


# def login(request):

#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         user_id = request.POST.get("user_id", None)
#         password = request.POST.get("password", None)

#         res_data = {}

#         if not (user_id and password):
#             res_data['error'] = "모든 값을 입력해야 합니다."
#         else:
#             # 아이디와 비밀번호를 모두 입력했으면

#             # 아이디, 패스워드를 이용해서 실제 로그인할 수 있는지를 구현
#             # 1. 아이디를 이용해서 데이터가 있는지를 확인
#             user = User.objects.get(user_id=user_id) # 사용자에게 입력받은 user_id를 이용해서 조회
#                                                      # SELECT * FROM tb_user WHERE user_id=user_id

#             # 2. 비밀번호 검사
#             if check_password(password, user.password): # password : 사용자가 로그인을 위해 입력한 암호
#                                                         # user.password : 데이터베이스에 들어있는 암호
#                 request.session['user'] = user.id # user의 pk를 세션에 저장
#                 return redirect("/")
#             else:
#                 res_data["error"] = "비밀번호가 틀렸습니다"


#         return render(request, 'login.html', res_data)
