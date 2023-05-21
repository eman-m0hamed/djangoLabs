from django.urls import path
from courseApp.views import *

urlpatterns = [
    path('', listCourse, name='coursesList'),
    path('add', addCourse, name='addCourse'),
    path('edit/<int:id>', editCourse, name='editCourse'),
    path('delete/<int:id>', deleteCourse, name='deleteCourse')
]
