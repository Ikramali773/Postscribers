from django.urls import path
from .import views 
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup/', views.sign_up, name='users-signup'),
    path('profile/',views.profile, name='users-profile'),
    path('login/', views.login_view, name='users-login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'),name='users-logout'),
    path('otp/', views.otp, name='otp'),
    path('resend/', views.resend_otp, name='resend')
]
 