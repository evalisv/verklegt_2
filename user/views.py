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
def update_name(request):
    instance = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':
        form = UpdateNameForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateNameForm(instance=instance)
        return render(request, 'user/update_name.html', {
            'form': form
        })

@login_required
def update_profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.profile_image = request.FILES['profile_image']
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile')
    return render(request, 'user/update_profile.html', {
        'form': ProfileForm(instance=user_profile),
        'readOnlyData': request.user,
        'error_messages': ProfileForm(request.POST, request.FILES, instance=user_profile).errors
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
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
                profile_image=request.FILES['profile_image']
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
    context = {
        'users': User.objects.filter(userrole__role='admin')
    }
    return render(request, 'agent/index.html', context)

@login_required
def register_agent(request):
    if request.method == 'POST':
        agent_form = AgentRegistrationForm(request.POST, request.FILES)
        if agent_form.is_valid():
            new_user_meta = request.POST
            new_user = agent_form.save()

            new_profile = Profile(
                user=new_user,
                kennitala=new_user_meta['kennitala'],
                phone_number=new_user_meta['phone_number'],
                address=new_user_meta['address'],
                postal_code_id=new_user_meta['postal_code'],
                country_id=new_user_meta['country'],
                profile_image=request.FILES['profile_image']
            )
            new_profile.save()

            user_role = UserRole(
                role='admin',
                user=new_user
            )
            user_role.save()

            return redirect('agent-index')
        else:
            return render(request, 'user/register_admin.html', {
                'form': AgentRegistrationForm(request.POST)
            })
    else:
        return render(request, 'user/register_admin.html', {
            'form': AgentRegistrationForm()
        })


@login_required
def my_offers(request):
    offer_list = Offer.objects.all().order_by("offer_made")
    user_role = request.user.userrole.role

    no_received_offers = True
    no_made_offers = True

    for offer in offer_list:
        if offer.estate.estate_seller == request.user:
            no_received_offers = False
            break

    for offer in offer_list:
        if offer.offer_maker == request.user:
            no_made_offers = False
            break

    context = {
        'offers': offer_list,
        'no_made_offers': no_made_offers,
        'no_received_offers': no_received_offers,
        'user_role': user_role
    }
    return render(request, "offer/offer_list.html", context)

def approve_offer(request, id):
    offer = get_object_or_404(Offer, pk=id)
    offer.status = 'Approved'
    offer.save()
    return redirect('my_offers')

def reject_offer(request, id):
    offer = get_object_or_404(Offer, pk=id)
    offer.status = 'Rejected'
    offer.save()
    return redirect('my_offers')

def accept_offer(request,id):
    offer = get_object_or_404(Offer, pk=id)
    offer.status = 'Accepted'
    offer.save()
    return redirect('my_offers')

@login_required
def profile(request):
    number_of_columns = 6

    if request.user.userrole.role == 'admin':
        number_of_columns = 4

    return render(request, 'user/profile.html', {
        'user': request.user,
        'user_role': request.user.userrole.role,
        'number_of_cols': number_of_columns
    })


def user_settings(request):
    return render(request, 'user/settings.html')