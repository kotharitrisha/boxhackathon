from django.db import models

# Create your models here.

class User(models.Model):
	email = models.CharField(max_length=100, primary_key=True)
	password = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)


	def __unicode__(self):
		return self.name


class Project(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=300)
	filename = models.CharField(max_length=100)
#	deadline = models.TimeField()
	owner = models.ForeignKey('User')


	def __unicode__(self):
		return self.name
		
		
class Task(models.Model):
	id = models.AutoField(primary_key=True)
	desc = models.CharField(max_length=100)
	project_id = models.ForeignKey('Project')
	owner = models.ForeignKey('User')
	step_id = models.IntegerField()
	step_deadline = models.TimeField()


	def __unicode__(self):
		return self.name
