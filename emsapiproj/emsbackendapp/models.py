from django.db import models

# Create your models here.


class Certificate(models.Model):

    certificateId = models.AutoField(primary_key=True)
    certificateName = models.CharField(max_length=50)

    class Meta:
        db_table = 'Certificates'

    def __str__(self):
        return self.certificateName
    




class Department(models.Model):
    deptId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=100)
    departmentCode = models.CharField(max_length=10,unique=True)
    isActive = models.BooleanField(default=True)
    createdDate = models.DateField(auto_now_add=True)
    DEPARTMENT_TYPE=[
        ('TECH','Technology'),
        ('HR','Human Resource'),
        ('FIN','Finance'),
        ('MRT','Marketing')
    ]
    departmentType = models.CharField(max_length=10,
                                       choices=DEPARTMENT_TYPE)
    #to provide additional info
    class Meta:
        db_table = "faith_Department"
    def __str__(self):
        return self.departmentName







from django.contrib.auth.models import User


class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    #one to one with AuthUser
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    employeeName = models.CharField(max_length=100) 
    dateOfJoining = models.DateField()


    #foreign key from department 
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    certificate = models.ManyToManyField(Certificate,blank=True)
    contact = models.CharField(max_length=10)

    #profile image
    #null django
    #blank db
    profileImage = models.ImageField(upload_to='employee-profile/',null=True,blank=True)

    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return self.employeeName






