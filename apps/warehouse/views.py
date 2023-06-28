import uuid

import environ
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouse.serializers import WarehouseOrderSerializer

env = environ.Env()
environ.Env.read_env()


class WarehouseOrderView(APIView):
    def post(self, request, *args, **kwargs):
        if request.headers.get('Authorization') == f"Bearer {env('STORE_TOKEN')}":
            serializer = WarehouseOrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
