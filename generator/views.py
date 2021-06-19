from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.
def home(request):
    return render(request,'Home.html')

def generated_password(request):
    length=int(request.GET.get('Length'))
    characters=list(string.ascii_lowercase)
    if request.GET.get('Uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('Numbers'):
        characters.extend(map(str,range(0,10)))
    if request.GET.get('Special Characters'):
        characters.extend(list('!@#$%&*'))
    password=''
    for i in range(length):
        password+=random.choice(characters)

    return render(request,"Generated_Password.html",{'Password':password})

def about(request):
    return render(request,'about.html')