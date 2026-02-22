

from rest_framework import serializers
from django.contrib.auth.models import User


class LoginSerializer(serializers.ModelSerializer):
    '''
    This class handles login serialization
    '''

    username = serializers.CharField(max_length=10)
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username','password']

# class SignupSerializer(serializers.ModelSerializer):
#     '''
#     This class handles signup serialization
#     '''

#     username = serializers.CharField(max_length=10)
#     password = serializers.CharField(write_only=True)
#     firstName = serializers.CharField(150)
#     lastName = serializers.CharField(150)
#     email = serializers.CharField(254)


#     class Meta:
#         model = User
#         field = ['username','password','firstName','lastName','email']


from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password'
        ]

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data['password']
        )
        return User.objects.create(**validated_data)
    