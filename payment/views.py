from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from payment.forms.payment_form import PaymentForm
from estate.models import Estate
from payment.models import Payment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from offer.models import Offer
import datetime

def index(request):
    return HttpResponse('<h1>payment</h1>')

@login_required
def make_payment(request, id):
    offer = get_object_or_404(Offer, pk=id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment(received= datetime.datetime.now(), offer=offer)
            payment.save()
            return redirect('review_payment', offer.id)
        else:
            return render(request, 'payment/payment_step.html', {
                'form': PaymentForm(request.POST),
                'error_messages': form.error_messages,
                'error_class': form.error_class,
                'errors': form.errors,
            })
    else:
        return render(request, 'payment/payment_step.html', {
            'form': PaymentForm(),
            'offer': offer
            })


@login_required
def get_review_info(request, id):
    offer = get_object_or_404(Offer, pk=id)
    return render(request, 'payment/review_step.html', {
        'offer': offer
    })

@login_required
def confirmation(request, id):
    offer = get_object_or_404(Offer, pk=id)
    offer.payed = True
    offer.save()
    return render(request, 'payment/confirmation_step.html')
