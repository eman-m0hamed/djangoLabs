from django.db import models

# Create your models here.
class myUser(models.Model):
    email =  models.EmailField(verbose_name="Email", max_length=255, unique=True)
    name =  models.CharField(verbose_name="name", max_length=255)
    password =  models.CharField(verbose_name="Password", max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)