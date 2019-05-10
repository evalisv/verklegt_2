from django.forms import ModelForm, widgets
from django import forms
from estate.models import Estate
from django.contrib.auth.models import User
import datetime


class UpdateEstateForm(ModelForm):
    image = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Estate
        exclude = ["id", "estate_seller", "open_house", "date_listed", "views", "address","postal_code", "size",
                   "bedrooms", "bathrooms", "fasteignamat", "brunabotamat", "type", "year_built", "entry", "garage",
                   "elevator"]
        widgets = {
            "price": widgets.NumberInput(attrs={"class": "form-control"}),
            "description": widgets.TextInput(attrs={"class": "form-control"})
        }

class RegisterEstateForm(ModelForm):
    # image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class': 'form-control'}))

    class Meta:
        model = Estate
        exclude = ['id', 'open_house', 'estate_seller']
        widgets = {
            "address" : widgets.TextInput(attrs={"class": "form-control col-sm-6 address form-group-1"}),
            "postal_code": widgets.Select(attrs={"class": "form-control col-sm-2 postal-code form-group-1"}),
            "price": widgets.NumberInput(attrs={"class": "form-control col-sm-2 price form-group-3"}),
            "fasteignamat": widgets.NumberInput(attrs={"class": "form-control col-sm-2 fasteignamat form-group-3"}),
            "brunabotamat": widgets.NumberInput(attrs={"class": "form-control col-sm-2 brunabotamat form-group-3"}),
            "size" : widgets.NumberInput(attrs={"class": "form-control col-sm-2 size form-group-2"}),
            "bedrooms": widgets.NumberInput(attrs={"class": "form-control col-sm-2 bedrooms form-group-2"}),
            "bathrooms": widgets.NumberInput(attrs={"class": "form-control col-sm-2 bathrooms form-group-2"}),
            "description": widgets.Textarea(attrs={"class": "form-control col-sm-10 form-group-6"}),
            "type": widgets.Select(attrs={"class": "form-control col-sm-2 type form-group-4"}),
            "year_built": widgets.NumberInput(attrs={"class": "form-control col-sm-2 year-built form-group-4"}),
            "entry": widgets.CheckboxInput(attrs={"class": "checkbox col-sm-2 entry form-group-5"}),
            "garage": widgets.CheckboxInput(attrs={"class": "checkbox col-sm-2 garage form-group-5"}),
            "elevator": widgets.CheckboxInput(attrs={"class": "checkbox  col-sm-2 garage form-group-5"}),
            "views": widgets.HiddenInput(attrs={"value": 0, "required": False}),
            "date_listed": widgets.HiddenInput(attrs={"value": datetime.datetime.now(), "required": False}),
            "images": widgets.ClearableFileInput(attrs={'multiple': True, "class": "col-sm-10 images form-group-7"}),
        }
        labels = {
            "address": "Heimilisfang",
            "postal_code": "Póstnúmer",
            "price": "Verð",
            "brunabotamat": "Brunabótamat",
            "size": "Fermetrar",
            "bedrooms": "Svefnherbergi",
            "bathrooms": "Baðherbergi",
            "description": "Lýsing",
            "type": "Tegund",
            "year_built": "Byggingarár",
            "entry": "Sérinngangur",
            "garage": "Bílskúr",
            "elevator": "Lyfta",
            "images": "Myndir"
        }

