from django.db import models


# Create your models here.
class StaffInfo(models.Model):
	"""database/table for staffs"""
	name=models.CharField(max_length=255)
	image = models.ImageField(upload_to='faceapp/images/staffs')
	code = models.CharField(primary_key=True, max_length=255)
	department=models.CharField(max_length=255)
	desgination = models.CharField(max_length=255)
	specialization = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	contact = models.CharField(max_length=255)
	address = models.CharField(max_length=255)

	def __str__(self):
		return self.name+'-->'+self.code+'-->'+self.department	#--> will be shown in database doesnot effect anything


class AttendanceTb(models.Model):
	"""table for attendance from webcame"""
	# status_choices=[
	# 	('PRESENT','Present'),
	# 	('ABSENT','Absent'),
	# 	]
	t=models.ForeignKey('StaffInfo',on_delete=models.CASCADE)
	date=models.CharField(max_length=255)
	time=models.CharField(max_length=255)
	status=models.CharField(max_length=255)

	def __str__(self):
		return self.t_id+'-->'+self.date