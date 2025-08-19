from django.views.generic import TemplateView


class UserLoginView(TemplateView):
    template_name = 'auth/user-login.html'


class UserRegisterView(TemplateView):
    template_name = 'auth/user-register.html'


class UserResetPasswordView(TemplateView):
    template_name = 'auth/user-reset-password.html'


class UserAccountView(TemplateView):
    template_name = 'auth/user-acount.html'
