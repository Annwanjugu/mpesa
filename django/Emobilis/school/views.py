from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse("WELCOME TO EMOBILIS")
def contact(request):
    return HttpResponse("CONTACT US")
