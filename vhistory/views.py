from django.shortcuts import render
from vhistory.models import Vhistory
import datetime

def index(request):
    return render(request, 'user/index.html')

def update_vhistory(address, date):
    today = datetime.today()
    for estate in Vhistory.objects.all():
        if address == estate.address:
            estate.view_date =  today
                return
    entry = Vhistory(address=address, date=date)
    entry.save()

def get_vhistory(request):
    return render(Vhistory.objects.all().order_by('-date'), 'vhistory.html',{
        'estate': get_object_or_404(Estate,pk=id)
    })
