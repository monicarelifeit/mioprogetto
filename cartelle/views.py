from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
# spedire email
from django.core import mail

# importiamo la struttura dei dati (modello)
from django.contrib.auth.models import User, Group
from cartelle.models import Cartella

# importiamo i serializer definiti in precedenza con gli attributi che vogliamo mostrare nella view
from cartelle.serializers import UserSerializer, GroupSerializer, CartellaSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # non richiede l'autenticazione nel caso di un post per inserire un nuovo utente
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def post_save(self, obj, created=False):
    	# manda mail di benvenuto
    	print ('Mandiamo la mail a %s' % obj.email)
        mail.send_mail('Subject here', 'Here is the message.', 'from@example.com', [obj.email], fail_silently=False)
        pass 

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CartellaViewSet(viewsets.ModelViewSet):
    """
    API che consente all'app Cartella di essere visualizzato o modificato.
    """
    # DA TOGLIERE non richiede l'autenticazione 
    permission_classes = (permissions.AllowAny,)
    
    queryset = Cartella.objects.all()
    serializer_class = CartellaSerializer