from django.shortcuts import render
from django.http import HttpResponse
from estate.models import Municipality, Estate


def homepage(request):
    context = {'postal_codes': Municipality.objects.all(),
               'estates': Estate.objects.filter(on_sale=True).order_by('-date_listed')[:6]}
    return render(request, 'home.html', context)

def about_us(request):
    return render(request, 'footer/about.html')

def contact(request):
    return render(request, 'footer/contact.html')

def terms(request):
    return render(request, 'footer/terms.html')
