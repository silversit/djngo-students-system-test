from django.db import models
from django.views.generic import CreateView,UpdateView,DetailView,ListView
from django.core.validators import MinValueValidator,MaxValueValidator
from  django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    class_number = models.CharField(max_length=6)
    def __str__(self):
        return f'Student in : {self.class_number} class - {self.first_name}, {self.last_name}'
    def get_absolute_url(self):
        return reverse("student_details", kwargs={"pk" : self.pk})



class Grades(models.Model):
    grade = models.IntegerField(null=True,blank=True)
    student = models.ForeignKey("Student",on_delete=models.SET_NULL, null=True,blank=True)
    explanation = models.TextField(max_length=600,null=True,blank=True)
    SUBJECT_CHOICES = (('m', 'Math' ),
                       ('l','literature'),
                       ('s','Sport'),
                       ('b', 'Biology'),
                       ('h', 'History')
                       )
    subject = models.CharField(max_length=1,choices=SUBJECT_CHOICES,blank=True,default='m')
    date = models.DateField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse("grades_details",kwargs={"pk": self.pk})
    def __str__(self):
        return f'{self.subject}: {self.grade} on {self.date}'

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name