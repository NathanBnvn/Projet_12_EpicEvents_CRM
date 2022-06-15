from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from api.permissions import IsSupportTeam, IsManagementTeam, IsSaleTeam
from api.serializers import LoginSerializer, ClientSerializer, ContractSerializer, EventSerializer
from api.models import Client, Contract, Event
from rest_framework import viewsets


class LoginView(TokenObtainPairView):
	serializer_class = LoginSerializer
	permission_classes = (AllowAny,)

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_permissions(self):
        management = Group.objects.get(name="Management").user_set.all()
        sale = Group.objects.get(name="Sale").user_set.all()
        support = Group.objects.get(name="Support").user_set.all()

        if self.request.user in management:
            self.permission_classes = [IsManagementTeam]
        elif self.request.user in sale:
            self.permission_classes = [IsSaleTeam]
        elif self.request.user in support:
            self.permission_classes = [IsSupportTeam]
        return super(self.__class__, self).get_permissions()


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    
    def get_queryset(self):
        return Contract.objects.filter(client=self.kwargs['client_pk'])

    def get_permissions(self):
        management = Group.objects.get(name="Management").user_set.all()
        sale = Group.objects.get(name="Sale").user_set.all()
        support = Group.objects.get(name="Support").user_set.all()

        if self.request.user in management:
            self.permission_classes = [IsManagementTeam]
        elif self.request.user in sale:
            self.permission_classes = [IsSaleTeam]
        elif self.request.user in support:
            self.permission_classes = [IsSupportTeam]
        return super(self.__class__, self).get_permissions()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(client=self.kwargs['client_pk'])

    def get_permissions(self):
        management = Group.objects.get(name="Management").user_set.all()
        sale = Group.objects.get(name="Sale").user_set.all()
        support = Group.objects.get(name="Support").user_set.all()

        if self.request.user in management:
            self.permission_classes = [IsManagementTeam]
        elif self.request.user in sale:
            self.permission_classes = [IsSaleTeam]
        elif self.request.user in support:
            self.permission_classes = [IsSupportTeam]
        return super(self.__class__, self).get_permissions()
