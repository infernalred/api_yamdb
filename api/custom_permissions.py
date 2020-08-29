from rest_framework import permissions

MODERATOR_METHODS = ('PATCH', 'DELETE')


'''class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user'''


# for GENRES, TITLES and CATEGORIES set permission_classes = [IsAdminOrReadOnly]
class IsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.role == 'admin'


# for COMMENTS and REVIEWS set permissions_classes = [IsAdminOrReadOnly|IsAuthorOrModerator]
class IsAuthorOrModerator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in MODERATOR_METHODS and request.user.role == 'moderator':
            return True
        return obj.author == request.user
