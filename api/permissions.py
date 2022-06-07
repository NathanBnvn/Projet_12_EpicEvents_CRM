from datetime import datetime
from .models import Event
from rest_framework import permissions
from django.contrib.auth.models import Group


class IsSupportTeam(permissions.BasePermission):
    # Retreive and update data related to attributed events
    # Update event until it's over

    editing_methods = ("PUT", "PATCH", "DEL")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
        support_team = Group.objects.get(name="Support").user_set.all()
        if request.user in support_team :
            if view.basename == 'client' | view.basename == 'contract' | view.basename == 'event':
                return True
    
    def has_object_permission(self, request, view):

        # Retreive data related to client to attributed events
        if request.methods in self.editing_methods:
            if request.user == Event.objects.support_contact:
                return True
            
            if Event.objects.date <= datetime.now():
                return True
