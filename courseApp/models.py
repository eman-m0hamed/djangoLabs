from django.db import models

# Create your models here.
class course(models.Model):
    title =  models.CharField(verbose_name="Title", max_length=255)
    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # trainees = models.ManyToManyField('trainee' , null = True, blank = True, related_name = 'Trainees courses')