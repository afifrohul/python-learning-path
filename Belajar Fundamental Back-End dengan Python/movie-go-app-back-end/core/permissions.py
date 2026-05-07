from rest_framework.permissions import BasePermission
 
class IsSuperUser(BasePermission):
    """
    Allows access to superusers.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
 
class IsAdmin(BasePermission):
    """
    Allows access to admin.
    """
 
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='admin').exists()
 
class IsStudioManager(BasePermission):
    """
    Allows access to studio manager.
    """
 
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='studio_manager').exists()
 
class IsAdminOrSuperUser(BasePermission):
    """
    Allows access to admin and superusers.
    """
    def has_permission(self, request, view):
      return (
          request.user and request.user.is_authenticated and (
              request.user.is_superuser or
              request.user.groups.filter(name='admin').exists()
          )
      )
 
class IsAdminOrStudioManagerOrSuperUser(BasePermission):
    """
    Allows access to admin, studio managers, and superusers.
    """
    def has_permission(self, request, view):
      return (
          request.user and request.user.is_authenticated and (
              request.user.is_superuser or
              request.user.groups.filter(name='admin').exists() or
              request.user.groups.filter(name='studio_manager').exists()
          )
      )
 
class IsOwnerOrAdminOrSuperUser(BasePermission):
    """
    Allows access to the owner of the object, admin, and superusers.
    """
    def has_object_permission(self, request, view, obj):

        is_owner = False

        if hasattr(obj, 'user'):
            is_owner = obj.user == request.user

        elif hasattr(obj, 'reservation'):
            is_owner = obj.reservation.user == request.user

        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_superuser
                or request.user.groups.filter(name='admin').exists()
                or is_owner
            )
        )