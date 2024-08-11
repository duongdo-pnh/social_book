from datetime import timezone
import uuid
import django
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,related_name='profile',on_delete=models.CASCADE,primary_key=True)
    id_user=models.IntegerField(default=0)
    bio=models.TextField(blank=True)
    profileimg=models.ImageField(upload_to="profile_images",default='profile_images/1.png')
    location=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username
    @property
    def ImageURL(self):
        try:
            url=self.profileimg.url
        except:
            url=''
        return url
    
class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_image')
    caption=models.TextField(max_length=100,null=True)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user
    
class Postlike(models.Model):
    post_id=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    