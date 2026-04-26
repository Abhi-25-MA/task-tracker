from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.toggle_complete, name='toggle_complete'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('signup/', views.signup_view, name='signup'),
]