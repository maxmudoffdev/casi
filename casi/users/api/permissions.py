from rest_framework.permissions import BasePermission, SAFE_METHODS


class RoleBasedPermission(BasePermission):
    allowed_role = []


    def has_permission(self, request, view):

        return bool(
            request.user and
            request.user.is_authenticated  == self.allowed_role
        )


class IsAdmin(RoleBasedPermission):
    allowed_role = "admin"

class IsEditor(RoleBasedPermission):
    allowed_role = "editor"

class IsReviewer(RoleBasedPermission):
    allowed_role = "review"


class IsAuthor(RoleBasedPermission):
    allowed_role = "author"


class IsAuthorOrAdminOrEditor(BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in SAFE_METHODS:
            return True

        if not(request.user and request.user.is_authenticated):
            return False
        if request.user.is_superuser:
            return True

        return (obj.author == request.user) or (request.user.role in ['admin', 'editor'])



