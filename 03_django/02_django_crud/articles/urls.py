from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'), # NEW(GET) + CREATE(POST)
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'), # EDIT(GET) + UPDATE(POST)
]