from django.urls import path
from traineeApp.views import *

urlpatterns = [
    path('', listTrainee, name='traineesList'),
    path('add', addTrainee, name='addTrainee'),
    path('edit/<int:id>', editTrainee, name='editTrainee'),
    path('delete/<int:id>', deleteTrainee, name='deleteTrainee')
    
]
