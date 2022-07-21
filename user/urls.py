from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import  UserDadosViewSet


router = SimpleRouter()
router.register(r'dado-users', UserDadosViewSet)

