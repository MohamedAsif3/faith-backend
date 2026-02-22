from django.urls import path
from .views import department_list_create, department_update_patch_delete,EmployeeViewSet,CerificateViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'certificate', CerificateViewSet)

urlpatterns = [
    path('departments/', department_list_create, name='department-list-create'),
    path('departments/<int:dept_id>/', department_update_patch_delete, name='department-update-patch-delete')
]


urlpatterns += router.urls

