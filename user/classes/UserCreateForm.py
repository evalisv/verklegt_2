from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import User as MetaUser


class UserCreateForm(UserCreationForm):
    kennitala = forms.IntegerField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=255)
    postal_code = forms.IntegerField()

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and Meta user without database save")
        user = super(UserCreateForm, self).save(commit=True)
     #   user.email = self.cleaned_data["email"]
     #   user.first_name = self.cleaned_data["first_name"]
      #  user.last_name = self.cleaned_data["last_name"]

      #  user.save()

        meta_user = MetaUser(auth_user_id=user.id
                             ,kennitala=self.cleaned_data['kennitala']
                             ,phone_number=self.cleaned_data['phone_number']
                             ,address=self.cleaned_data['address']
                             ,postal_code=self.cleaned_data['postal_code'])
        meta_user.save()
        return user, meta_user

