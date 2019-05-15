from django.shortcuts import render, redirect
from django.http import HttpResponse
from user_role.models import UserRole
# from user_role.forms.agent_profile_form import ProfileForm
# from user_role.forms.agent_registration_form import RegistrationForm
from user.models import Profile

# Create your views here.
def index(request):
    return HttpResponse('<h1>user role</h1>')

# def view_agents(request):
#     context = {'agents': UserRole.objects.filter(role='admin')}
#     return render(request, 'agent/index.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             new_user_meta = request.POST
#             new_user = form.save()
#
#             new_profile = Profile(
#                 user=new_user,
#                 kennitala=new_user_meta['kennitala'],
#                 phone_number=new_user_meta['phone_number'],
#                 address=new_user_meta['address'],
#                 postal_code_id=new_user_meta['postal_code'],
#                 country_id=new_user_meta['country']
#             )
#
#             user_role = UserRole(
#                 role="user",
#                 user=new_user
#             )
#             user_role.save()
#
#             agent_role = UserRole(
#                 role="admin",
#                 user=new_user
#                 )
#             agent_role.save()
#
#             form = ProfileForm(request.POST, request.FILES, instance=new_profile)
#             if form.is_valid():
#                 user_profile = form.save(commit=False)
#                 user_profile.profile_image = request.FILES['profile_image']
#                 user_profile.user = request.user
#                 user_profile.save()
#         return HttpResponse('Fasteignasali skráður.')
#
#     else:
#         return render(request, 'user/register_admin.html', {
#             'form': RegistrationForm()
#         })


# def register_agent(request):
#     register(request, True)
#     return HttpResponse('<h1>Agent registered</h1>')