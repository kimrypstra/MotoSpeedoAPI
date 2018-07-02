from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from . import permissions
from .views import KeyView
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

# Create your tests here.

'''
authentication:
- test that an unauthenticated user cannot get anything
- test that a staff user can read and write 
- test that a client user can only read 

creation:
- test that a new key is created with test defaulted to false 
- test that a new key has a date, string, and test value 
- test that a new key is not created if any of the values are not present 

read: 
- test that the most recent key is delivered 
- test that keys created in the future are not delivered 
- test that deprecated keys are not delivered 
'''

class AuthenticationTests(TestCase):
    def test_unauthenticated_user_cannot_get(self):
        # The factory handles the requests
        factory = APIRequestFactory()

        # Set up an anonymous user
        user = AnonymousUser()

        # Set up the request
        request = factory.get('/keys/', format='json')

        # Force authentication
        force_authenticate(request, user=user)

        # Execute and render the request
        response = KeyView.as_view({'get': 'list'})(request)
        response.render()

        # Test
        self.assertJSONEqual(response.content, '{"detail":"Authentication credentials were not provided.", "detail": "You do not have permission to perform this action."}')


    def test_unauthenticated_user_cannot_post(self):
        # The factory handles the requests
        factory = APIRequestFactory()

        # Set up an anonymous user
        user = AnonymousUser()

        # Set up the request
        request = factory.post('/keys/', format='json')

        # Force authentication
        force_authenticate(request, user=user)

        # Execute and render the request
        response = KeyView.as_view({'post': 'list'})(request)
        response.render()

        # Test
        self.assertJSONEqual(response.content, '{"detail":"Authentication credentials were not provided.", "detail": "You do not have permission to perform this action."}')

