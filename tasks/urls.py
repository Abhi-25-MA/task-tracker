from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_task),
    path('delete/<int:id>/', views.delete_task),
    path('complete/<int:id>/', views.toggle_complete),
    path('edit/<int:id>/', views.edit_task),

    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
]