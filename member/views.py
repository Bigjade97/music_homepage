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
      logged_member = User.objects.filter(userid = req.POST.get('id'), password = req.POST.get('pw'))
      if logged_member :
        req.session['userid'] = req.POST.get('id')
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
    logged_member = User.objects.filter(userid = req.POST.get('id'), password = req.POST.get('pw'))
    if logged_member :
      req.session['userid'] = req.POST.get('id')
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
  return render(req, 'edit.html', {'pam1' : req.session['userid']}) 

def out (req) :
  if req.method == "POST" :
    user = User.objects.filter( userid = req.POST.get('id'), password = req.POST.get('pw'))

    if user:
      user.delete()
      req.session.pop('userid')
      return redirect('../ssac/main')
    else :
      return render(req, 'out.html') 
  else:
    return render (req, 'out.html', {'pam1' : req.session['userid']})