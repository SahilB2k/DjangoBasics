from django.db import models
from django.utils import timezone

# Create your models here.
class deployedProjects(models.Model):
    PROJECT_TYPE=[
        ('Py','PYTHON'),
        ('J','JAVA'),
        ('ML','Machine Learning'),
        ('Js','Javascript'),

        
    ]
    name=name = models.CharField(max_length=1000)
    image=models.ImageField( upload_to="images/", height_field=None, width_field=None, max_length=None)
    Date=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=PROJECT_TYPE)



    def __str__(self):
        return self.name