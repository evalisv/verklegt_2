from django.forms import ModelForm, widgets
import datetime
from offer.models import Offer


class MakeOfferForm(ModelForm):
   class Meta:
        model = Offer
        exclude = ['id', 'estate', 'offer_maker', 'payment', 'counter_offer_to',]
        widgets = {
            "amount": widgets.NumberInput(attrs={"class": "form-control"}),
            "expires": widgets.SelectDateWidget(attrs={"class": "form-control col-4 float-left"}),
            "offer_made": widgets.HiddenInput(attrs={"value": datetime.datetime.now()}),
            "payed": widgets.HiddenInput(attrs={"value": False}),
            "status": widgets.HiddenInput(attrs={"value": "Incoming"}),
        }
        labels = {
            "amount": "Upphæð",
            "expires": "Gildir til"
        }

