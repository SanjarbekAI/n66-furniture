from django.urls import path

from apps.accounts.views import UserLoginView, UserRegisterView, UserResetPasswordView, UserAccountView

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('reset-password/', UserResetPasswordView.as_view(), name='reset-password'),
    path('account/', UserAccountView.as_view(), name='user-account'),
]
