from rest_framework import permissions


class IsGestionTeam(permissions.BasePermission):
    # CRUD operation on CRM system users.
    # Retreive and update all CRM system.

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view):
        pass


class IsSalesTeam(permissions.BasePermission):
    # Add new clients, update client data
    # Create contract and change the contract status
    # Create a new event for the contract

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
        if view.basename == 'client' | view.basename == 'contract' | view.basename == 'event':
            return True
    
    def has_object_permission(self, request, view):
        pass


class IsSupportTeam(permissions.BasePermission):
    # Retreive and update data related to attributed events
    # Retreive data related to client to attributed events
    # Update event until it's over

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view):
        pass