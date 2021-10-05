from django.contrib import admin
from .models import User, Top100, Ballad, Pop, Hip, Trot, Video, Live_Chart, New_Song, New_Album, Mylist
# Register your models here.
admin.site.register(User)
admin.site.register(Top100)
admin.site.register(Ballad)
admin.site.register(Pop)
admin.site.register(Hip)
admin.site.register(Trot)
admin.site.register(Video)
admin.site.register(Live_Chart)
admin.site.register(New_Song)
admin.site.register(New_Album)
admin.site.register(Mylist)