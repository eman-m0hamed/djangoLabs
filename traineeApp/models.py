from django.db import models
from courseApp.models import *
# Create your models here.
class trainee(models.Model):
    name =  models.CharField(verbose_name="Name", max_length=255)
    email =  models.EmailField(verbose_name="Email", max_length=255, unique=True)
    course =  models.ForeignKey(course, on_delete=models.CASCADE,verbose_name="course", null=True)
    created_at = models.DateTimeField(auto_now_add= True)
