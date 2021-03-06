from django.db import models

# Create your models here.

class Student(models.Model):
	regno = models.CharField(max_length=7,primary_key=True)
	name = models.CharField(max_length=20,default='')
	mq1 = models.FloatField(default=0)
	mq2 = models.FloatField(default=0)
	mq3 = models.FloatField(default=0)
	ml = models.FloatField(default=0)
	eq1 = models.FloatField(default=0)
	eq2 = models.FloatField(default=0)
	eq3 = models.FloatField(default=0)
	eq4 = models.FloatField(default=0)
	el = models.FloatField(default=0)
	assign = models.FloatField(default=0)
	proj = models.FloatField(default=0)
	def __str__(self):
		return self.regno
