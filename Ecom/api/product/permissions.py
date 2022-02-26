from rest_framework import permissions


# define is admin or readonly permission
class IsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # return False
        # for read-only request allow any user to have access
        # SAFE_METHODS is the array holding hhtp verbs like GET,HEAD, OPTIONS
        # following code will grant read-only access
        if request.method in permissions.SAFE_METHODS:
            return True
        # # if the request is of edit or delete, check the user of the request
        return request.method == "GET" or request.user.is_admin
