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
        path('pw_chg', views.pw_chg),
        path('chart_top', views.chart_top),
        path('chart_genre', views.chart_genre),
        path('chart_genre_pop', views.chart_genre_pop),
        path('chart_genre_ost', views.chart_genre_ost),
        path('chart_genre_trot', views.chart_genre_trot),
        path('chart_video', views.chart_video),
]
