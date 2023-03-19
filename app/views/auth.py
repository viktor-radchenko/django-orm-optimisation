from django.http import HttpResponse
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, 'app/auth/login.html')
    else:
        username = request.POST.get('username', '').lower()
        password = request.POST.get('password', '')
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect(reverse('app:index'))
        else:
            return HttpResponse("Dude, yuo are messed yp!")


@require_http_methods(["GET"])
def logout(request):
    auth.logout(request)
    return redirect(reverse('app:index'))


@require_http_methods(["GET", "POST"])
def sign_up(request):
    if request.method == "GET":
        return HttpResponse("Seems like you are trying to create an account")
    else:
        return HttpResponse("You created an account, but I don't like you any more")


@require_http_methods(["GET", "POST"])
def forgot_password(request):
    if request.method == "GET":
        return HttpResponse("Seems like you are trying to restore password")
    else:
        return HttpResponse("You restored password, but I don't like you any more")
