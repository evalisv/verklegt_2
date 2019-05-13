from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from user.models import Profile
from django.core.exceptions import ValidationError

class UpdateNameForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'email', 'username', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups']
        widgets = {
            'first name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last name': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'profile_image': widgets.ClearableFileInput(attrs={'class': 'form-control'}),
            'kennitala': widgets.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.NumberInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal_code': widgets.Select(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'profile_image': 'Mynd',
            'phone_number': 'Sími',
            'address': 'Heimilisfang',
            'postal_code': 'Póstnúmer',
            'country': 'Land'
        }

