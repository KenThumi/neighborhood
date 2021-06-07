from .models import Post, Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nat_id','location']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         exclude = ['project','count']
