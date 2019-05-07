from django.shortcuts import render, get_object_or_404
from estate.models import Estate
# Create your views here.

estates = [
    {
        "name": "Björgvinsbraut 70",
        "price": 69900000
    },
    {
        "name": "Arnarsmári 2",
        "price": 15900000
    }
]

def index(request):
    context = {"estates": estates}
    return render(request, "estate/index.html", context)

def get_estate_by_id(request, id):
    return render(request, 'estate/estate_details.html', {
      'estate' : get_object_or_404(Estate, pk=id)
    })