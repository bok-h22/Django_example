from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=64,
        label="사용자 아이디",
        error_messages={"required": "아이디를 입력해 주세요"}
    )

    # widget : input 태그의 타입
    password = forms.CharField(
        max_length=64, label="비밀번호",
        widget=forms.PasswordInput,
        error_messages={"required": "비밀번호를 입력해 주세요"}
    )

    def clean(self):
        # cleaned_data : 유효성 검증을 통과한 데이터
        # super().clean() : 부모클래스의 유효성 검증이 된 데이터 받아오기
        cleaned_data = super().clean()

        user_id = cleaned_data.get("user_id")
        password = cleaned_data.get("password")

        if user_id and password:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error("user_id", "아이디가 없습니다.")
                return

            if not check_password(password, user.password):
                self.add_error("password", "비밀번호가 틀렸습니다.")
            else:
                # 1. 클라이언트가 아이디와 비밀번호를 잘 입력했다.(기본 유효성 검증 - 부모클래스가 해줌)
                # 2. 클라이언트가 입력한 아이디에 해당하는 사용자가 있고, 비밀번호도 맞다.( 오버라이딩으로 구현 )
                self.uid = user.id  # pk를 저장해줌
