from dataclasses import fields
from rest_framework import serializers

from .models import UserDados

class UserDadosSerializer(serializers.ModelSerializer):
    
    class Meta:
        """extra_kwargs = {
            'email' : {'write_only': True},
            'senha' : {'write_only': True},
            'cpf' : {'write_only': True},
            'pis' : {'write_only': True},
        }"""
        
        model = UserDados
        fields = ('id','email','louser','luser','suser', 'cpf', 'pis',
                  'pais','estado','municipio','cep','rua','numero','complemento',)
