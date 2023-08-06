from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewset import FormulatorAPI

app_name = 'form_generator'

router = DefaultRouter()
router.register(r'', viewset=FormulatorAPI, basename='form')

urlpatterns = [
    path('', include(router.urls)),
]

