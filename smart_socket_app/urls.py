from django.urls import path

from smart_socket_app.views.about_ss import about_ss
from smart_socket_app.views.contact_us import contact_us
from smart_socket_app.views.index import index
from smart_socket_app.views.add_ss import add_ss

urlpatterns = (
    path('', index, name='index'),
    path('contact/', contact_us, name='contact us'),
    path('about_smart_sockets/', about_ss, name='about ss'),
    path('add_smart_socket/', add_ss, name='add smart socket'),
)
