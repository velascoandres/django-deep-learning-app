from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .red_neural import predecir
from .helpers import handle_uploaded_file
from django.http import JsonResponse
# Create your views here.


# Vista para predicir una imagen a traves de la API
@csrf_exempt
def predecir_imagen(request):
    if request.method == 'POST':
        print("datos"+ str(request.FILES))
        imagen = request.FILES['imagen']
        handle_uploaded_file(imagen)
        resultados = predecir(imagen)
        return JsonResponse(resultados)
    return JsonResponse({'mensaje': 'error'})

