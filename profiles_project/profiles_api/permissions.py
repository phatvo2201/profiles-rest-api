from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):

    """add permission class function to class"""

    def has_object_permission(self,request,view,obj):
        """check user trying to edit"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
