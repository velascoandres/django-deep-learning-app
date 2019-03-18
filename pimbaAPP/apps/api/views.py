from django.shortcuts import render
#from .utils import predictor

# Create your views here.

def predecir_imagen(request):
    if request.method =='POST':
        imagen = request.POST['imagen']
