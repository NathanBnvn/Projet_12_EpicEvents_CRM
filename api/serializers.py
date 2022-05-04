from rest_framework import serializers
from .models import SalesTeam, SupportTeam, GestionTeam, Client, Contract, Event


class SalesTeamSerializer(serializers.ModelSerializer):
    pass


class SupportTeamSerializer(serializers.ModelSerializer):
    pass


class GestionTeamSerializer(serializers.ModelSerializer):
    pass


class ClientSerializer(serializers.ModelSerializer):
    pass


class ContractSerializer(serializers.ModelSerializer):
    pass


class EventSerializer(serializers.ModelSerializer):
    pass