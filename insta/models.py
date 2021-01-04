from django.db import models
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    bio=models.TextField(max_length=100,blank=True,default="bio please...")
    profilepic=models.ImageField(upload_to='profile/', blank = True,default='../static/images/bad-profile-pic-2.jpeg')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    @classmethod
    def search_by_name(cls,search_term):
        news = cls.objects.filter(user__username__icontains = search_term)
        return news
