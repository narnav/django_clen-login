from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
def index(req):
    return Response('hello')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(req):
    return Response('secret')