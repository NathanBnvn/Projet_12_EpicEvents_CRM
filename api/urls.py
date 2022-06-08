from posixpath import basename
from django.urls import path, include
from rest_framework_nested import routers
from .views import ClientViewSet, ContractViewSet, EventViewSet


router = routers.DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')

client_router = routers.NestedSimpleRouter(router, r'client', lookup='client')
client_router.register(r'contract', ContractViewSet, basename='contract')
client_router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(client_router.urls)),
]