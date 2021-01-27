from django.db import models


# Create your models here.
class Teacherdb(models.Model):
	"""database for teacherdb"""
	image = models.ImageField(upload_to='faceapp/images/')
	teachers = models.CharField(max_length=255)
	code = models.CharField(max_length=255)
	desgination = models.CharField(max_length=255)
	attendance = models.CharField(max_length=255)
	time = models.CharField(max_length=255)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.teachers+'-->'+self.attendance+'-->'+self.time	#--> will be shown in database doesnot effect anything