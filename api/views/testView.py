from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from spread.utils import CustomPagination
from django.http import Http404
from spread.utils.get_standar_success_response import get_standar_success_response
from django.db import transaction

from api import models
from api import serializers

ACCESS = AllowAny

# class TestView(viewsets.ViewSet, PageNumberPagination):
class TestView(viewsets.ViewSet, CustomPagination):
    serializer_class = serializers.TestSerializer
    permission_classes = [ACCESS]

    def get_queryset(self, **kwargs):
        return models.Test.objects.filter(isActive=True)
    
    def list(self, request):
        try:
            queryset = self.get_queryset()
            page_size = request.query_params.get('page_size', self.page_size)
            self.page_size = page_size
            page = self.paginate_queryset(queryset,request, view=self)
            serializer = serializers.TestSerializer(page, many=True).data
            return self.get_paginated_response(data=serializer)
        except Exception as ex:
            raise Exception(str(ex),'Error desconocido')
            
    @transaction.atomic
    def create(self, request):
        try:
            check_point = transaction.savepoint()
            serializer = serializers.TestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return get_standar_success_response(
                    request=request,
                    messageUser='Recurso creado con exito',
                    data=serializers.TestSerializer(serializer.data).data,
                    status_code=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            transaction.savepoint_rollback(check_point)
            raise Exception(str(ex),'Error desconocido')

    def retrieve(self, request, pk=None):
        try:
            queryset = self.get_queryset()
            instance = queryset.get(pk=pk)
            serializer = serializers.TestSerializer(instance).data
            return get_standar_success_response(
                    request=request,
                    messageUser='Recurso encontrado con exito',
                    data=serializers.TestSerializer(instance).data,
                    status_code=status.HTTP_200_OK
                )
        except models.Test.DoesNotExist as ex:
            raise Http404(str(ex),'Recurso no encontrado')
        except Exception as ex:
            raise Exception(str(ex),'Error desconocido')

    @transaction.atomic
    def update(self, request, pk=None):
        try:
            check_point = transaction.savepoint()
            queryset = self.get_queryset()
            instance = queryset.get(pk=pk)
            serializer = serializers.TestSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return get_standar_success_response(
                    request=request,
                    messageUser='Recurso editado con exito',
                    data=serializers.TestSerializer(instance).data,
                    status_code=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Test.DoesNotExist as ex:
            raise Http404(str(ex),'Recurso no encontrado')
        except Exception as ex:
            transaction.savepoint_rollback(check_point)
            raise Exception(str(ex),'Error desconocido')

    @transaction.atomic
    def partial_update(self, request, pk=None):
        try:
            check_point = transaction.savepoint()
            queryset = self.get_queryset()
            instance = queryset.get(pk=pk)
            serializer = serializers.TestSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                # return Response(serializer.data)
                return get_standar_success_response(
                    request=request,
                    messageUser='Recurso editado con exito',
                    data=serializers.TestSerializer(instance).data,
                    status_code=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Test.DoesNotExist as ex:
            raise Http404(str(ex),'Recurso no encontrado')
        except Exception as ex:
            transaction.savepoint_rollback(check_point)
            raise Exception(str(ex),'Error desconocido')

    @transaction.atomic
    def destroy(self, request, pk=None):
        try:
            check_point = transaction.savepoint()
            queryset = self.get_queryset()
            instance = queryset.get(pk=pk)
            if instance:
                instance.isActive = False
                instance.save()
                return get_standar_success_response(
                    request=request,
                    messageUser='Recurso eliminado con exito',
                    data=serializers.TestSerializer(instance).data,
                    status_code=status.HTTP_200_OK
                )
            return Response(status=status.HTTP_404_NOT_FOUND)
        except models.Test.DoesNotExist as ex:
            raise Http404(str(ex),'Recurso no encontrado')
        except Exception as ex:
            transaction.savepoint_rollback(check_point)
            raise Exception(str(ex),'Error desconocido')