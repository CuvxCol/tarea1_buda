from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.http import Http404

from spread.utils import get_standar_success_response
from spread.utils import CustomPagination
from spread.utils import get_spread

from api import models
from api import serializers

from datetime import datetime

ACCESS = AllowAny

class LastSavedAPIView(APIView):
    serializer_class = serializers.SpreadSerializer
    permission_classes = [ACCESS]

    def get_queryset(self, **kwargs):
        instance = models.Spread.objects.filter(isActive=True, market_id=kwargs.get('market_id')).order_by('-id')
        if(instance.count() > 0):
            return instance[:1]
        else:
            raise Http404('No se encontro ningun registro')

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset(market_id=kwargs.get('market_id'))
            serializer = self.serializer_class(queryset, many=True)
            data = {
                'markets':{
                    'saved_at': serializer.data[0]['createdAt'],
                    kwargs.get('market_id'): [
                        serializer.data[0]['spread'],
                        serializer.data[0]['iso_code']
                    ],
                }
            }
            return get_standar_success_response(
                request=request,
                messageUser='Recurso encontrado con exito',
                data=data,
                status_code=status.HTTP_200_OK
            )
        except Http404 as ex:
            raise Http404(str(ex))
        except Exception as ex:
            raise Exception(str(ex))

