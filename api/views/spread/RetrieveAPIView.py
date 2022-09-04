from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import Http404

from spread.utils import get_standar_success_response
from spread.utils import CustomPagination
from spread.utils import get_spread

ACCESS = AllowAny

class RetrieveAPIView(APIView):
    permission_classes = [ACCESS]

    def get(self, request, *args, **kwargs):
        try:
            market_id = kwargs.get('market_id')
            spread = get_spread(market_id)
            return get_standar_success_response(
                request=request,
                messageUser='Recurso encontrado con exito',
                data={
                    'markets': spread,
                },
                status_code=status.HTTP_200_OK
            )
        except Http404 as ex:
            raise Http404(str(ex))
        except Exception as ex:
            raise Exception(str(ex))

