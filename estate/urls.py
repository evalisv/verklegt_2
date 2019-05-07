from django.urls import path

from . import views

urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name="estate-index"),
    path('<int:id>', views.get_estate_by_id)
]