from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    # path('search_history', views.view_search_words, name="user_search_words"),
    # path('search_history', views.search_history, name='search_history')
]