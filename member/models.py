from django.db import models

# Create your models here.

class User( models.Model ) :
  userid = models.CharField(max_length=64, unique = True, verbose_name='아이디')
  password = models.CharField(max_length=64, verbose_name='비밀번호')
  username = models.CharField(max_length=64, verbose_name='사용자명')
  GENDERS = ( ('M','남성(Man)'),('W','여성(Woman)') )
  gender = models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
  address = models.CharField(max_length=128, verbose_name='주소')
  LIKES = ( ('K','가요(K-POP)'),('P','팝(POP)'),('H','힙합(HIP-POP)'),('T','트롯(TROT)') )
  like = models.CharField(max_length=1, verbose_name='좋아하는 장르', choices=LIKES)
  registered = models.DateTimeField(auto_now_add=True, verbose_name='등록')