from django.urls import path
from .views import *
urlpatterns = [
    path('v1/predecir', predecir_imagen, name='predecir'),
]