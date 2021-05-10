from django.shortcuts import render
from rest_framework import permissions
from rest_framework import permissions

from apps.evaluation_folder.models import EvaluationFolder
from apps.user.models.user import Account, Admin, Insurer, AssessorExpert


class SuperuserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsInsurerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # create permission are allowed to
        user = Admin.objects.filter(user_id=request.user.pk).values('role')
        if not user.exists():
            user = Insurer.objects.filter(user_id=request.user.pk).values('role')
        elif not user.exists():
            user = AssessorExpert.objects.filter(user_id=request.user.pk).values('role')
        if not user.exists():
            return False
        permission = request.user and request.user.is_superuser or user[0]['role'] == "0"
        if not permission:
            # Read permissions are allowed to  Assessor expert user
            # so we'll always allow GET, HEAD or OPTIONS requests.
            return bool(request.method in permissions.SAFE_METHODS)

        return bool(permission)


class ReadonlyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed to  Assessor expert user
        # so we'll always allow GET, HEAD or OPTIONS requests.
        return bool(request.method in permissions.SAFE_METHODS)
