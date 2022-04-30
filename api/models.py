from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Titre(models.Model):
    ligue=models.IntegerField()
    superDZ = models.IntegerField()
    cup = models.IntegerField()
    caf = models.IntegerField()
    conf = models.IntegerField()
    SuperAF = models.IntegerField()


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Equipe(models.Model):
    nom =models.CharField(max_length=30)
    abbreviation=models.CharField(max_length=30)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    stade =models.CharField(max_length=30)
    dateDeCreation= models.DateField(auto_now_add=True)
    president = models.CharField(max_length=30)
    entraineur = models.CharField(max_length=30)
    titres = models.ForeignKey(Titre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
