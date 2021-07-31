from django.urls import path

from accounts.views import login_user, register_user, logout_user, profile_details

urlpatterns = [
    path('login/', login_user, name='user login'),
    path('register/', register_user, name='user register'),
    path('logout/', logout_user, name='user logout'),
    path('profile_details/', profile_details, name='profile details')
]
