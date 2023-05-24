from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from courseApp.models import *
# Create your views here.
def listCourse(request):
   # if 'userName' in request.session:      
   context={}
   context['pageTitle'] = 'Courses List'
   allCourses = course.objects.all();
   context['courses']= allCourses;
   return render(request, 'index.html', context)
   # else:
   #    return HttpResponseRedirect('/login')

def addCourse(request):
   if 'userName' in request.session: 
      context={}
      context['pageTitle'] = 'Add Course'
      if request. method == "GET":
         return render(request, 'addCourse.html', context)
      elif request. method == "POST":
         title = request.POST['courseTitle'] 
         description = request.POST['courseDescription']
         course.objects.create(title=title, description=description)
         return HttpResponseRedirect('/courses')
      else:
         return render(request, 'addCourse.html', context)
   else:
      return HttpResponseRedirect('/users/login')

def editCourse(request, id):
   if 'userName' in request.session: 
      context={}
      context['pageTitle'] = 'Edit Course'
      existCourse = course.objects.get(id = id)
      
      if request.method == "GET":
         context['course'] = existCourse
         return render(request, 'editCourse.html', context)
      
      elif request.method == "PUT" or request.method == "POST":
         title = request.POST['courseTitle'] 
         description = request.POST['courseDescription']
         existCourse.title = title;
         existCourse.description = description;
         existCourse.save()
         return HttpResponseRedirect('/courses')
   else:
      return HttpResponseRedirect('/users/login')
   
def deleteCourse(request, id):
   if 'userName' in request.session: 
      existCourse = course.objects.get(id = id)
      existCourse.delete()
      deletedMessage = "Course is Deleted Successfully"
      return HttpResponseRedirect('/courses')
   else:
      return HttpResponseRedirect('/users/login')