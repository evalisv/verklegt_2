from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile_form import ProfileForm
from user.forms.registration_form import RegistrationForm
from user.forms.agent_registration_form import AgentRegistrationForm
from user.forms.profile_form import UpdateNameForm
from user.models import Profile
from user_role.models import UserRole
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from offer.models import Offer
from django.http import HttpResponse


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

def view_agents(request):
    context = {'agents': UserRole.objects.filter(role='admin')}
    return render(request, 'agent/index.html', context)


def register_agent(request):
    if request.method == 'POST':
        form = AgentRegistrationForm(request.POST)
        if form.is_valid():
            new_user_meta = request.POST
            new_user = form.save()

            new_profile = Profile(
                user=new_user,
                kennitala=new_user_meta['kennitala'],
                phone_number=new_user_meta['phone_number'],
                address=new_user_meta['address'],
                postal_code_id=new_user_meta['postal_code'],
                country_id=new_user_meta['country'],
                profile_image=new_user_meta['profile_image']
            )
            new_profile.save()

            user_role = UserRole(
                role="user",
                user=new_user
            )
            user_role.save()

            agent_role = UserRole(
                role="admin",
                user=new_user
                )
            agent_role.save()

        return HttpResponse('Fasteignasali skráður.')

    else:
        return render(request, 'user/register_admin.html', {
            'form': AgentRegistrationForm()
        })


#þetta fall er ekki notað til þess að uppfæra profile upplýsingar, heldur má þetta vera fallið sem opnar "Mínar síður"

@login_required
def my_offers(request):
    user_roles_set = UserRole.objects.filter(user_id=request.user.id)
    user_roles = list(user_roles_set.values_list('role', flat=True))
    is_admin = False
    try:
        if user_roles.index('admin'):
            is_admin = True
    except:
        pass
    offer_list = Offer.objects.all().order_by("-offer_made")
    no_received_offers = True
    no_made_offers = True
    if request.user.id in list(offer_list.values_list('offer_maker', flat=True)):
        no_made_offers = False

    if request.user.id in list(request.user.estate_set.values_list('estate_seller_id', flat=True)):
        no_received_offers = False

    # if request.user.id in list(offer_list.values_list('estate', flat=True)):
    #     no_received_offers = False

    context = {
        'offers': offer_list,
        'is_admin': is_admin,
        'no_made_offers': no_made_offers,
        'no_received_offers': no_received_offers
    }
    return render(request, "offer/offer_list.html", context)


@login_required
def profile(request):
    user_roles_set = UserRole.objects.filter(user_id=request.user.id)
    user_roles = list(user_roles_set.values_list('role', flat=True))
    is_admin = False
    number_of_columns = 6

    if 'admin' in user_roles:
        is_admin = True
        number_of_columns = 4
        print('if')
    # try:
    #     if user_roles.index('admin'):
    #         is_admin = True
    #         number_of_columns = 4
    # except:
    #     pass

    print(is_admin, request.user.id)
    return render(request,'user/profile.html', {
        'user': request.user,
        'is_admin': is_admin,
        'number_of_cols': number_of_columns
    })
