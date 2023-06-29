import uuid

import environ
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouse.models import WarehouseOrder
from apps.warehouse.serializers import WarehouseOrderSerializer
from rest_framework import authentication


env = environ.Env()


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get('Authorization') != f"Token {env('STORE_TOKEN')}":
            raise exceptions.AuthenticationFailed('No correct token provided')


class WarehouseOrderView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = WarehouseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = WarehouseOrder.objects.get(id=request.data['id'])
        serializer = WarehouseOrderSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
