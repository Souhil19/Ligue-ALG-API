from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Titre(models.Model):
    championnat=models.IntegerField(blank=True,null=True)
    ligue=models.IntegerField(blank=True,null=True)
    coupe_dalgerie = models.IntegerField(blank=True,null=True)
    superDZ = models.IntegerField(blank=True,null=True)
    coupe_des_coupe = models.IntegerField(blank=True,null=True)
    coupe_caf = models.IntegerField(blank=True,null=True)
    Supercoupe_afrique = models.IntegerField(blank=True,null=True)


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Equipe(models.Model):
    nom =models.CharField(max_length=50)
    abbreviation=models.CharField(max_length=50)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    stade =models.CharField(max_length=50)
    dateDeCreation= models.DateField()
    president = models.CharField(max_length=50)
    entraineur = models.CharField(max_length=50, default='')
    titres = models.ForeignKey(Titre, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.nom





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
