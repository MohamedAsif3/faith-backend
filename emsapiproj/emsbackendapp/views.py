from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Certificate, Department, Employee
from .serializer import CertificateSerializer, DepartmentSerializer, EmployeeSerializer
from rest_framework import status


# Create your views here.


@api_view(['GET', 'POST'])
def department_list_create(request):
    '''
        end point to list and create department
    '''
    try:
        if request.method == 'GET':
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'POST':
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response("METHOD NOT SUPPORTED",status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

 
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def department_update_patch_delete(request, dept_id):
    """
    Endpoint to retrieve, update, partially update, or delete a department
    """
    try:
        department = Department.objects.get(pk=dept_id)

        if request.method == 'GET':
            serializer = DepartmentSerializer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = DepartmentSerializer(department,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PATCH':
            serializer = DepartmentSerializer(department,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            department.delete()
            return Response(
                {"message": "Department deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )

    except Department.DoesNotExist:
        return Response({"error": "Department not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )




#class based view






from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from Authentication.permissions import IsAdminGroup
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing employee instances.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated,IsAdminGroup]

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)
    
    def destroy(self):
        employee = self.get_object()
        employee.isActive = False
        employee.save()

        return Response(
            {"message": "Employee deactivated successfully"},
            status=status.HTTP_200_OK
        )


class CerificateViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing certificate instances.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
