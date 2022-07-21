from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import UserDados
from .forms import *

from rest_framework import generics
from .serializers import UserDadosSerializer
from rest_framework import viewsets

class UserCreate(CreateView):
    model = UserDados
    form_class = CustomUserDadosCreateForm
    template_name = 'cadastros/adicionar.html'
    success_url = reverse_lazy('index')
    
class UserUpdate(UpdateView):
    model = UserDados
    form_class = CustomUserDadosChangeForm
    template_name = 'cadastros/atualizar.html'
    success_url = reverse_lazy('index')

class UserDelete(DeleteView):
    model = UserDados
    template_name = 'cadastros/excluir.html'
    success_url = reverse_lazy('index')
    

class UserDadosViewSet(viewsets.ModelViewSet):
    queryset = UserDados.objects.all()
    serializer_class = UserDadosSerializer