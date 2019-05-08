from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    email = forms.CharField(max_length=255)
    kennitala = forms.IntegerField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=255)
    postal_code = forms.IntegerField()

    #Til að exclude-a reit við register.
    #exclude = ['id', 'user']
    class Meta:
        model = User
        exclude = ['id', 'password', 'username', 'is_active', 'date_joined', 'is_staff', 'last_login'
                       , 'is_superuser', 'auth_user_pkey', 'group_id', 'user_permissions', 'groups',  'watchlist']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        return user

