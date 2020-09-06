from rest_framework import permissions

MODERATOR_METHODS = ('PATCH', 'DELETE')


class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or \
            request.user.is_authenticated and request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or \
            request.user.is_authenticated and request.user.role == 'admin'


class IsAuthorOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or \
            request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.method in MODERATOR_METHODS \
            and request.user.role == 'moderator' or obj.author == request.user
