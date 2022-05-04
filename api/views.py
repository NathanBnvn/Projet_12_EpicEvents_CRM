from django.shortcuts import render
from django.contrib.auth import authenticate
from api.serializers import ClientSerializer, ContractSerializer, EventSerializer
from .models import GestionTeam, SupportTeam, SalesTeam, Client, Contract, Event
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    pass


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    pass


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    pass
