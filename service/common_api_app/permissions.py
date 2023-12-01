from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and (obj.organizer == request.user or request.user.is_staff))


class IsInstitutionWorkerOrStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated 
                    and (request.user.is_staff or ('institution_workers' in request.user.groups.all())))