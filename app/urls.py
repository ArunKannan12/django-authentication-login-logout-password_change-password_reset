from . import views
from .views import home
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import *

urlpatterns = [
    path("",views.loginpage,name="loginpage"),
    path("signinpage/", views.signinpage, name="signinpage"),
    path("logoutpage/", views.logoutpage, name="logoutpage"),
    path("home",views.home,name="home"),

    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html',form_class=changepassword,success_url='password_change_done'),name='password_change'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html',form_class=UserPasswordResetForm),name='password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html', form_class=UserSetPasswordForm),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_complete'),
]
