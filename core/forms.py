from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'name': "username",
            'id' : 'username',
            'type': 'text',
            'placeholder' : 'Enter Username.....',
            'class' : 'bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;'
                     
        })

        self.fields['email'].widget.attrs.update({
            'name': "email",
            'id' : 'email',
            'type': 'email',
            'placeholder' : 'Enter Email.....',
            'class' : 'bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;'
                     
        })

        self.fields['password1'].widget.attrs.update({
            'required' : "",
            'name': "password1",
            'id' : 'password1',
            'type': 'text',
            'placeholder' : 'Enter password.....',
            'class' : 'bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;'
                     
        })

        self.fields['password2'].widget.attrs.update({
            'required' : "",
            'name': "password2",
            'id' : 'password2',
            'type': 'text',
            'placeholder' : 'Confirm password.....',
            'class' :'bg-gray-200 mb-2 shadow-none  dark:bg-gray-800" style="border: 1px solid #d3d5d8 !important;'
                     
        })


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class User_Profile_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs.update({
            'name': 'bio',
            'id' : 'about',
            'type': 'textarea',
            'row':'3',
            'placeholder' : 'Enter Username.....',
            'class' : 'shadow-none bg-gray-100'
                     
        })

        self.fields['location'].widget.attrs.update({
            'name': "location",
            'id' : 'location',
            'type': 'text',
            'placeholder' : 'Enter Location',
            'class' : 'shadow-none bg-gray-100',
            'value':'{{user.location}}'
                     
        })
        self.fields['profileimg'].widget.attrs.update({
            'name': "profileimg",
            'id' : 'img',
            'type': 'file',
            'placeholder' : 'Confirm password.....',
            'class' :'shadow-none bg-gray-10',
            
                     
        })

    class Meta:
        model = Profile
        fields = ("bio", "profileimg","location")