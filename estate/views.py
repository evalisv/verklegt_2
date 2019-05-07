from django.shortcuts import render, get_object_or_404
from estate.models import Estate
from estate.forms.estate_form import RegisterEstateForm
# Create your views here.


def index(request):
    context = {"estates": Estate.objects.all().order_by('address')}
    return render(request, "estate/index.html", context)

def get_estate_by_id(request, id):
    return render(request, 'estate/estate_details.html', {
      'estate' : get_object_or_404(Estate, pk=id)
    })

def register_estate(request):
    if request.method == 'POST':
        print(1)
    else:
        form = RegisterEstateForm()
    return render(request, 'estate/register_estate.html', {
        'form' : form
    })
