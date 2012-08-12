from django.db import models

# Create your models here.

class User(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)


	def __unicode__(self):
		return self.name


class Project(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=300)
	filename = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name
		
		
class Task(models.Model):
	id = models.AutoField(primary_key=True)
	desc = models.CharField(max_length=100)
	project = models.ForeignKey('Project')
	owner = models.ForeignKey('User')
	step_id = models.IntegerField()
	step_deadline = models.DateTimeField()


	def __unicode__(self):
		return self.name
