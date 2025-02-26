from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from api.services.AuthService import AuthService
from api.serializers.CreateUserSerializer import CreateUserSerializer

class AuthView(ViewSet):
    @action(detail=False, methods=['post'])
    def create_user(self, request):
        dto = CreateUserSerializer(data=request.data)

        AuthService.create_by_creds(dto)
        return Response(request.data)