from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from django.http import Http404

from spread.utils import get_standar_success_response
from spread.utils import CustomPagination
from spread.utils import get_spread
from api import serializers

ACCESS = AllowAny

class SaveAPIView(APIView):
    permission_classes = [ACCESS]

    def post(self, request, *args, **kwargs):
        try:
            market_id = kwargs.get('market_id')
            spread = get_spread(market_id)
            data = {
                'market_id': market_id,
                'spread': spread[market_id][0],
                'iso_code': spread[market_id][1],
            }
            serializer = serializers.SpreadSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                instance = serializers.SpreadSerializer(serializer.data).data
                data = {
                    'markets':{
                        market_id: [
                            instance['spread'],
                            instance['iso_code']
                        ]
                    }
                }
                return get_standar_success_response(
                    request=request,
                    messageUser='Recurso creado con exito',
                    data=data,
                    status_code=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404 as ex:
            raise Http404(str(ex))
        except Exception as ex:
            raise Exception(str(ex))