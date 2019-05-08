from django.forms import ModelForm, widgets
<<<<<<< HEAD
from django import forms
from user.models import User
from user.models import Profile

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'kennitala', 'email', 'watchlist', 'auth_user_id']
        widgets = {
            'first name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.Select(attrs={'class': 'form-control'})
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }

