from django.forms import ModelForm, widgets
import datetime
from offer.models import Offer
from django.core.exceptions import ValidationError

class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer
        exclude = ['id', 'estate', 'offer_maker', 'payment', 'counter_offer_to',]
        widgets = {
            "amount": widgets.NumberInput(attrs={"class": "form-control"}),
            "expires": widgets.SelectDateWidget(attrs={"class": "form-control"}),
            "offer_made": widgets.HiddenInput(attrs={"value": datetime.datetime.now()}),
            "payed": widgets.HiddenInput(attrs={"value": False}),
            "status": widgets.HiddenInput(attrs={"value": "Incoming"}),
        }
        labels = {
            "amount": "Upphæð",
            "expires": "Gildir til"
        }

    def clean_amount(self):
        amount_passed = self.cleaned_data.get('amount')
        if amount_passed < 0:
            raise ValidationError('Upphæð verður að vera hærri en 0.')
        return amount_passed

    def clean_expires(self):
        expires_passed = self.cleaned_data.get('expires')
        todays_date = datetime.today()
        if todays_date > expires_passed:
            raise ValidationError('Dagsetning má ekki vera liðin.')
        return expires_passed







