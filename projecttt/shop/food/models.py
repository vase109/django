from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Food(models.Model):
    name=models.CharField(default='no name' , max_length=50)
    text=models.TextField()
    author=models.ForeignKey(User,  on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    published=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='food/')
   