from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.SignInView.as_view(), name='sign_in'),
    path('edit/', views.EditUserView.as_view(), name='edit_user'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('password/', views.ForgetPasswordView.as_view(), name="forget_password"),
    path('password-success/', views.PasswordChangeSuccessView.as_view(), name='password_edit_success'),
]