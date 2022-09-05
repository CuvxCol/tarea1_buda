from django.http import JsonResponse
from datetime import datetime 
 
def error_404_view(request, exception):
    return JsonResponse({
        'codeHttp': 404,
        'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        'message': 'Exception',
        'developsMessage': 'Page not found',
        'messageUser': 'Pagina no encontrada',
        'path': request.path,
        'method': request.method,
    })