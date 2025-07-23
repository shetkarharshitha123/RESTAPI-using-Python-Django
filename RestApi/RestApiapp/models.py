from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=100)
    eid = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Added for login
    etreatment = models.CharField(max_length=100)

    def __str__(self):
        return self.ename
