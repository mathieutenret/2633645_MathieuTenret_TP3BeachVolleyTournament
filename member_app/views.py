from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import View

from .forms import SignInForm, LogInForm, ForgetPasswordForm, EditUserForm

# Création de compte - vue (Point 5)
class SignInView(CreateView):
    form_class = SignInForm
    template_name = 'sign_in.html'
    success_url = reverse_lazy('login')

# Connexion - vue (Point 5)
class LogInView(LoginView):
    form_class = LogInForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

# Déconnexion - vue (Point 5)
class LogOutView(View):
    def post(self, request):
        logout(request)
        return redirect('home')


# Modification du mot de passe - vue (Point 5)
class ForgetPasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ForgetPasswordForm
    template_name = 'forget_password.html'
    success_url = reverse_lazy('password_edit_success')

# Modification du mot de passe - vue de succès (Point 5)
class PasswordChangeSuccessView(LoginRequiredMixin, View):
    template_name = 'password_edit_success.html'

    def get(self, request):
        return render(request, self.template_name)

# Modification du profil - vue (Point 5)
class EditUserView(LoginRequiredMixin, UpdateView):
    form_class = EditUserForm
    template_name = 'edit_user.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset = None):
        return self.request.user