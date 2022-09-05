from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import Http404

from spread.utils import get_standar_success_response
from spread.utils import CustomPagination
from spread.utils import get_spread
from spread.utils import buda
from spread.utils import xmap

ACCESS = AllowAny

class ListAPIView(APIView):
    permission_classes = [ACCESS]

    def get(self, request, *args, **kwargs):
        try:
            markets = buda.get_markets()
            markets = markets['markets']

            spreads = xmap(lambda market: {market['id']:get_spread(market['id'])}, markets)
                
            return get_standar_success_response(
                request=request,
                messageUser='Recurso encontrado con exito',
                data={'markets': spreads},
                status_code=status.HTTP_200_OK
            )
        except Http404 as ex:
            raise Http404(str(ex))
        except Exception as ex:
            raise Exception(str(ex))