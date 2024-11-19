from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.user.role == 'admin':
            return True

class FacultyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'faculty'

class StudentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'