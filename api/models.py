
from unicodedata import name
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Epic Events Staff


# Epic Events Client & related content

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.CharField(max_length=400)
    sales_contact = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='client')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Contract(models.Model):
    sales_contact = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='contract')
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE, related_name='contract')
    status = models.BooleanField(verbose_name="signé")
    amount =  models.FloatField()
    payment_due = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    A_VENIR = 'à venir'
    EN_COURS = 'en cours'
    TERMINÉ = 'terminé'
    ANNULÉ = 'annulé'
    
    STATUS_EVENT = [
		(A_VENIR, 'à venir'),
		(EN_COURS, 'en cours'),
		(TERMINÉ, 'terminé'),
        (ANNULÉ, 'annulé'),
	]

    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE, related_name='event')
    attendees = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS_EVENT)
    support_contact = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='event')
    date = models.DateTimeField(null=True)
    notes = models.CharField(max_length=7000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
