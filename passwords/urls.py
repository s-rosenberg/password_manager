from django.urls import path, include

from . import views

app_name = 'passwords'
urlpatterns = [
    path('save_password/', views.save_password, name='save_password'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register_user, name='register'),
    path('saved_passwords/', views.get_saved_passwords, name='saved_passwords'),
    path('logout/', views.logout_view, name='logout')
]