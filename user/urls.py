from django.urls import path

from . import views

urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name="user-index"),
    path('update_user/<int:id>', views.update_user, name="update_user")
]