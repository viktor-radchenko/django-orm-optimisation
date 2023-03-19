from django.urls import path, include

from app import views

app_name = "app"

urlpatterns = [
    path("", include('app.urls.index')),
    path("auth/", include('app.urls.auth')),
]
