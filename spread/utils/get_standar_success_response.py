from rest_framework.response import Response
from rest_framework import status
from datetime import datetime 

def get_standar_success_response(request, messageUser, data, status_code=status.HTTP_200_OK):
    data = {
        'codeHttp': status_code,
        'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        'message': 'Success',
        'messageUser': messageUser,
        'path': request.path,
        'method': request.method,
        'data': data,
    }
    return Response(data, status=status_code)