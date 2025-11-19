from rest_framework.permissions import BasePermission


class CheckRolePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'client'


class CreateHotelPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.status == 'owner'