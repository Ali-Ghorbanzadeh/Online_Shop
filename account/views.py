from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_200_OK)


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return render(request, 'home.html')


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm-password')

        if len(password) < 6 and len(confirm_password) < 6 and \
                password != confirm_password and User.objects.filter(username=username).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return Response(status=status.HTTP_202_ACCEPTED)
