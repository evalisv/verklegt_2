from django.shortcuts import render
from vhistory.models import Vhistory
from django.utils import timezone

def index(request):
    context = {'estate': estate}
    return render('vhistory/index.html', context)

def update_vhistory(user, estate):
    today = timezone.now()
    for viewed_estate in Vhistory.objects.all():
        if user.id == viewed_estate.user_id:
            if estate.id == viewed_estate.estate_id:
                viewed_estate.view_date = today
                viewed_estate.save()
                return
    entry = Vhistory(user=user, estate=estate, view_date=today)
    entry.save()

def get_vhistory_by_user(user):
    return Vhistory.objects.filter(user_id=user.id).order_by('-view_date')

##To test in Python console:
#view_history = get_vhistory_by_user(user)
#for item in view_history:
#    print(item.estate_id)

#for entry in view_history:
#    print(Estate.objects.filter(id=entry.estate_id))

#To clear Vhistory:
#Vhistory.objects.all().delete

#Þessa skipun á eftir að laga til:
def get_vhistory(request):
    return render(Vhistory.objects.all().order_by('-date'), 'vhistory/index.html',{
        'estate': get_object_or_404(estate,pk=id)
    })
