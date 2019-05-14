from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from user.models import Profile
from django.core.exceptions import ValidationError
from django.forms.widgets import ClearableFileInput

class ClearableFileUpload(ClearableFileInput):
    initial_text = 'Núverandi mynd'
    input_text = 'Skipta um mynd'

class UpdateNameForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'email', 'username', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'user_permissions', 'groups']
        widgets = {
            'first name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last name': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(ModelForm, ClearableFileUpload):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'kennitala']
        widgets = {
            'profile_image': ClearableFileUpload(attrs={'class': 'col-4'}),
        }
        labels = {
            'profile_image': '',
        }



# initial_text = 'currently'
#     input_text = 'change'
#     clear_checkbox_label = 'clear'

# 'kennitala': widgets.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),