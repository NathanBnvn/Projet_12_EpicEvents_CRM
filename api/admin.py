from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from api.models import Client, Contract, Event



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company_name')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'status')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client', 'attendees', 'status')
