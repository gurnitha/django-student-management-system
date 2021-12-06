# apps/student/models.py

# Django modules
from django.db import models

# Locals
from apps.user.models import CustomUserModel

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name 


class Session_Year(models.Model):
	session_start = models.CharField(max_length=100)
	session_end = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'Session year'


	def __str__(self):
		return self.session_start + " - " + self.session_end


class Student(models.Model):
	admin = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
	address = models.TextField()
	gender = models.CharField(max_length=100)
	course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
	session_year_id = models.ForeignKey(Session_Year, on_delete=models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.admin.first_name + " " + self.admin.last_name