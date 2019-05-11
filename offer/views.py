from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from offer.forms.offer_forms import MakeOfferForm
from estate.models import Estate

# Create your views here.
def index(request):
    return HttpResponse('<h1>offer</h1>')

def make_offer(request, id):
    estate = get_object_or_404(Estate, pk=id)

    if request.method == 'POST':
        form =  MakeOfferForm(data=request.POST)
        if form.is_valid():
            offer = form.save(commit=False)

    else:
        print(2)
    return render(request, 'form/make_offer.html',{
        'form': form
    })
