from django.urls import path

from . import views

urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name='payment-index'),
    path('pay/offer<int:id>', views.make_payment, name='pay'),
    path('pay/offer<int:id>/review', views.get_review_info, name='review')
]