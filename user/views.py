from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile_form import ProfileForm
from user.forms.registration_form import RegistrationForm
from user.forms.agent_registration_form import AgentRegistrationForm
from user.forms.profile_form import UpdateNameForm, PasswordForm
from user.models import Profile
from estate.models import Estate
from user_role.models import UserRole
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from offer.models import Offer
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator


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
    next_page = request.GET.get('next', False)
    user_profile = Profile.objects.filter(user=request.user).first()
    file = request.FILES.get('profile_image', user_profile.profile_image)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.profile_image = file
            user_profile.user = request.user
            user_profile.save()
            if next_page:
                return redirect(next_page)
            return redirect('profile')
    return render(request, 'user/update_profile.html', {
        'form': ProfileForm(instance=user_profile),
        'readOnlyData': request.user,
        'error_messages': ProfileForm(request.POST, request.FILES, instance=user_profile).errors
    })


def register(request):
    file = request.FILES.get('profile_image', '')
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
                profile_image=file
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


@login_required
def view_agents(request):
    context = {}
    if request.user.userrole.role == 'admin':
        user_list = User.objects.filter(userrole__role='admin').order_by('first_name')
        paginator = Paginator(user_list, 20)

        page = request.GET.get("page")
        users = paginator.get_page(page)

        context['users'] = users
        context['is_admin'] = True
    else:
        context['is_admin'] = False
    return render(request, 'user/admin_index.html', context)


@login_required
def view_user(request):
    context = {}
    if request.user.userrole.role == 'admin':
        user_list = User.objects.filter(userrole__role='user').order_by('first_name')
        paginator = Paginator(user_list, 20)

        page = request.GET.get("page")
        users = paginator.get_page(page)

        context['users'] = users
        context['is_admin'] = True
    else:
        context['is_admin'] = False
    return render(request, 'user/user_index.html', context)


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
    offer_list = Offer.objects.all().order_by('-offer_made')
    user_role = request.user.userrole.role

    no_received_offers = True
    no_made_offers = True

    for offer in offer_list:
        if offer.estate.estate_seller == request.user and offer.status != 'Incoming':
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
    return render(request, 'offer/offer_list.html', context)


@login_required
def approve_offer(request, id):
    offer = get_object_or_404(Offer, pk=id)
    offer.status = 'Approved'
    offer.save()
    return redirect('my_offers')


@login_required
def reject_offer(request, id):
    offer = get_object_or_404(Offer, pk=id)
    offer.status = 'Rejected'
    offer.save()
    return redirect('my_offers')


@login_required
def accept_offer(request,id):
    offer = get_object_or_404(Offer, pk=id)
    offer.status = 'Accepted'
    offer.save()
    estate = get_object_or_404(Estate, pk=offer.estate.id)
    estate.on_sale = False
    estate.save()
    other_offers = Offer.objects.filter(estate=estate)
    for item in other_offers:
        if item != offer:
            item.status = 'Rejected'
            item.save()
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


@login_required
def user_settings(request):
    return render(request, 'user/settings.html')


@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordForm(user=request.user)
        return render(request, 'user/update_password.html', {
            'form': form,
            'readOnlyData': request.user,
        })














