from rest_framework import permissions


class DocumentModelPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.method == 'POST' and view.action == 'create':
            if request.user:
                return request.user.is_authenticated
        return super().has_permission(request, view)
