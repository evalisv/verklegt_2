from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from user.models import User, UserImage
from user.forms.profile_form import UserUpdateForm

# Create your views here.
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
