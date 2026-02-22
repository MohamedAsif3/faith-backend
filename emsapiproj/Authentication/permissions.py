



from rest_framework.permissions import BasePermission

class IsAdminGroup(BasePermission):
    '''
    Allow access only to  users in admin group or role
    '''

    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()
        )
    