from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from user.models import Profile
from django.forms.widgets import ClearableFileInput
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm
import datetime


class ClearableFileUpload(ClearableFileInput):
    initial_text = 'Núverandi mynd'
    input_text = 'Skipta um mynd'


class UpdateNameForm(ModelForm):
    class Meta:
        model = User
        exclude = [
            'id',
            'email',
            'username',
            'password',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'user_permissions',
            'groups'
        ]
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Eigið nafn'
        }


class ProfileForm(ModelForm, ClearableFileUpload):
    class Meta:
        model = Profile
        exclude = ['id', 'user']
        widgets = {
            'profile_image': ClearableFileUpload(attrs={'class': 'col-4'}),
            'kennitala': widgets.NumberInput(attrs={'class': 'form-control col-2 form-group-1'}),
            'phone_number': widgets.NumberInput(attrs={'class': 'form-control col-2 form-group-3'}),
            'address': widgets.TextInput(attrs={'class': 'form-control col-10 form-group-2'}),
            'postal_code': widgets.Select(attrs={'class': 'form-control col-2 form-group-3'}),
        }
        labels = {
            'profile_image': '',
            'kennitala': 'Kennitala',
            'phone_number': 'Sími',
            'address': 'Heimilisfang',
            'postal_code': 'Póstnúmer'
        }

    def clean_kennitala(self):
        kennitala_passed = self.cleaned_data.get('kennitala')
        kennitala_str = str(kennitala_passed)

        day = 0
        month = 0
        year = 0
        century = 0

        is_valid_length = False
        if len(kennitala_str) == 10:
            is_valid_length = True
            day = int(kennitala_str[0:2])
            month = int(kennitala_str[2:4])
            year = int(kennitala_str[4:6])
            century = int(kennitala_str[9])

        is_valid_birthday = self.is_date_of_birth_valid(day, month, year, century)

        is_valid_last_number = False
        if century == 0 or century == 9:
            is_valid_last_number = True

        if not is_valid_birthday or not is_valid_last_number or not is_valid_length:
            raise ValidationError('Kennitala er ógild.')
        return kennitala_passed

    def clean_phone_number(self):
        phone_number_passed = self.cleaned_data.get('phone_number')
        if len(str(phone_number_passed)) < 7 or len(str(phone_number_passed)) > 10:
            raise ValidationError('Símanúmer verður að vera 7-10 tölustafir að lengd.')
        return phone_number_passed

    def is_date_of_birth_valid(self, day, month, year_short, century):
        year = year_short
        if century == 9:
            year += 1900
        else:
            year += 2000

        if year > datetime.datetime.now().year:
            return False
        try:
            datetime.datetime(year=year, month=month, day=day)
            return True
        except ValueError:
            return False


class PasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = (
            'old_password',
            'password1',
            'password2'
        )

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError(self.error_messages['password_mismatch'])
        return password1
