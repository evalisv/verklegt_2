import datetime
from django.core.exceptions import ValidationError
from django import forms


class PaymentForm(forms.Form):
    months = []
    current_year = datetime.datetime.now().year
    years = []

    for i in range(1, 13):
        option = ''
        if i < 10:
            option = '0' + str(i)
        else:
            option = str(i)
        months.append((i, option))

    for i in range(current_year, current_year + 10):
        years.append((i, i))

    card_number = forms.IntegerField(
        label='Kortanúmer',
        widget=forms.NumberInput(attrs={'class': 'form-control col-sm-2 card-number form-group-3'})
    )
    expiration_month = forms.ChoiceField(
        label='Gildistími',
        choices=months,
        widget=forms.Select(attrs={'class': 'form-control col-sm-2 exp-month form-group-3'})
    )
    expiration_year = forms.ChoiceField(
        label='',
        choices=years,
        widget=forms.Select(attrs={'class': 'form-control col-sm-2 exp-year form-group-3'})
    )
    cvc = forms.IntegerField(
        label='CVC öryggisnúmer',
        widget=forms.NumberInput(attrs={'class': 'form-control col-sm-2 price form-group-3'})
    )

    def clean_card_number(self):
        card_number_passed = self.cleaned_data['card_number']
        if len(str(card_number_passed)) != 16:
            raise ValidationError('Kortanúmer er ógilt.')
        return card_number_passed

    def clean_expiration_month(self):
        expiration_year =self.data['expiration_year']
        expiration_month = self.cleaned_data['expiration_month']
        if int(expiration_year) == datetime.datetime.now().year and int(expiration_month) < datetime.datetime.now().month:
            raise ValidationError('Gildistími korts er ógildur.')
        return expiration_month

    def clean_cvc(self):
        cvc_passed = self.cleaned_data['cvc']
        if len(str(cvc_passed)) != 3:
            raise ValidationError('CVC númer er ógilt.')
        return cvc_passed

