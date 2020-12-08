from django.urls import path

from smart_socket_app.views.about_ss import about_ss
from smart_socket_app.views.contact_us import contact_us
from smart_socket_app.views.edit_delete_ss import edit_ss
from smart_socket_app.views.index import index
from smart_socket_app.views.add_ss import add_ss
from smart_socket_app.views.set_up_instructions import set_up_instructions
from smart_socket_app.views.ss_description import ss_description

urlpatterns = (
    path('', index, name='index'),
    path('<str:socket_name>=<str:cmd>', index, name='cmd'),
    path('contact/', contact_us, name='contact us'),
    path('about_smart_sockets/', about_ss, name='about ss'),
    path('set_up_instructions/', set_up_instructions, name='set up instructions'),
    path('add_smart_socket/', add_ss, name='add smart socket'),
    path('smart_socket_description/<int:pk>/', ss_description, name='ss description'),
    path('smart_socket_edit/<int:pk>/', edit_ss, name='edit ss'),
    path('smart_socket_edit/<str:action>=<int:pk>/', edit_ss, name='delete ss'),
)
