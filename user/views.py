from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile_form import ProfileForm
from user.forms.registration_form import RegistrationForm
from user.forms.profile_form import UpdateNameForm
from user.models import Profile
from user_role.models import UserRole
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
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.profile_image = request.FILES['profile_image']
            user_profile.user = request.user
            user_profile.save()
            return redirect('user-index')
    return render(request, 'user/update_profile.html', {
        'form': ProfileForm(instance=user_profile),
        'readOnlyData': request.user,
        'error_messages': ProfileForm(request.POST, request.FILES, instance=user_profile).errors
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user_meta = request.POST
            new_user = form.save()

            new_profile = Profile(
                user=new_user,
                kennitala=new_user_meta['kennitala'],
                phone_number=new_user_meta['phone_number'],
                address=new_user_meta['address'],
                postal_code_id=new_user_meta['postal_code'],
                country_id=new_user_meta['country']
            )
            new_profile.save()

            user_role = UserRole(
                role="user",
                user=new_user
            )
            user_role.save()
            return redirect('login')
        else:
            return render(request, 'user/register.html', {
                'form': RegistrationForm(request.POST),
                'error_messages': form.error_messages,
                'error_class': form.error_class,
                'errors': form.errors
            })
    else:
        return render(request, 'user/register.html', {
            'form': RegistrationForm()
        })

#þetta fall er ekki notað til þess að uppfæra profile upplýsingar, heldur má þetta vera fallið sem opnar "Mínar síður"

@login_required
def my_offers(request):
    offer_list = Offer.objects.all().order_by("-offer_made")
    context = {"offers": offer_list}
    return render(request, "offer/offer_list.html", context)

@login_required
def profile(request, id):
    user_roles_set = UserRole.objects.filter(user_id=request.user.id)
    user_roles = list(user_roles_set.values_list('role', flat=True))
    is_admin = False
    number_of_columns = 6
    try:
        if user_roles.index('admin'):
            is_admin = True
            number_of_columns = 4
    except:
        pass
    return render(request,'user/profile.html', {
        'user': request.user,
        'is_admin': is_admin,
        'number_of_cols': number_of_columns
    })

