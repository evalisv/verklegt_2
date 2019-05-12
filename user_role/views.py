from django.shortcuts import render
from django.http import HttpResponse
from user_role.models import UserRole

# Create your views here.
def index(request):
    return HttpResponse('<h1>user role</h1>')

def view_agents(request):
    context = {'agents': UserRole.objects.filter(role='admin')}
    return render(request, 'agent/index.html', context)


