from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from payment.forms.payment_form import PaymentForm
from estate.models import Estate
from payment.models import Payment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse('<h1>payment</h1>')

@login_required
def make_payment(request, id):
    estate = get_object_or_404(Estate, pk=id)  #veit ekki, þarf að laga
    if request.method == 'POST':
        form = PaymentForm(request.POST) #veit ekki, þarf að laga
        if form.is_valid():
            payment = form.save(commit=False)
            payment.buyer_id = request.user
            payment.estate_id = estate
            payment.save()
            return redirect('')
    else:
        form = PaymentForm()
        return render(request, 'payment/payment_step.html', {
            'form': form,
            'id': id
        })

