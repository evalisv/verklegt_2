from django.urls import path

from . import views

urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name='payment-index'),
    path('make_payment/<int:id>', views.make_payment, name='make_payment')
]