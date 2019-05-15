from django.urls import path

from . import views

urlpatterns = [
    # url, fall sem á að keyrast þegar farið er á urlið, nafn á fallinu
    path('', views.index, name='userrole-index'),
    path('index/', views.view_agents, name='userrole-index'),
    path('index/register_agent/', views.register, name='register_agent'),

]
# TODO: fix after functionality is finished,