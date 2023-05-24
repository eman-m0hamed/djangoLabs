from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from traineeApp.models import *
from courseApp.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def listTrainee(request):
   # if 'userName' in request.session:
   context={}
   context['pageTitle'] = 'trainees List'
   allTrainees = trainee.objects.all();
   context['trainees']= allTrainees;
   return render(request, 'trainees.html', context)
   # else:
   #    return HttpResponseRedirect('/login')


# @login_required
def addTrainee(request):
   if 'userName' in request.session:
      context={}
      context['pageTitle'] = 'Add trainee'
      context['button'] = 'Add'
      allCourses = course.objects.all();
      context['courses']= allCourses;
      if request.method == 'GET':
         return render(request, 'addTrainee.html', context)
      elif request.method == 'POST':
         name = request.POST['traineeName'] 
         email = request.POST['traineeEmail']
         Course = request.POST['traineeCourse']
         trainee.objects.create(name = name, email = email, course =  Course)
         return HttpResponseRedirect('/trainees')
               
      else:
         return render(request, 'addTrainee.html', context)
   else:
      return HttpResponseRedirect('/users/login')

def editTrainee(request, id):
   if 'userName' in request.session:
      context={}
      context['pageTitle'] = 'Edit trainee'
      existTrainee = trainee.objects.get(id = id)
      allCourses = trainee.objects.all();
      context['courses']= allCourses;
      if request.method == "GET":
         context['trainee'] = existTrainee
         return render(request, 'editTrainee.html', context)
      
      elif request.method == "PUT" or request.method == "POST":
         name = request.POST['traineeName'] 
         email = request.POST['traineeEmail'] 
         course = request.POST['traineeCourse']
         existTrainee.name = name;
         existTrainee.email = email;
         existTrainee.course = course;
         existTrainee.save()
         return HttpResponseRedirect('/trainees')
   else:
      return HttpResponseRedirect('/users/login')

      
      
def deleteTrainee(request, id):
   if 'userName' in request.session:
      existTrainee = trainee.objects.filter(id = id)
      existTrainee.delete()
      return HttpResponseRedirect('/trainees')
   else:
      return HttpResponseRedirect('/users/login')

