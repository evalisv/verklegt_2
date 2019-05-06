from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
@login_required
def index(request):
    context = {"estates": estates}
    return render(request, "estate/index.html", context)
