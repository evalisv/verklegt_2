from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    # path('viewing_history', views.get_vhistory_by_user, name='viewing_history')
    # path('vhistory/', include('vhistory.urls')),
]