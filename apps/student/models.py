# apps/student/models.py

# Django modules
from django.db import models

# Locals

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