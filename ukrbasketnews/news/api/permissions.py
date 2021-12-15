from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_author


class IsAnonymousUser(BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsCurrentUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and view.kwargs.get('user_id') == request.user.id
