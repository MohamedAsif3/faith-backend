from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView, Response
from .serializer import LoginSerializer, SignupSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    '''
    This api will handle login and return token
    '''

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request,username=username,password=password)

            if user is not None:
                '''
                We are retrieving the token for authenticated user
                '''

                token = Token.objects.get(user=user)
                response = {
                    "status" : status.HTTP_200_OK,
                    "messsage" : "success",
                    "username" : user.username,
                    "role" : user.groups.all()[0].id
                    if user.groups.exists() else None,
                    "data": {
                        "Token" : token.key
                    }



                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    "status" : status.HTTP_401_UNAUTHORIZED,
                    "message" : "Invalid username or password"
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        
        response = {
            "status" : status.HTTP_400_BAD_REQUEST,
            "message" : "Bad Request",
            "data" : serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    

# class SignupViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for adding signup instances
#     """
#     queryset = User.objects.all()
#     serializer_class = SignupSerializer

#     def create(self, request, *args, **kwargs):
#         user = self.get_object()
#         user.password 
#         return 




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token

class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)

            response = {
                "status": status.HTTP_201_CREATED,
                "message": "User registered successfully",
                "data": {
                    "username": user.username,
                    "email": user.email,
                    "token": token.key
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Bad Request",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
