from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login_view),
    path('logout/', views.logout_view),  # 👈 THIS IS IMPORTANT

    path('', include('tasks.urls')),
]