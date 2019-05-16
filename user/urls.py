from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views
from searches import views as searchviews
from vhistory import views as vhistoryviews
from estate import views as estateviews
from payment import views as paymentviews



urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name='user-index'),
    path('index', views.view_user, name='user-index'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', views.register, name='register'),
    path('register_estate', estateviews.register_estate, name='register_estate'),
    path('profile/', views.profile, name='profile'),
    path('profile/history/', searchviews.search_history, name='search_history'),
    path('profile/history/viewing_history', vhistoryviews.get_vhistory_by_user, name='viewing_history'),
    path('profile/history/search_history', searchviews.view_search_words, name='search_word_history'),
    path('profile/settings', views.user_settings, name='settings'), #TODO: búa til settings sídu
    path('profile/settings/update_profile', views.update_profile, name='update_profile'),
    path('profile/settings/update_name', views.update_name, name='update_name'),
    path('profile/settings/update_password', views.update_password, name='update_password'),
    path('profile/my_estates/', estateviews.seller_index, name='seller_estates'),
    path('profile/my_estates/delete_estate/<int:id>', estateviews.delete_estate, name='delete_estate'),
    path('profile/my_estates/update_estate/<int:id>', estateviews.update_estate, name='update_estate'),
    path('profile/my_offers', views.my_offers, name='my_offers'),
    path('profile/my_offers/approve<int:id>', views.approve_offer, name='approve_offer'),
    path('profile/my_offers/reject<int:id>', views.reject_offer, name='reject_offer'),
    path('profile/my_offers/accept<int:id>', views.accept_offer, name='accept_offer'),
    path('profile/my_offers/pay<int:id>', paymentviews.make_payment, name='make_payment'),
    path('profile/my_offers/pay<int:id>/review', paymentviews.get_review_info, name='review_payment'),
    path('profile/my_offers/pay<int:id>/review/confirmation', paymentviews.confirmation, name='confirmation'),
    path('profile/agents/', views.view_agents, name='agent-index'),
    path('profile/agents/register_agent/', views.register_agent, name='register_agent'),
    path('profile/agents/delete_agent/<int:id>', views.delete_agent, name='delete_agent')

]


# path('update_profile/<int:gid>', views.update_profile, name='update_profile'),