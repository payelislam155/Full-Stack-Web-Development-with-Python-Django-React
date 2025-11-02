from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    inputEmail = models.EmailField()
    inputPhone = models.CharField(max_length=15)
    inputPassword = models.CharField(max_length=10)
    checkbox = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/',default=None, null=True)
    
    def __str__(self):
        return f"{self.name}"


