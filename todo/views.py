from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login_view(request):
    if request.GET:
        pass
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,
                                 password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
        return redirect(reverse('todo:index'))
    return render(request, 'templates/registration/login.html')


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/account/loggedout")
