from django.urls import path

from accounts.views import login_user, register_user, logout_user, profile_details, edit_profile, delete_account

urlpatterns = [
    path('login/', login_user, name='user login'),
    path('register/', register_user, name='user register'),
    path('logout/', logout_user, name='user logout'),
    path('profile_details/<int:pk>', profile_details, name='profile details'),
    path('edit_profile/<int:pk>', edit_profile, name='edit profile'),
    path('delete_account/<int:pk>', delete_account, name='delete account')
]
