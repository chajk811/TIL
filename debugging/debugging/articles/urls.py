from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/update/', views.update, name='update'),
    path('<int:article_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]
