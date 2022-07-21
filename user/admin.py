from dataclasses import fields
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserDadosCreateForm, CustomUserDadosChangeForm
from .models import UserDados

@admin.register(UserDados)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserDadosCreateForm
    form = CustomUserDadosChangeForm
    model = UserDados
    list_display = ('luser', 'email', 'suser', 'cpf', 'pis','pais', 
                    'estado', 'municipio', 'cep', 'rua', 'numero', 'complemento')
    fieldsets = (
        (None, {'fields': ('email', 'password'),}),
        ('Informações Pessoais', {'fields': ('luser', 'suser', 'cpf', 'pis','pais',
                                             'estado','municipio','cep','rua','numero','complemento')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login','date_joined')}),
    )
    
