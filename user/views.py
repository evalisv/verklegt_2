from user.classes.UserCreateForm import UserCreateForm
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'user/index.html')


#setti tímabundið inn UserCreationForm
def register(request):
    if 'POST' == request.method:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
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
