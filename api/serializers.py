from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Client, Contract, Event


class LoginSerializer(TokenObtainPairSerializer):

	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		token['password'] = user.password
		return token


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contract
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = "__all__"