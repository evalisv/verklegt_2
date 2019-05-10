from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    password1 = forms.CharField(
                            label="Password",
                            max_length=100,
                            min_length=8,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(
                            label="Confirm Password",
                            max_length=100,
                            min_length=8,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == '':
            raise forms.ValidationError()
        return first_name

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('p1 not match p2')
        return password1

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Passwords Do Not Match')














