from django.shortcuts import render
from django.http import HttpResponse
from estate.models import Municipality, Estate
# Create your views here.
def index(request):
    return HttpResponse("Hello from index function in main")

def homepage(request):
    context = {'postal_codes': Municipality.objects.all(),
               'estates': Estate.objects.order_by('-date_listed')[:6]}
    return render(request, "home.html", context)