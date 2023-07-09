from . import views
from django.urls import path


app_name = "users"

urlpatterns = [
    path(
        'register/',
        views.RegisterView.as_view(),
        name='register'
    ),
    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        'password-reset/',
        views.PasswordResetCustomView.as_view(),
        name="password_reset"
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>',
        views.PasswordResetConfirmCustomView.as_view(
            template_name='users/password_reset_confirm.html'),
        name="password_reset_confirm"
    ),
]
