from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Your existing authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Password Reset
    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]