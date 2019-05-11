from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from offer.forms.offer_forms import MakeOfferForm
from estate.models import Estate
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return HttpResponse('<h1>offer</h1>')

@login_required
def make_offer(request, id):
    estate = get_object_or_404(Estate, pk=id)
    if request.method == 'POST':
        form =  MakeOfferForm(data=request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.offer_maker = request.user
            offer.estate = estate
            offer.save()
            return redirect('my_offers')
    else:
        form = MakeOfferForm()
    return render(request, 'offer/make_offer.html',{
        'form': form,
        'id': id
    })
