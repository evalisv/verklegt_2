from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from offer import views as offerviews


urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name="user-index"),
    path('update_name/<int:id>', views.update_name, name="update_name"),
    path('update_profile/<int:id>', views.update_profile, name="update_profile"),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    #path('make_offer/<int:id>', offerviews.make_offer, name='make_offer')
]