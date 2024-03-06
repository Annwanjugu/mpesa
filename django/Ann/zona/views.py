
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def home(request):
    return render(request, 'index.html')
def students(request):
    s = Student.objects.all()
    return render(request, 'students.html', {"pupil":s})

