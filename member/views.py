from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import User, Top100, Video, Live_Chart, Ballad, Pop, Hip, Trot, New_Song, New_Album, Mylist
from django.contrib import messages
from django.core.paginator import Paginator
import os
# Create your views here.

def main (req) :
  l_chart_10 = Live_Chart.objects.all().order_by('pk')
  if req.session.get('userid'):
    return render (req, 'music.html', {'pam1' : req.session['userid'], 'l_chart' : l_chart_10} )
  else:
    if req.method == "POST" :
      try :
        logged_member = User.objects.get(userid = req.POST.get('id'), password = req.POST.get('pw'))
        if logged_member :
          req.session['userid'] = req.POST.get('id')
          req.session['password'] = req.POST.get('pw')
          print("asda")
          return render(req, 'music.html', {'pam1' : req.session['userid'], 'l_chart' : l_chart_10})
      except :
        messages.error(req, '아이디와 비밀번호를 확인해주세요.')
        return redirect('../ssac/main')
    else :
      return render (req, 'music.html', {'l_chart' : l_chart_10})

def login_ajax (req) :
  return render(req, 'login_ajax.html')

def make (req) :
  if req.method == "POST" :
    new_member = User( userid = req.POST.get('id'), username = req.POST.get('name'), password = req.POST.get('pw'), gender = req.POST.get('gender'), address = req.POST.get('address'), like = req.POST.get('genre'))

    new_member.save()
    messages.success(req, '회원가입 성공.')
    return redirect('../ssac/login')
  else :
    return render (req, 'make.html')

def login (req) :
  if req.method == "POST" :
    try :
      logged_member = User.objects.get(userid = req.POST.get('id'), password = req.POST.get('pw'))
      if logged_member :
        req.session['userid'] = req.POST.get('id')
        req.session['password'] = req.POST.get('pw')
        return redirect('../ssac/main')
    except :
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
  if req.session.get('userid'):
    chart_100 = Top100.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(chart_100, 50) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    if req.method == "POST" :
      songs = req.POST.getlist('chkbox_elem')
      
      for song in songs :
        songss = Top100.objects.filter( name = song ).first()
      # chkbox_elems = req.POST.getlist('chkbox_elem')
        user = User.objects.get( userid = req.session.get('userid'))
        mylist = Mylist(
          user = user,
          song = songss
        )
        mylist.save()
      messages.success(req, '정상적으로 리스트에 추가되었습니다.')
      # chkbox_elems = Mylist.objects.get( user = req.session.get('userid'))
      # , song = req.POST.getlist('chkbox_elem')
      # chkbox_elems.save()
      return render(req, 'chart_top.html', {'pam1' : req.session['userid'], 'page_obj' : page_obj})
    else:
      return render(req, 'chart_top.html', {'pam1' : req.session['userid'], 'page_obj' : page_obj})
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')

  

def chart_genre (req) :
  if req.session.get('userid'):
    b_chart_50 = Ballad.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(b_chart_50, 25) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj_b = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    return render(req, 'chart_genre.html', {'pam1' : req.session['userid'], 'page_obj_b' : page_obj_b}) 
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')

def chart_genre_pop (req) :
  if req.session.get('userid'):
    p_chart_50 = Pop.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(p_chart_50, 25) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj_b = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    return render(req, 'chart_genre_pop.html', {'pam1' : req.session['userid'], 'page_obj_b' : page_obj_b}) 
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')

def chart_genre_hip (req) :
  if req.session.get('userid'):
    h_chart_50 = Hip.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(h_chart_50, 25) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj_b = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    return render(req, 'chart_genre_hip.html', {'pam1' : req.session['userid'], 'page_obj_b' : page_obj_b}) 
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')

def chart_genre_trot (req) :
  if req.session.get('userid'):
    t_chart_50 = Trot.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(t_chart_50, 25) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj_b = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    return render(req, 'chart_genre_trot.html', {'pam1' : req.session['userid'], 'page_obj_b' : page_obj_b}) 
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')

def chart_video (req) :
  if req.session.get('userid'):
    v_chart_100 = Video.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(v_chart_100, 50) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    return render(req, 'chart_video.html', {'pam1' : req.session['userid'], 'page_obj' : page_obj})
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')

def new_song (req) :
  if req.session.get('userid'):
    n_chart_100 = New_Song.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(n_chart_100, 25) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    return render(req, 'new_song.html', {'pam1' : req.session['userid'], 'page_obj' : page_obj}) 
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')

def new_album (req) :
  if req.session.get('userid'):
    na_chart_100 = New_Album.objects.all().order_by('pk')
    page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(na_chart_100, 10) #Paginator(분할된 객체, 페이지 당 담길 객체수)
    page_obj_b = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴
    return render(req, 'new_album.html', {'pam1' : req.session['userid'], 'page_obj_b' : page_obj_b})  
  else:
    messages.error(req, '로그인을 먼저 해주세요.')
    return redirect('/ssac/main')


def mylist (req) :
  user_ = User.objects.get(userid = req.session.get('userid'))
  my_chart = Mylist.objects.filter(user = user_).order_by('-pk')
  page = int(req.GET.get('page', '1')) #GET 방식으로 정보를 받아오는 데이터
  paginator = Paginator(my_chart, 50) #Paginator(분할된 객체, 페이지 당 담길 객체수)
  page_obj = paginator.get_page(page) #페이지 번호를 받아 페이지를 리턴

  if req.method == "POST" :
    songs = req.POST.getlist('chkbox_elem')

    for song in songs :
      song_la = Top100.objects.filter( name = song ).first()

      # songss = Mylist.objects.get( song = song_la.name )
    # chkbox_elems = req.POST.getlist('chkbox_elem')
      # print(songss)
      user = User.objects.get( userid = req.session.get('userid'))
      mylist = Mylist.objects.filter( user = user, song = song_la).first()
      mylist.delete()
    messages.success(req, '정상적으로 리스트에서 삭제되었습니다.')
    return redirect('/ssac/mylist')
  else :
    context = {
        'pam1' : req.session['userid'],
        'page_obj' : page_obj
      }
    return render(req, 'mylist.html', context)




