from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
    )

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),

    #for password resetting
    path('password-reset/', PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
]