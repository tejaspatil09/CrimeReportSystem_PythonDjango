from django.urls import  path
from .views import *
from django.contrib.auth.views import LogoutView,PasswordChangeView ,PasswordChangeDoneView
from .forms import ChangePasswordForm
urlpatterns =[
    path('',home , name='home'),
    path('signup/',SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page = '/login/'),name='logout'),
    path('change-password/',PasswordChangeView.as_view(template_name="core/change-password.html",form_class =ChangePasswordForm),name='change-password'),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name="core/change-password-done.html"),name="password_change_done"),
    path('addcomplaint/',Addcomplaint.as_view(),name='addcomplaint'),
    path('adminlogin/',AdminloginView.as_view(),name='adminlogin'),
    path('viewcomplaint/',Viewcomplaint.as_view(),name='viewcomplaint')
 ]
