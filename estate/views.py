from django.shortcuts import render
from estate.models import Estate
# Create your views here.


def index(request):
    context = {"estates": Estate.objects.all().order_by('address')}
    return render(request, "estate/index.html", context)
