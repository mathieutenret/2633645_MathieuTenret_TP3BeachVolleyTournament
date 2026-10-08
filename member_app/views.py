from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import View

from .forms import SignInForm, LogInForm, ForgetPasswordForm, EditUserForm

class SignInView(CreateView):
    form_class = SignInForm
    template_name = 'sign_in.html'
    success_url = reverse_lazy('index')

class LogInView(LoginView):
    form_class = LogInForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

class ForgetPasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = ForgetPasswordForm
    template_name = 'forget_password.html'
    success_url = reverse_lazy('password_edit_success')

class PasswordChangeSuccessView(LoginRequiredMixin, View):
    template_name = 'password_edit_success.html'

    def get(self, request):
        return render(request, self.template_name)

class EditUserView(LoginRequiredMixin, UpdateView):
    form_class = EditUserForm
    template_name = 'edit_user.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset = None):
        return self.request.user