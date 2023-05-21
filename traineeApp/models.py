from django.db import models

# Create your models here.
class trainee(models.Model):
    name =  models.CharField(verbose_name="Name", max_length=255)
    email =  models.EmailField(verbose_name="Email", max_length=255, unique=True)
    Class =  models.CharField(verbose_name="Class", max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
