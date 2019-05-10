from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile_form import ProfileForm
from user.forms.registration_form import RegistrationForm
from user.forms.profile_form import UpdateNameForm
from user.models import Profile
from django.contrib.auth.models import User


def index(request):
    return render(request, 'user/index.html')


def update_user(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UpdateNameForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            #{return redirect('profile.html', id=id)
    else:
        form = UpdateNameForm(instance=instance)
        return render(request, 'user/update_user.html', {
            'form': form,
            'id': id


        })

def update_profile(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile.html', id=id)
    else:
        form = ProfileForm(instance=instance)
        return render(request, 'user/update_profile.html', {
            'form': form,
            'id': id

        })



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': RegistrationForm()
    })


def profile(request, id):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            #tengja foreign key við innskráðan notanda
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })
