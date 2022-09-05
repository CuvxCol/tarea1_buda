from rest_framework.response import Response
from datetime import datetime 

def get_standar_error_response(exc, context, status_code):
    args = exc.args
    developsMessage = args[0] if len(args) > 0 else ''
    messageUser = args[1] if len(args) > 1 else 'Sin mensaje de usuario'
    data = {
        # 'error': 'Internal server error',
        'codeHttp': status_code,
        'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        'message': 'Exception',
        'developsMessage': developsMessage,
        'messageUser': messageUser,
        'path': context.get('view').request.path,
        'method': context.get('view').request.method,
    }
    return Response(data, status=status_code)