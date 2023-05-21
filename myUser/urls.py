from django.urls import path
from myUser.views import *

urlpatterns = [
    path('', login, name='login'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logOut', logOut, name='logOut')
    
]
