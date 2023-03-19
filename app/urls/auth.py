from django.urls import path

from app import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
]
