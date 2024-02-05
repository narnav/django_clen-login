from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import Product
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def index(req):
    return Response('hello')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(req):
    return Response('secret')


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


@permission_classes([IsAuthenticated])
class ProductView(APIView):
    def get(self, request):
        user= request.user
        my_model = user.product_set.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
