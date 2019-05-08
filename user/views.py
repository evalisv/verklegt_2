from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from user.models import User, UserImage
from user.forms.profile_form import UserUpdateForm
from user.classes.UserCreateForm import UserCreateForm
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm

def index(request):
    return render(request, 'user/index.html')


def update_user(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            #{return redirect('profile.html', id=id)
    else:
        form = UserUpdateForm(instance=instance)
        return render(request, 'user/update_user.html', {
            'form': form,
            'id': id
        })

def register(request):
    if 'POST' == request.method:
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreateForm()
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

