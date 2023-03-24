from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    user_id = forms.CharField(max_length=64,
                              label="사용자 아이디",
                              error_messages={
                                'required': "아이디를 입력해 주세요"
                              })
    password = forms.CharField(max_length=64,
                               label="비밀번호",
                               widget=forms.PasswordInput,
                               error_messages={
                                'required': "비밀번호를 입력해 주세요"
                              })
    

		    # 기본적인 유효성 검증을 먼저 수행하기 위해 부모 클래스의 clean()을 먼저 실행
		    # 값이 모두 들어있는지를 검사합니다.
		    # 값이 모두 들어있지 않으면 여기에서 이미 실패처리가 됩니다.

