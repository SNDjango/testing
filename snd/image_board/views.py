from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def login(request):
    if(request.method == 'POST'):
        user = request.POST['user']
        pwd = request.POST['pwd']

        user = authenticate(username=user, password=pwd)
        if user is not None:
            login(request, user)
            return redirect(index)


    else:
        return render(request, 'login.html')
