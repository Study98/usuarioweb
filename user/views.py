from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserDados
from .forms import *

class UserCreate(CreateView):
    model = UserDados
    #fields = ('email','password','luser')
    form_class = CustomUserDadosCreateForm
    template_name = 'cadastros/adicionar.html'
    success_url = reverse_lazy('index')
    
class UserUpdate(UpdateView):
    model = UserDados
    #fields = ('email','password','luser')
    form_class = CustomUserDadosChangeForm
    template_name = 'cadastros/adicionar.html'
    success_url = reverse_lazy('index')
