from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20)
    roll_number = models.IntegerField()

    def __str__(self):
        return self.name


class DisciplineRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    incident_date = models.DateField()
    description = models.TextField()
    severity = models.CharField(max_length=10)
    action_taken = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.student.name} - {self.severity}"
