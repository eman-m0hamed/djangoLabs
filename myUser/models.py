from django.db import models

# Create your models here.
class myUser(models.Model):
    name =  models.CharField(verbose_name="name", max_length=255)
    email =  models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password =  models.CharField(verbose_name="Password", max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)