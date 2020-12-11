from django.urls import path

from ssm_auth.views import login_user, logout_user, register_user, edit_delete_user

urlpatterns = (
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register_user/', register_user, name='register user'),
    path('edit_user/<int:pk>/', edit_delete_user, name='edit user'),
    path('delete_edit/<str:action>=<int:pk>/', edit_delete_user, name='delete user'),
)
