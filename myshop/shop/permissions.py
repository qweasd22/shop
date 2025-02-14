from rest_framework import permissions

class IsProductOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD, OPTIONS для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Разрешить редактирование только владельцу или админу
        return obj.owner == request.user or request.user.is_staff