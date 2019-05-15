from django.forms import ModelForm, widgets
from estate.models import Estate
from django.contrib.auth.models import User
import datetime
from payment.models import Payment
from django.core.exceptions import ValidationError

class PaymentForm(ModelForm):
    # image = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Payment
        exclude = ['id', 'estate_id', 'buyer_id', 'seller_id']
        widgets = {
            'card_number': widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"}),
            'expiration': widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"}),
            'cvc': widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"}),
            'received': widgets.HiddenInput(attrs={"value": datetime.datetime.now(), "required": False}),
        }

        labels = {
            'card_number': 'Kortanúmer',
            'expiration': 'Gildistími',
            'cvc': 'CVC Öryggisnúmer',
        }
    def clean_card_number(self):
        card_number_passed = self.cleaned_data.get('card_number')
        if len(str(card_number_passed)) != 16:
            raise ValidationError('Kortanúmer er ógilt.')
        return card_number_passed

    def clean_expiration(self):
        expiration_passed = self.cleaned_data.get('expiration')
        if len(str(expiration_passed)) != 4 and expiration_passed > 3112:
            raise ValidationError('Gildistími korts er ógildur.')
        return expiration_passed

    def clean_cvc(self):
        cvc_passed = self.cleaned_data.get('cvc')
        if len(str(cvc_passed)) != 3:
            raise ValidationError('Kortanúmer er ógilt.')
        return cvc_passed

