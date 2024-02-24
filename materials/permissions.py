from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Права для группы модераторов"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()


class IsOwner(BasePermission):
    """Права для владельцев"""

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return request.method in ('GET', 'POST', 'PATH', 'DELETE',)

        return False
