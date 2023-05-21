from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from traineeApp.models import *
# Create your views here.
def listTrainee(request):
   context={}
   context['pageTitle'] = 'trainees List'
   allTrainees = trainee.objects.all();
   context['trainees']= allTrainees;
   # context['deletedMessage']= deletedMessage;

   return render(request, 'trainees.html', context)

def addTrainee(request):
   context={}
   context['pageTitle'] = 'Add trainee'
   context['button'] = 'Add'
   if request.method == 'GET':
      return render(request, 'addTrainee.html', context)
   elif request.method == 'POST':
      name = request.POST['traineeName'] 
      email = request.POST['traineeEmail']
      Class = request.POST['traineeClass']
      trainee.objects.create(name = name, email = email, Class =  Class)
      if request.POST['button'] =="Register":
         return HttpResponseRedirect('/login')
      else :
         return HttpResponseRedirect('/trainees')
            
   else:
      return render(request, 'addTrainee.html', context)

def editTrainee(request, id):
   context={}
   context['pageTitle'] = 'Edit trainee'
   existTrainee = trainee.objects.get(id = id)
   if request.method == "GET":
      context['trainee'] = existTrainee
      return render(request, 'editTrainee.html', context)
   
   elif request.method == "PUT" or request.method == "POST":
      name = request.POST['traineeName'] 
      email = request.POST['traineeEmail'] 
      Class = request.POST['traineeClass']
      existTrainee.name = name;
      existTrainee.email = email;
      existTrainee.Class = Class;
      existTrainee.save()
      return HttpResponseRedirect('/trainees')

   
   
def deleteTrainee(request, id):
   existTrainee = trainee.objects.filter(id = id)
   existTrainee.delete()
   deletedMessage = "Trainee is Deleted Successfully"
   return HttpResponseRedirect('/trainees')

