from django.urls import path
from . import views

app_name = 'freeapp'

urlpatterns = [
    path('', views.demo, name='demo'),
    path('login/',views.log,name='login'),
    path('register/',views.regist,name='register'),
    path('computer Science/', views.one_r,name='computer Science'),
    path('biology/', views.two_r,name='biology'),
    path('maths/', views.three_r,name='maths'),
    path('commerce/', views.four_r,name='commerce'),
    path('history/', views.five_r,name='history'),
    path('student_form/', views.student_form, name='student_form'),
    path('log',views.log, name='log'),
    path('regi', views.regi, name='regi'),
    path('welcome/',views.logi,name='logi'),
    path('home/',views.hello,name='home'),
    path('logout',views.logout,name='logout'),




]
