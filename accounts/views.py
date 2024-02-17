from django.shortcuts import render
from rest_framework.response import Response
from .models import MyUser
from rest_framework.views import APIView
from rest_framework import status
from .serializer import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,ChangeUserPassword,ResetPasswordemailSerializer,UserPasswordResetSErializer
from django.contrib.auth import authenticate,login,logout
from .renders import UserRender
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistration(APIView):
    renderer_classes = [UserRender]
    def post(self,request,format=None):
        seriallizer = UserRegistrationSerializer(data=request.data)
        if seriallizer.is_valid(raise_exception=True):
            user = seriallizer.save()
            token =get_tokens_for_user(user)
            return Response({'token':token,'data':request.data},status=status.HTTP_200_OK)
        return Response(seriallizer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class UserLogin(APIView):
    renderer_classes = [UserRender]
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(request,email=email,password=password)
            if user is not None:
                token =get_tokens_for_user(user)
                return Response({"token":token,"msg":"login sucessfull"})
            return Response({"errors":{"non_field_error":"email or password"}})
        return Response(serializer.errors)
    


class User_Profile_view(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class Change_user_password(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = ChangeUserPassword(data=request.data,context={"user":request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"Your password is changed"},status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_OK)

class ResetPassword_emailview(APIView):
    renderer_classes = [UserRender]
    def post(self,request,format=None):
        serializer = ResetPasswordemailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"Your password link sent to your email"},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserPasswordResetView(APIView):
    renderer_classes = [UserRender]
    def post(self,request,uid,token,format=None):
        serializer = UserPasswordResetSErializer(data = request.data,context={'uid':uid,'token':token} )
        if serializer.is_valid(raise_exception=True):
            if serializer.is_valid(raise_exception=True):
                return Response({"msg":"Your password Reset Successfully"},status=status.HTTP_200_OK)

        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

