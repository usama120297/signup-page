from django.http import HttpResponse, Http404
from .models import *
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    template = loader.get_template('signup/signup.html')
    context = {}
    return HttpResponse(template.render(context, request))

def success(request):
    HttpResponse(' <h2>your data has been saved</h2> ')

def adddata(request):
    name = request.POST['t1']
    age = request.POST['t2']
    print(name)
    gender = request.POST['gender']
    studentObj = Student.objects.create(
            name = name,
            age = age,
            gender = gender,
            )

    studentObj.save()
    # template = loader.get_template("signup/success.html")
    return HttpResponse("<h1>Your response has successfully saved</h1>")

def showdata(request):
    temp = Student.objects.all()
    template = loader.get_template('signup/show.html')
    context = { 'temp' : temp}
    return HttpResponse(template.render(context,request))