from django.db import models

class Student(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15) 

    class Meta:
        db_table = 'student'
