from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_author:
            return True


class NotRegisterUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False
