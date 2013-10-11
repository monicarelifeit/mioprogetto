from rest_framework import serializers

# importiamo la struttura dei dati (modello)
from django.contrib.auth.models import User, Group
from cartelle.models import Cartella

# serialize ci serve per poter tradurre il modello nativo django in altri formati (es. Json)
# definiamo le classi serializer per ogni diverso oggetto
# quindi nel campo field definiamo solo gli attributi
# che ci servono per costruire il nostro oggetto json per il response
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CartellaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cartella
		fields = ('nameIT',)