from rest_framework import permissions

class IsAuthenticatedAndOwnerOrDeny(permissions.BasePermission):

    def has_permission(self, request, view):
        # check if the user is authenticated
        return self.request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        # check if the user is the owner of the inference object
        return obj.user == request.user
