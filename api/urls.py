from posixpath import basename
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, ClientViewSet, ContractViewSet, EventViewSet


router = routers.DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')

client_router = routers.NestedSimpleRouter(router, r'client', lookup='client')
client_router.register(r'contract', ContractViewSet, basename='contract')
client_router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path(r'api/login', LoginView.as_view()),
    path(r'api/login/refresh', TokenRefreshView.as_view()),
    path(r'api/', include(router.urls)),
    path(r'api/', include(client_router.urls)),
]