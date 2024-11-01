from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=64, verbose_name="사용자 아이디")
    user_email=models.EmailField(max_length=128, verbose_name="사용자 이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.user_id
    
    class Meta:
        db_table = 'tb_user'

