from datetime import datetime
from http import client
from .models import Event
from rest_framework import permissions
from django.contrib.auth.models import Group


class IsManagementTeam(permissions.BasePermission):
    # CRUD operation on CRM system users.
    # Retreive and update all CRM system.

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True


class IsSaleTeam(permissions.BasePermission):
    # Add new clients, update client data
    # Create contract and change the contract status
    # Create a new event for the contract

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view, obj):

        if view.basename == 'client' or view.basename == 'contract':
            return True

        if view.basename == 'event':
            if request.method == 'POST' or request.method in permissions.SAFE_METHODS:
                return True


class IsSupportTeam(permissions.BasePermission):
    # Retreive and update data related to attributed events
    # Update event until it's over

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
    def has_object_permission(self, request, view, obj):
        pass

        editing_methods = ("PUT", "PATCH", "DEL")
        event = Event.objects.get(support_contact=request.user)

        if view.basename == 'event':
            if request.user == obj.support_contact:
                return True
            
            if obj.date <= datetime.now() and request.methods in editing_methods :
                return True
        
        # Retreive data related to client to attributed events
        if view.basename == 'client':
            if obj.pk == event.client.id:
                if request.method in permissions.SAFE_METHODS:
                    return True

        if view.basename == 'contract':
            if obj.client == event.client.id:
                if request.method in permissions.SAFE_METHODS:
                    return True
