from django.urls import path, re_path
from offer import views as offerviews
from . import views

urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name="estate-index"),
    path('<int:id>/', views.get_estate_by_id, name="estate_details"),
    path('<int:id>/make_offer/', offerviews.make_offer, name="make_offer"),
    #path('register_estate', views.register_estate, name="register_estate"),
    #path('delete_estate/<int:id>', views.delete_estate, name="delete_estate"),
    #path('update_estate/<int:id>', views.update_estate, name="update_estate"),
    re_path(r'^sort$', views.sort_estates, name="sort_estates")
    #path('my_estates/<int:id>', views.seller_index, name="seller_estate")
]