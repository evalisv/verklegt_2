from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import User as MetaUser


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    kennitala = forms.IntegerField(required=True)
    phone_number = forms.IntegerField(required=True)
    address = forms.CharField(max_length=255, required=True)
    postal_code = forms.IntegerField()

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Meta user without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        meta_user = MetaUser(auth_user_id=user, kennitala=self.cleaned_data['kennitala'],
                             phone_number=self.cleaned_data['phone_number'])
        meta_user.save()
        return user

