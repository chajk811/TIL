from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('team/', views.team, name='team'),
    path('members/', views.members, name='members'),
]
