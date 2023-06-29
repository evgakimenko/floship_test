import environ
from rest_framework import status, exceptions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.store.models import StoreOrder
from apps.store.serializers import StoreOrderSerializer


env = environ.Env()


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get('Authorization') != f"Token {env('WAREHOUSE_TOKEN')}":
            raise exceptions.AuthenticationFailed('No correct token provided')


class StoreOrderView(APIView):
    authentication_classes = [TokenAuthentication]

    def put(self, request, *args, **kwargs):
        instance = StoreOrder.objects.get(id=request.data['id'])
        serializer = StoreOrderSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
