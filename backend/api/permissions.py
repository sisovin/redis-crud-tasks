from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTaskOwner(BasePermission):
    """
    Custom permission to only allow owners of a task to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the task.
        return obj.owner == request.user
