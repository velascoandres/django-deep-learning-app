from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .red_neural import predecir_resnet50, predecir_vgg16
from .helpers import handle_uploaded_file
from django.http import JsonResponse
# Create your views here.


# Vista para predicir una imagen a traves de la API
@csrf_exempt
def predecir_imagen(request):
    if request.method == 'POST':
        imagen = request.FILES['imagen']
        ruta_imagen = handle_uploaded_file(imagen)
        #resultados = predecir_resnet50(ruta_imagen)
        resultados = predecir_vgg16(ruta_imagen)
        return JsonResponse(resultados)
    return JsonResponse({'mensaje': 'error'})

