from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

from rest_framework import viewsets, filters, permissions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import EquipeSerializer,TitreSerializer
from .models import Equipe, Titre


class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all().order_by('nom')
    serializer_class = EquipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'abbreviation']
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TitreViewSet(viewsets.ModelViewSet):
    queryset = Titre.objects.all()
    serializer_class = TitreSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)