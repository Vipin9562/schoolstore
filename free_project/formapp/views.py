from django.contrib import messages
from django.shortcuts import render, redirect
from formapp.models import Student


# Create your views here.

def student_form(request):
    return render(request, 'student_form.html')


def students(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        last1 = request.POST.get('materials')

        student_details = Student(name=name, dob=dob, age=age, gender=gender,
                                  phone_number=phone, email=email, address=address, department=department,
                                  course=course, purpose=purpose, last=last1)
        student_details.save();
        messages.success(request,'Successfully Submitted')
        return render(request,'student_form.html')


