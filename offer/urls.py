from django.urls import path

from . import views

urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name="offer-index"),
    path('make_offer/<int:id>', views.make_offer, name="make_offer")
]