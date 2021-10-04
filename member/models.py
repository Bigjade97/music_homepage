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

  def __str__(self):
    	return self.userid

class Top100(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Ballad(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Pop(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Hip(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Trot(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Live_Chart(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class New_Song(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class New_Album(models.Model):
    singer = models.CharField(max_length=50, null=True)
    album = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    kind = models.CharField(max_length=50, null=True)
    many = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.album