from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from user.models import Profile
from django.forms.widgets import ClearableFileInput
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

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
        exclude = ['id', 'user']
        widgets = {
            'profile_image': ClearableFileUpload(attrs={'class': 'col-4'}),
            'kennitala': widgets.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': widgets.NumberInput(attrs={'class': 'form-control col-2 form-group-3'}),
            'address': widgets.TextInput(attrs={'class': 'form-control col-10 form-group-2'}),
            'postal_code': widgets.Select(attrs={'class': 'form-control col-2 form-group-3'}),
            'country': widgets.Select(attrs={'class': 'form-control col-2 form-group-3'}),
        }
        labels = {
            'profile_image': '',
            'kennitala': 'Kennitala',
            'phone_number': 'Sími',
            'address': 'Heimilisfang',
            'postal_code': 'Póstnúmer',
            'country': 'Land'
        }

    # def clean_kennitala(self):
    #     kennitala_passed = self.cleaned.data.get('kennitala')
    #     kennitala_str = str(kennitala_passed)
    #     if len(kennitala_str) != 10 and 31 < int(kennitala_str[0:2]) < 0 and 13 < int(kennitala_str[2:4]) < 0:
    #         raise ValidationError('Kennitala er ógild.')
    #     return kennitala_passed
    #
    # def clean_phone_number(self):
    #     phone_number_passed = self.cleaned.data.get('phone_number')
    #     if 10 < len(str(phone_number_passed)) < 7:
    #         raise ValidationError('Símanúmer verður að vera á milli 7-10 tölustafir að lengd.')
    #     return phone_number_passed
    #

class PasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = (
        'old_password'
        'password1',
        'password2'
        )




# initial_text = 'currently'
#     input_text = 'change'
#     clear_checkbox_label = 'clear'

# 'kennitala': widgets.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),


