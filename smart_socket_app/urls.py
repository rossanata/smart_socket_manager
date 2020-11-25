from django.urls import path
from smart_socket_app.views.index import index
from smart_socket_app.views.profiles import home, create_profile

urlpatterns = (
    path('', index, name='index'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/home/', home, name='home'),
)
