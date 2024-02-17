from rest_framework import serializers
from .models import MyUser
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError

from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util




class UserRegistrationSerializer(serializers.ModelSerializer):
    #i gave style to this field so when i enter password i want texts to be in ***** 
    password2 = serializers.CharField(style = {'input_type':'password'},write_only=True)
    class Meta:
        model = MyUser
        fields = ['name','email','tc','password','password2']
        #i want to give extra features to this field
        extra_kwargs = {'password':{'write_only':True}}
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password !=password2 :
            raise serializers.ValidationError('password1 and password2 is not same')
    
        return attrs
    
    #since create method is already inside the modelseralizer but if i want to write my own "create"metho then i can override it and overall this is my Custom user model

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)
    



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = MyUser
        fields = ["email","password"]



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["name","email",]


class ChangeUserPassword(serializers.Serializer):
    password = serializers.CharField(max_length=225,style = {'input_type':'password'},write_only=True)
    password2 = serializers.CharField(max_length=225,style = {'input_type':'password'},write_only=True)

    class Meta:
        model = MyUser
        fields = ['password','password2']

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get("user")
        print("this is self",self)
        if password != password2 :
            raise serializers.ValidationError('password1 and password2 is not same')
        user.set_password(password)
        user.save()             
        return attrs
    


class ResetPasswordemailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)

    class Meta:
        model = MyUser
        fields = ['email']

    
    def validate(self, attrs):
        email = attrs.get("email")
        if MyUser.objects.filter(email=email).exists():
            user = MyUser.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            print("password reset token",token)
            link = 'http://localhost:3000/api/user/'+ uid + '/' + token + '/'
            print('tis is link',link)
            #SEND EMAIL
            body = 'Click Following Link to Reset Your Password' + link
            data = {'subject':'Reset your password',
                    'body':body,
                    'to_email':user.email}
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError("User with this email doesnot exists")

        return attrs


class UserPasswordResetSErializer(serializers.Serializer):
    password = serializers.CharField(max_length=225,style={'input_type':'password'},write_only = True)
    password2 = serializers.CharField(max_length=225,style={'input_type':'password'},write_only = True)
    class Meta:
        model = MyUser
        fields = ['password','password2']

    def validate(self, attrs):
        try:
                
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')

            if password != password2:
                raise serializers.ValidationError('Password1 and Password2 is not same')

            id = smart_str(urlsafe_base64_decode(uid))
            user = MyUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError("Token is not valid or Expired")

            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifire:
            PasswordResetTokenGenerator().check_token(user,token)

