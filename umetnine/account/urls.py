from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('profile', views.profile_view, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout, name='logout'),
    path('list/', views.user_list, name='user_list'),
]
