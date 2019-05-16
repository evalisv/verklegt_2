from django.urls import path, re_path
from offer import views as offerviews
from . import views

urlpatterns = [
    path('', views.index, name='estate-index'),
    path('<int:id>/', views.get_estate_by_id, name='estate_details'),
    path('<int:id>/make_offer/', offerviews.make_offer, name='make_offer'),
    re_path(r'^sort$', views.sort_estates, name='sort_estates')
]