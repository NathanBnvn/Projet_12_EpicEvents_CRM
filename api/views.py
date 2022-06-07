from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from api.permissions import IsSupportTeam
from api.serializers import ClientSerializer, ContractSerializer, EventSerializer
from api.models import Client, Contract, Event
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = (IsSupportTeam,)
    queryset = Client.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = (IsSupportTeam,)
    
    def get_queryset(self):
        return Contract.objects.filter(client=self.kwargs['client_pk'])


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (IsSupportTeam,)

    def get_queryset(self):
        return Event.objects.filter(client=self.kwargs['client_pk'])
