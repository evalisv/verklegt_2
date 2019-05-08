from django.forms import ModelForm, widgets
from django import forms
from user.models import User

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
