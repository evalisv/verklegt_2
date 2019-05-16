from django.forms import ModelForm, widgets
from estate.models import Estate
from django.contrib.auth.models import User
import datetime
from payment.models import Payment
from django.core.exceptions import ValidationError
from django import forms

class PaymentForm(forms.Form):
    card_number = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3", "label": "Kortanúmer"}))
    expiration = forms.IntegerField( widget=forms.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3", "label": "Gildistími"}))
    cvc = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3", "label": "CVC öryggisnúmer"}))

    def clean_card_number(self):
        card_number_passed = self.cleaned_data['card_number']
        if len(str(card_number_passed)) != 16:
            raise ValidationError('Kortanúmer er ógilt.')
        return card_number_passed

    def clean_expiration(self):
        expiration_passed = self.cleaned_data['expiration']
        if len(str(expiration_passed)) != 4 and expiration_passed > 3112:
            raise ValidationError('Gildistími korts er ógildur.')
        return expiration_passed

    def clean_cvc(self):
        cvc_passed = self.cleaned_data['cvc']
        if len(str(cvc_passed)) != 3:
            raise ValidationError('Kortanúmer er ógilt.')
        return cvc_passed

