from django.forms import ModelForm, widgets
from estate.models import Estate
from django.contrib.auth.models import User
import datetime
from payment.models import Payment

class PaymentForm(ModelForm):
    # image = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Payment
        exclude = ['id', 'received', 'estate_id', 'buyer_id', 'seller_id']
        widgets = {
            'amount': widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"}),
            'card_number': widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"}),
            'expiration': widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"}),
            'cvc': widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"})
        }

        labels = {
            'amount': 'Upphæð',
            'card_number': 'Kortanúmer',
            'expiration': 'Gildistími',
            'cvc': 'CVC Öryggisnúmer',
        }
