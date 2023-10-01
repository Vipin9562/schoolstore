from django.urls import path
from . import views

app_name = 'formapp'

urlpatterns = [

     path('students',views.students, name='students')

    # Add more URLs as needed
]
