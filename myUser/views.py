from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from myUser.models import *
# Create your views here.


def register(request):
    context={}
    if request.method == 'GET':
        return render(request, 'register.html', context)
    elif request.method == 'POST':
        name = request.POST['Name'] 
        email = request.POST['Email']
        password = request.POST['Password']
        myUser.objects.create(name = name, email = email, password =  password)
        return HttpResponseRedirect('/login')

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
      
      existUser = myUser.objects.filter(email = email)

      if existUser:
         if existUser[0].password == password:
            return HttpResponseRedirect('/courses')
         else: 
            context['ClassError'] ="Invalid Class"
            return render(request, 'login.html', context)
      else:
         context['emailError'] ="Invalid Email"
         return render(request, 'login.html', context)
    
def logOut(request):
   return HttpResponse("<h1>LogOut</h1>")