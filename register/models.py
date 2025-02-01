from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100)
    mom_name = models.CharField(max_length=100)
    mom_second_name = models.CharField(max_length=100)
    birthday = models.DateField()
    college = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    university = models.CharField(max_length=100, default="Kirkuk University")
    year_of_study = models.IntegerField()
    type_of_study = models.CharField(max_length=20, choices=[('morning', 'Morning'), ('evening', 'Evening'), ('parallel', 'Parallel')])
    national_id_front = models.ImageField(upload_to='national_ids/')
    national_id_back = models.ImageField(upload_to='national_ids/')
    uni_id_photo = models.ImageField(upload_to='uni_ids/')

    def __str__(self):
        return f"{self.first_name} {self.second_name}"