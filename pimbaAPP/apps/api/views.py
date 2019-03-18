from django.shortcuts import render
from .red_neural import predecir
from .helpers import handle_uploaded_file
from django.http import JsonResponse
# Create your views here.


# Vista para predicir una imagen a traves de la API
def predecir_imagen(request):
    if request.method == 'POST':
        imagen = request.POST['imagen']
        handle_uploaded_file(imagen)
        print(imagen)
        resultados = {'status': 'OK'}
        return JsonResponse(resultados)
    return JsonResponse({'mensaje': 'error'})

