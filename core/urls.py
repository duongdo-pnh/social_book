
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='home'),
   path('login',views.login,name='login'),
   path('register',views.register,name='register'),
   path('logout',views.logout,name='logout'),
   path('setting',views.setting,name='setting'),
   path('upload',views.uploadFile,name='upload'),
   path('like-post',views.post_like,name='like-post')



]