from rest_framework import serializers

from .models import Equipe, Titre


class EquipeSerializer(serializers.HyperlinkedModelSerializer):
    logo = serializers.ImageField(required=False)

    class Meta:
        model = Equipe
        fields = ('__all__')


class TitreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titre
        fields = ('__all__')

