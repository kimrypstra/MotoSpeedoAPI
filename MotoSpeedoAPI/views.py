from django.shortcuts import render
from rest_framework import viewsets
from .models import Key
from .serializers import KeySerializer
from .permissions import APIPermission

# Create your views here.
class KeyView(viewsets.ModelViewSet):
    queryset = Key.objects.all()
    serializer_class = KeySerializer
    permission_classes = (APIPermission,)

