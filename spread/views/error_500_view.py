from django.http import JsonResponse
from datetime import datetime 
 
def error_500_view(request):
    return JsonResponse({
        'codeHttp': 500,
        'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        'message': 'Exception',
        'developsMessage': 'Internal server error',
        'messageUser': 'Error interno del servidor',
        'path': request.path,
        'method': request.method,
    })