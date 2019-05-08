from django.forms import ModelForm, widgets
from django import forms
from estate.models import Estate

class UpdateEstateForm(ModelForm):
    image = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Estate
        exclude = ['id', 'estate_seller', 'open_house', 'date_listed', 'views', 'address','postal_code', 'size',
                   'bedrooms', 'bathrooms', 'fasteignamat', 'brunabotamat', 'type', 'year_built', 'entry', 'garage',
                   'elevator']
        widgets = {
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'})
        }

class RegisterEstateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control'}))

    class Meta:
        model = Estate
        exclude = [ 'id', 'estate_seller', 'open_house', 'date_listed', 'views' ]
        widgets = {
            'address' : widgets.TextInput(attrs={ 'class': 'form-control'}),
            'postal_code': widgets.Select(attrs={'class': 'form-control'}),
            'size' : widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'bedrooms': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'bathrooms': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'fasteignamat': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'brunabotamat': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'type': widgets.Select(attrs={ 'class': 'form-control'}),
            'year_built': widgets.NumberInput(attrs={ 'class': 'form-control'}),
            'entry': widgets.CheckboxInput(attrs={ 'class': 'checkbox'}),
            'garage': widgets.CheckboxInput(attrs={ 'class': 'checkbox'}),
            'description': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'elevator': widgets.CheckboxInput(attrs={ 'class': 'checkbox'})
        }