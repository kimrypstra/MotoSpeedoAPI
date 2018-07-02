from django.contrib.auth.models import Group
from rest_framework import permissions


class APIPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        '''
        If a user is staff, just return true
        If a user is not staff, check the request.
        If the request is safe, return true
        Otherwise, return false
        '''

        if request.user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True

        return False
