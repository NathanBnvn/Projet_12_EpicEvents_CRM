from django.db import models
from django.contrib.auth.models import User


# Epic Events Staff

class Gestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Epic Events Client & related content

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=400)
    sales_contact = models.ForeignKey(Sale, blank=True, null=True, on_delete=models.CASCADE, related_name='client')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Contract(models.Model):
    sales_contact = models.ForeignKey(Sale, blank=True, null=True, on_delete=models.CASCADE, related_name='contract')
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
    attendees = models.IntegerField()
    status = models.CharField(max_length=20, null=True, choices=STATUS_EVENT)
    support_contact = models.ForeignKey(Support, blank=True, null=True, on_delete=models.CASCADE, related_name='event')
    date = models.DateTimeField(null=True)
    notes = models.CharField(max_length=7000)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
