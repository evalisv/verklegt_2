from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from payment.forms.payment_form import PaymentForm
from estate.models import Estate
from payment.models import Payment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from offer.models import Offer

def index(request):
    return HttpResponse('<h1>payment</h1>')

@login_required
def make_payment(request, id):
    offer = get_object_or_404(Offer, pk=id)
    if request.method == 'POST':
        form = PaymentForm(data=request.POST, instance=offer)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.amount = offer.amount
            payment.save()
            #return redirect('review_step.html url')
    else:
        form = PaymentForm()
        return render(request, 'payment/payment_step.html', {
            'form': form,
            'offer': offer
        })

def get_review_info(request, id):
    offer = get_object_or_404(Offer, pk=id)
    return render(request, 'payment/review_step.html', {
        'offer': offer
    })
