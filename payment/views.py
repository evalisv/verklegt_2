from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from payment.forms.payment_form import PaymentForm
from payment.models import Payment
from django.contrib.auth.decorators import login_required
from offer.models import Offer
import datetime


@login_required
def make_payment(request, id):
    offer = get_object_or_404(Offer, pk=id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            return redirect('review_payment', offer.id)
    else:
        form = PaymentForm()
    return render(request, 'payment/payment_step.html', {
        'form': form,
        'offer': offer
    })

@login_required
def get_review_info(request, id):
    offer = get_object_or_404(Offer, pk=id)
    return render(request, 'payment/review_step.html', {
        'offer': offer,
    })

@login_required
def confirmation(request, id):
    offer = get_object_or_404(Offer, pk=id)
    already_payed = False
    if len(Payment.objects.filter(offer_id=id)) == 0:
        offer.payed = True
        offer.save()
        payment = Payment(received=datetime.datetime.now(), offer=offer)
        payment.save()
    else:
        already_payed = True
    return render(request, 'payment/confirmation_step.html', {
        'offer': offer,
        'already_payed': already_payed
    })
