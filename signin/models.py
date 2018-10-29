from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=50)
    order = models.SmallIntegerField()

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return ', '.join([self.last_name, self.first_name])


class Line(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    time_in = models.TimeField()
    in_signature = models.ImageField()
    time_out = models.TimeField()
    out_signature = models.ImageField()

    class Meta:
        ordering = ['date', 'student'] 