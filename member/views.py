from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
# Create your views here.

def main (req) :
  if req.session.get('userid'):
    return render (req, 'music.html', {'pam1' : req.session['userid']} )
  else:
    if req.method == "POST" :
      logged_member = User.objects.get(userid = req.POST.get('id'), password = req.POST.get('pw'))
      if logged_member :
        req.session['userid'] = req.POST.get('id')
        req.session['password'] = req.POST.get('pw')
        print("asda")
        return render(req, 'music.html', {'pam1' : req.session['userid']})
      else :
        messages.error(req, '아이디와 비밀번호를 확인해주세요.')
        return redirect('../ssac/main')
    else :
      return render (req, 'music.html')

def login_ajax (req) :
  return render(req, 'login_ajax.html')

def make (req) :
  if req.method == "POST" :
    new_member = User( userid = req.POST.get('id'), username = req.POST.get('name'), password = req.POST.get('pw'), gender = req.POST.get('gender'), address = req.POST.get('address'), like = req.POST.get('genre'))

    new_member.save()
    return redirect('../ssac/login')
  else :
    return render (req, 'make.html')

def login (req) :
  if req.method == "POST" :
    logged_member = User.objects.get(userid = req.POST.get('id'), password = req.POST.get('pw'))
    if logged_member :
      req.session['userid'] = req.POST.get('id')
      req.session['password'] = req.POST.get('pw')
      return redirect('../ssac/main')
    else :
      messages.error(req, '아이디와 비밀번호를 확인해주세요.')
      return redirect('../ssac/login')
  else :
    return render (req, 'login.html')

def id_check (req) :
  userid = req.POST.get('id_')
  try: 
    User.objects.get(userid = userid)
    overlap = True
    return render (req, 'id_check.html', {'OK' : overlap})
  except:
    if userid == "" :
      overlap = "Blank"
    else:
      overlap = False
    return render(req, 'id_check.html', {'OK' : overlap}) 

def logout (req) :
  req.session.pop('userid')
  return redirect('../ssac/main')

def mypage (req) :
  return render(req, 'mypage.html', {'pam1' : req.session['userid']}) 

def edit (req) :
  if req.method == "POST" :
    edit_member = User.objects.get(userid = req.session.get('userid'))
    edit_member.username = req.POST.get('name')
    edit_member.gender = req.POST.get('gender')
    edit_member.address = req.POST.get('address')
    edit_member.like = req.POST.get('genre')
    edit_member.save()
    messages.success(req, '회원정보 수정이 완료되었습니다.')
    print(edit_member.like)
    return render(req, 'edit.html', {'pam1' : edit_member.userid, 'pam2' : edit_member.password, 'pam3' : edit_member.username, 'pam4' : edit_member.gender, 'pam5' : edit_member.address, 'pam6' : edit_member.like}) 
  else:
    edit_member = User.objects.get(userid = req.session.get('userid'))
    return render(req, 'edit.html', {'pam1' : edit_member.userid, 'pam2' : edit_member.password, 'pam3' : edit_member.username, 'pam4' : edit_member.gender, 'pam5' : edit_member.address, 'pam6' : edit_member.like}) 

def pw_chg (req) :
  if req.method == "POST" :
    edit_member = User.objects.get(userid = req.session.get('userid'))
    edit_member.password = req.POST.get('pw')
    edit_member.save()
    messages.success(req, '비밀번호 변경이 완료되었습니다.')
    return render(req, 'pw_chg.html', {'pam1' : req.session['userid']})
  else :
    return render(req, 'pw_chg.html', {'pam1' : req.session['userid']})


def out (req) :
  if req.method == "POST" :
    user = User.objects.filter( userid = req.POST.get('id'), password = req.POST.get('pw'))

    if user:
      user.delete()
      req.session.pop('userid')
      messages.success(req, '탈퇴가 완료되었습니다.')
      return redirect('../ssac/main')
    else :
      messages.error(req, '비밀번호가 일치하지 않습니다.')
      return render(req, 'out.html', {'pam1' : req.session['userid']}) 
  else:
    return render (req, 'out.html', {'pam1' : req.session['userid']})

def chart_top (req) :
  return render(req, 'chart_top.html', {'pam1' : req.session['userid']}) 

def chart_genre (req) :
  return render(req, 'chart_genre.html', {'pam1' : req.session['userid']}) 

def chart_genre_pop (req) :
  return render(req, 'chart_genre_pop.html', {'pam1' : req.session['userid']}) 

def chart_genre_ost (req) :
  return render(req, 'chart_genre_ost.html', {'pam1' : req.session['userid']}) 

def chart_genre_trot (req) :
  return render(req, 'chart_genre_trot.html', {'pam1' : req.session['userid']}) 

def chart_video (req) :
  return render(req, 'chart_video.html', {'pam1' : req.session['userid']}) 