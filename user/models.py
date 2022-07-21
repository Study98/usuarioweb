from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
   
    use_in_migrations: True
   
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)       
        extra_fields.setdefault('is_active', True)       
        extra_fields.setdefault('is_staff', True)       
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)       
        return self._create_user(email, password, **extra_fields)
   
class UserDados(AbstractUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique = True)
    luser = models.CharField(max_length=30, verbose_name= "Primeiro Nome")
    suser = models.CharField(max_length=100, verbose_name= "Segundo Nome")
    cpf = models.CharField(max_length=16, blank= False)
    pis = models.CharField(max_length=16, blank= False)
    pais = models.CharField(max_length=20, verbose_name= "País", blank= False)
    estado = models.CharField(max_length=10, verbose_name= "Estado", blank= False)
    municipio = models.CharField(max_length=60, verbose_name= "Município", blank= False)
    cep = models.CharField(max_length=60, verbose_name= "CEP", blank= False)
    rua = models.CharField(max_length=60, blank= False)
    numero = models.CharField(max_length=80, verbose_name= "Número da Casa", blank= False)
    complemento =models.CharField(max_length=60, blank = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['luser']
    
    objects = UserManager()
    
    def __str__ (self):
        return self.luser
