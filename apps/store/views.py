import environ
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.store.models import StoreOrder
from apps.store.serializers import StoreOrderSerializer


env = environ.Env()
environ.Env.read_env()


class StoreOrderView(APIView):
    def put(self, request, *args, **kwargs):
        if request.headers.get('Authorization') == f"Bearer {env('WAREHOUSE_TOKEN')}":
            instance = StoreOrder.objects.get(id=request.data['id'])
            serializer = StoreOrderSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
