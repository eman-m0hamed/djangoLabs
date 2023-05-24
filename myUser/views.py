from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from myUser.models import *
from .forms import userFom
# Create your views here.

def register(request):
    context={}
    myForm = userFom
    if request.method == 'GET':
      context['myForm'] = myForm
      return render(request, 'register.html', context)
    elif request.method == 'POST':
      myForm = userFom(request.POST)
      if myForm.is_valid():
         instance = myForm.save()
         return HttpResponseRedirect('/login')
 

# def register(request):
#     context={}
#     if request.method == 'GET':
#         return render(request, 'register.html', context)
#     elif request.method == 'POST':
#         name = request.POST['Name'] 
#         email = request.POST['Email']
#         password = request.POST['Password']
#         myUser.objects.create(name = name, email = email, password =  password)
#         return HttpResponseRedirect('/users/login')

def login(request):
   context={}
   if request.method == "GET":
      return render(request, 'login.html', context)
   
   elif request.method == "POST":
      email = request.POST['Email']
      password = request.POST['Password']
      context['form']={"email":email, "password": password}
      if not email:
        context['emailError'] ="Email is Required"
        return render(request, 'login.html', context)
      elif not password: 
        context['passwordError'] ="Password is Required"
        return render(request, 'login.html', context)
      
      existUser = myUser.objects.filter(email = email).first()

      if existUser:
         if existUser.password == password:
            request.session['userName'] = existUser.name
            return HttpResponseRedirect('/courses')
         else: 
            context['passwordError'] ="Invalid Password"
            return render(request, 'login.html', context)
      else:
         context['emailError'] ="Invalid Email"
         return render(request, 'login.html', context)
    
def logOut(request):
   request.session.clear();
   return HttpResponse("<h1>LogOut</h1> <a href='/users/login'>Login Again</a>")
   
 

