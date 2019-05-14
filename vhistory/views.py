from django.shortcuts import render, redirect, get_object_or_404
from estate.models import Estate
from vhistory.models import Vhistory
from django.utils import timezone

def index(request, id):
    filtered_vhistory = Vhistory.objects.values('estate_id').filter(user_id=request.user.id).order_by('-view_date')
    list_of_viewed = []
    for item in filtered_vhistory:
        list_of_viewed.append(get_object_or_404(Estate, id=item['estate_id']))
    context = {'estates': list_of_viewed}

    return render(request, 'vhistory/index.html', context)


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

#def get_vhistory_by_user(user):
    #return Vhistory.objects.filter(user_id=user.id).order_by('-view_date')


def get_vhistory_by_user(request, id):
    filtered_vhistory = Vhistory.objects.values('estate_id').filter(user_id=request.user.id).order_by('-view_date')
    list_of_viewed = []
    for item in filtered_vhistory:
        list_of_viewed.append(get_object_or_404(Estate, id=item['estate_id']))
    context = {'estates': list_of_viewed}

    return render(request, 'vhistory/index.html', context)


##To test in Python console:
#view_history = get_vhistory_by_user(user)
#for item in view_history:
#    print(item.estate_id)

#for entry in view_history:
#    print(Estate.objects.filter(id=entry.estate_id))

#user_list = []
#estate_list = []
#for user in User.objects.all():
#    user_list.append(user)
#for estate in Estate.objects.all():
#    estate_list.append(estate)
#update_vhistory(user2,estate2)
#for entry in view_history:
#    print(Estate.objects.filter(id=entry.estate_id))


#To clear Vhistory:
#Vhistory.objects.all().delete

