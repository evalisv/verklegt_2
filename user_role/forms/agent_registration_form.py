from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Notendanafn',
        max_length=255,
        required=True
    )
    first_name = forms.CharField(
        label='Eigið nafn',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-sm-8 form-group-1'})
    )
    last_name = forms.CharField(
        label='Eftirnafn',
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control col-sm-8 form-group-2'})
    )
    email = forms.EmailField(
        label='Netfang',
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control col-sm-8 form-group-3'})
    )
    password1 = forms.CharField(
        label='Lykilorð',
        max_length=100,
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control col-sm-8 form-group-4'})
    )
    password2 = forms.CharField(
        label='Lykilorð endurtekið',
        max_length=100,
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'form-control col-sm-8 form-group-5'})
    )
    kennitala = forms.CharField(
        label='Kennitala',
        widget=forms.NumberInput(attrs={'class': 'form-control col-sm-3 form-group-6'})
    )
    phone_number = forms.CharField(
        label='Sími',
        widget=forms.NumberInput(attrs={'class': 'form-control col-sm-3 form-group-6'})
    )
    address = forms.CharField(
        label='Heimilisfang',
        widget=forms.TextInput(attrs={'class': 'form-control col-sm-8 form-group-7'})
    )
    postal_code = forms.ChoiceField(
        label='Póstnúmer',
        choices=postal_codes,
        widget=forms.Select(attrs={'class': 'form-control col-sm-3 form-group-8'})
    )
    country = forms.ChoiceField(
        label='Land',
        choices=countries,
        widget=forms.Select(attrs={'class': 'form-control col-sm-3 form-group-8'})
    )
    profile_image = forms.FileField(
        label='Mynd',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'kennitala',
            'phone_number',
            'address',
            'postal_code',
            'country'
        )


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Lykilorð passar ekki við lykilorð endurtekið.')
        return password1
