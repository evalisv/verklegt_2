from django.shortcuts import render
from models import Vhistory
import datetime

# Create your views here.
# Vhistory.objects.all

def index(request):
    return render(request, 'user/index.html') #Athuga þetta síðar.

def update_vhistory(request,address, date):
    today = datetime.today()
    for estate in vhistory.objects.all()
        if address == estate.address:
        estate.view_date =  today
            return
    entry = Vhistory(address=address, date=date)
    entry.save()

def get_vhistory(request):
    return render(Vhistory.objects.all().order_by('-date'), 'vhistory.html',{
        'estate': get_object_or_404(Estate,pk=id)
    })
