from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path
from . import views
from estate import views as estateviews


urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name="user-index"),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', views.register, name='register'),
    path('register_estate', estateviews.register_estate, name="register_estate"),
    path('profile/', views.profile, name='profile'),
    path('profile/update', views.update_profile, name="update_profile"),
    path('profile/my_estates/', estateviews.seller_index, name="seller_estate"),
    path('profile/my_estates/delete_estate/<int:id>', estateviews.delete_estate, name="delete_estate"),
    path('profile/my_estates/update_estate/<int:id>', estateviews.update_estate, name="update_estate"),
    path('profile/my_offers', views.my_offers, name='my_offers'),
    path('profile/update_name/<int:id>', views.update_name, name="update_name"),
    # path('<int:id>/update', views.update_profile, name="update_profile"
]

# path('update_profile/<int:gid>', views.update_profile, name="update_profile"),