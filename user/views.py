from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile_form import ProfileForm
from user.forms.registration_form import RegistrationForm
from user.forms.profile_form import UpdateNameForm
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from offer.models import Offer


def index(request):
    return render(request, 'user/index.html')

@login_required
def update_name(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UpdateNameForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('user-index')
    else:
        form = UpdateNameForm(instance=instance)
        return render(request, 'user/update_name.html', {
            'form': form,
            'id': id
        })

@login_required
def update_profile(request, id):
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('user-index')
    return render(request, 'user/update_profile.html', {
        'form': ProfileForm(instance=user_profile)
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-index')
    return render(request, 'user/register.html', {
        'form': RegistrationForm()
    })

#þetta fall er ekki notað til þess að uppfæra profile upplýsingar, heldur má þetta vera fallið sem opnar "Mínar síður"
@login_required
def profile(request):
    pass

@login_required
def my_offers(request):
    offer_list = Offer.objects.all().order_by("offer_made")
    context = {"offers": offer_list}
    return render(request, "offer/offer_list.html", context)
