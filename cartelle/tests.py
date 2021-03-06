"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth import authenticate
from rest_framework import request


from django.contrib.auth.models import User, Group
from cartelle.models import Cartella

import json
from django.core import mail

class CartelleTests(APITestCase):
    def test_create_cartella(self):
        """
        Ensure we can create a new cartella object.
        """
        print '\n\n\n\n==========START test_create_cartella =================================='
        url = '/cartelle/'
        dati_json = {'nameIT': 'ProvaCartella','nameEN': 'ProvaCartella2'}
        self.assertFalse(Cartella.objects.count())

        user = User(username='test', email='test@example.com')
        user.set_password('test')
        user.save()

        self.client.login(username='test', password='test')
        response = self.client.post(url, dati_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        print ('stampa cartella: %s' % response.data)
        print '==========END \n\n\n\n'

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        print '==========START test_create_user =================================='
        # inseriamo 2 utenti
        url = '/users/'
        dati_json = {'url': 'http://127.0.0.1:8000/users/1/', 'username': 'monica', 'email': 'monica.bramuzzi@relifeit.com', 'groups': []}
        response = self.client.post(url, data=dati_json, format='json')
        url = '/users/'
        dati_json = {'url': 'http://127.0.0.1:8000/users/2/', 'username': 'omar', 'email': 'omar.quattrin@relifeit.com', 'groups': []}
        response = self.client.post(url, dati_json, format='json')

        # controlliamo inserimento degli utenti
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print '\nOK user inserito'
        queryset = User.objects.all()
        print ('stampa users: %s' % queryset)

        # controlliamo invio email
        print '\nControlliamo la mail se e stata inviata...'
        self.assertEquals(len(mail.outbox), 2)
        print 'Controlliamo se la mail e stata inviata alla persona giusta...'
        self.assertEquals(mail.outbox[0].to, ['monica.bramuzzi@relifeit.com'])
        print 'Ok email inviata correttamente'
        print '==========END \n\n\n\n'