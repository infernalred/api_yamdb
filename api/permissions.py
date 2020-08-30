from rest_framework import permissions

MODERATOR_METHODS = ('PATCH', 'DELETE')


# for GENRES, TITLES and CATEGORIES set permission_classes = [IsAdminOrReadOnly]
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff and request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff and request.user.role == 'admin'


# for COMMENTS and REVIEWS set permissions_classes = [IsAdminOrReadOnly|IsAuthorOrModerator&IsAuthenticatedOrReadOnly]
class IsAuthorOrModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in MODERATOR_METHODS and request.user.role == 'moderator':
            return True
        return obj.author == request.user


class AdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
