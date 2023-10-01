from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login

from formapp.models import Student


# Create your views here.
def demo(request):
    return render(request, 'index.html')


def student_form(request):
    return render(request, 'student_form.html')


def hello(request):
    return render(request, 'home.html')


def log(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('freeapp:home')
        else:
            messages.warning(request, "Incorrect password or Username")
            return redirect('freeapp:log')

    return render(request, 'login.html')


def logi(request):
    return render(request, 'login.html')


def regist(request):
    return render(request, 'register.html')


def regi(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password1")

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Taken")
                return redirect('freeapp:regi')
            else:
                my_user = User.objects.create_user(username=username, password=pass1)
                my_user.save()
                return render(request, 'login.html')
        else:
            messages.info(request,"passwords are note same")
            return redirect('freeapp:regi')


    return render(request, 'register.html')


def one_r(request):
    return redirect("https://en.wikipedia.org/wiki/Computer_science")


def two_r(request):
    return redirect("https://en.wikipedia.org/wiki/Biology")


def three_r(request):
    return redirect("https://en.wikipedia.org/wiki/Business_mathematics")


def four_r(request):
    return redirect("https://en.wikipedia.org/wiki/Commerce")


def five_r(request):
    return redirect("https://en.wikipedia.org/wiki/Humanities")


def logout(request):
    return render(request,'login.html')