from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from spread.utils import CustomPagination
from django.http import Http404
from spread.utils.get_standar_success_response import get_standar_success_response
from django.db import transaction

from api import models
from api import serializers

from spread.utils.request import generate_request

ACCESS = AllowAny
BUDA_MARKETS_API_URL = 'https://www.buda.com/api/v2/markets/'

class SpreadView(APIView):
    serializer_class = serializers.SpreadSerializer
    permission_classes = [ACCESS]

    def get_spread(self, **kwargs):
        try:
            data = kwargs.get('data')
            min_sell = float(data['order_book']['asks'][0][0])
            max_buy = float(data['order_book']['bids'][0][0])
            return abs(max_buy - min_sell)
        except Exception as ex:
            raise Exception(str(ex))

    def get(self, request, *args, **kwargs):
        try:
            market_id = kwargs.get('market_id')
            response = generate_request(BUDA_MARKETS_API_URL + market_id + "/order_book", 'GET')
            if(response.status_code != 200):
                return Response({
                    'message': response.reason,
                    'status': response.status_code
                },status=response.status_code)
            data = response.json()
            spread = self.get_spread(data=data)
            return get_standar_success_response(
                request=request,
                messageUser='Recurso encontrado con exito',
                data={
                    market_id: {
                        'spread': spread
                    }
                },
                status_code=status.HTTP_200_OK
            )
        except Exception as ex:
            raise Exception(str(ex),'Error desconocido')


# class SpreadView(viewsets.ViewSet, CustomPagination):
    # serializer_class = serializers.SpreadSerializer
    # permission_classes = [ACCESS]

    # def get_queryset(self, **kwargs):
    #     return models.Spread.objects.filter(isActive=True)

    # def call_request(self, **kwargs):
    #     return generate_request(BUDA_MARKETS_API_URL + kwargs['endpoint'], 'GET')

    # def list(self, request):
    #     try:
    #         queryset = self.get_queryset()
    #         page_size = request.query_params.get('page_size', self.page_size)
    #         self.page_size = page_size
    #         page = self.paginate_queryset(queryset,request, view=self)
    #         serializer = serializers.SpreadSerializer(page, many=True).data
    #         return self.get_paginated_response(data=serializer)
    #     except Exception as ex:
    #         raise Exception(str(ex),'Error desconocido')

    # def retrieve(self, request, pk=None):
    #     try:
    #         instance = self.call_request(endpoint=pk)
    #         print(instance.status_code)
    #         queryset = self.get_queryset()
    #         instance = queryset.get(pk=pk)
    #         serializer = serializers.SpreadSerializer(instance).data
    #         return get_standar_success_response(
    #                 request=request,
    #                 messageUser='Recurso encontrado con exito',
    #                 data=serializers.SpreadSerializer(instance).data,
    #                 status_code=status.HTTP_200_OK
    #         )
    #     except Exception as ex:
    #         raise Exception(str(ex),'Error desconocido')