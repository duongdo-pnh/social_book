from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def index(request):
    user=User.objects.get(username=request.user)
    user_profile=Profile.objects.get(user=user)
    profile=Post.objects.all()
    return render(request,'index.html',{'profile':profile,'user_profile':user_profile})
def login(request):
   if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      myuser=authenticate(username=username,password=password)
      if myuser is None:
         messages.error(request,'password not valid')
         return render(request,'login.html')
      else:
         auth.login(request,myuser)
         return redirect('home')
   else:
      return render(request,'login.html')
 
      
def register(requets):
   form=SignupForm()
   if requets.method=='POST':
     form=SignupForm(requets.POST)
     if form.is_valid():
        form.save()
        messages.success(requets,'Create success')
        username=requets.POST.get('username')
        user_model=User.objects.get(username=username)
        user_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
        user_profile.save()
   context={'form':form}
   return render(requets,'register.html',context)

def logout(request):
    auth.logout(request)
    return redirect('login')

def setting(request):
   user_profile=Profile.objects.get(user=request.user)
   if request.method == 'POST':
      if request.FILES.get('image')==None:
         user_profile.profileimg=user_profile.profileimg
      else:
         user_profile.profileimg=request.FILES.get('image')
      user_profile.bio=request.POST.get('bio')
      user_profile.location=request.POST.get('location')
      user_profile.save()
   context={'user':user_profile}
   return render(request, "setting.html", context)

def uploadFile(request):
   if request.method=='POST':
      image=request.FILES.get('image')
      user=request.user.username
      caption=request.POST.get('cap')
      user_upload=Post.objects.create(user=user,image=image,caption=caption)
      user_upload.save()
      return redirect('home')
 
def post_like(request):
   username=request.user.username
   post_id=request.GET.get('post_id')
   post=Post.objects.get(id=post_id)

   like=Postlike.objects.filter(username=username,post_id=post_id).first()
   if like == None:
      like_filter=Postlike.objects.create(username=username,post_id=post_id)
      like_filter.save()
      post.no_of_likes = post.no_of_likes + 1
      post.save()
      return redirect('home')

   else:
      like.delete()
      post.no_of_likes = post.no_of_likes - 1
      post.save()
      return redirect('home')



   
      