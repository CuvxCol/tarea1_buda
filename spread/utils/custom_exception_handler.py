from rest_framework.views import exception_handler
from rest_framework import status
from .get_standar_error_response import get_standar_error_response

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    handlers = {
        'Http404' : _handle_http_404,
        'DoesNotExist' : _handle_http_404,
        'error404' : _handle_http_404,
    }

    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__

    # If the exception is in our dictionary, use our custom handler.
    if exception_class in handlers:
        response = handlers[exception_class](exc, context, response)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['codeHttp'] = response.status_code
    else:
        response = _handle_default_custom_error(exc, context, response)

    return response

def _handle_http_404(exc, context, response):
    return get_standar_error_response(exc, context, status.HTTP_404_NOT_FOUND)

def _handle_default_custom_error(exc, context, response):
    return get_standar_error_response(exc, context, status.HTTP_500_INTERNAL_SERVER_ERROR)