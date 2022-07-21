from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import  UserDadosViewSet


router = SimpleRouter()
router.register('dado-users', UserDadosViewSet)

