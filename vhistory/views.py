from django.shortcuts import render
from vhistory.models import Vhistory
import datetime
from django.utils import timezone

def index(request):
    context = {'estate': estate}
    return render('vhistory/index.html', context)

def update_vhistory(user, estate):
    #today = datetime.date(datetime.today())
    today = timezone.now()
    for viewed_estate in Vhistory.objects.all():
        if estate.address == viewed_estate.address:
            viewed_estate.view_date = today
            return
    entry = Vhistory(user=user, estate=estate, view_date=today)
    entry.save()

def get_vhistory(request):
    return render(Vhistory.objects.all().order_by('-date'), 'vhistory/index.html',{
        'estate': get_object_or_404(estate,pk=id)
    })
