from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('contactList', views.contact_list, name='contact_list'),
    path('edit/<int:pk>/', views.contact_edit, name='contact_edit'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),
]