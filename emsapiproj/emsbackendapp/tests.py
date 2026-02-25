from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Department
# Create your tests here.

#unit testing department APIs
#create a class

class DepartmentAPITest(APITestCase):

    """
    Setup() runs before every test cases
    """

    def setUp(self):
        # self.url = reverse('department/')

        self.url = reverse('department-list-create')
        self.department = Department.objects.create(
            departmentName = "IT",
            departmentCode = "IT01",
            departmentType = "TECH"
        )

    #TEST CASE 1
    def test_get_department(self):
        response = self.client.get(self.url)


        #to check the data we have inbuilt classes
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)

    #TEST CASE FOR POST
    
    def test_post_department(self):
        data = {
            "departmentName" : "HR",
            "departmentCode" : "HR01",
            "departmentType" : "HR"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(),2)

    #update and delete

    def test_update_department(self):
        url = reverse("department-update-patch-delete",args=[self.department.deptId])
        
        updated_data = {
            "departmentName" : "Marketing",
            "departmentCode" : "MR01",
            "departmentType" : "MRT"
        }

        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.department.refresh_from_db()
        self.assertEqual(self.department.departmentName,"Marketing")
        
    def test_delete_department(self):
        url = reverse("department-update-patch-delete",args=[self.department.deptId])

        response = self.client.delete(url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(),0)
