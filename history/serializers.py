from rest_framework import serializers
from .models import Monuments, User
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True},'email': {'read_only': True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )
   
    def run_validation(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            email="admin@email.com",
            password="admin"
        )
        if not user:
            msg = gettext_lazy("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authetication")
        attrs["user"] = user
        return 

class MonumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monuments
        fields = "__all__"

    def create(self, validated_data):
        monument = self.Meta.model(**validated_data)
        monument.save()       
        return monument