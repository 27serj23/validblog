from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='list'),
    path('post/<int:pk>/', views.post_detail, name='detail'),
    path('post/create/', views.post_create, name='create'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('comment/<int:pk>/delete/', views.delete_comment, name="delete_comment"),
    path('post/<int:pk>/comment/add/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
]