from django.urls import path
from . import views

urlpatterns = [
        path('main', views.main),
        path('make', views.make),
        path('login', views.login),
        path('logout', views.logout),
        path('login_ajax', views.login_ajax),
        path('mypage', views.mypage),
        path('edit', views.edit),
        path('id_check', views.id_check),
        path('out', views.out),
]
