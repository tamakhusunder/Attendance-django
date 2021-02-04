from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacherdb

# Create your views here.
# def index(request):
#     return HttpResponse('Hello world 2')




# def database_collection():
# 	teacherdbs=Teacherdb.objects
# 	cursor = connection.cursor()
# 	cursor.execute("SELECT COUNT(*) FROM faceapp_teacherdb")
#     sql_totstaff = fetchone()
#     print(connection.queries)
# 	print('sunder')
# 	print(sql_totstaff)
# 	print('sunder')
# 	return teacherdbs,sql_totstaff

################

def database_collection():
	teacherdbs=Teacherdb.objects.all()
	# sql_totstaff=Teacherdb.objects.raw("SELECT  COUNT(*) FROM faceapp_teacherdb")
	sql_totstaff = Teacherdb.objects.all().count()
	sql_present = Teacherdb.objects.filter(attendance="Present").count()
	sql_absent = Teacherdb.objects.filter(attendance="Absent").count()
	print('sunder')
	print(sql_present)
	print('sunder')
	return teacherdbs,sql_totstaff,sql_present,sql_absent

def index(request):
	teacherdbs,sql_totstaff,sql_present,sql_absent=database_collection()
	return render(request,'faceapp/index.html',{'teacherdbs':teacherdbs,'sql_totstaff':sql_totstaff,'sql_present':sql_present,'sql_absent':sql_absent})

def chart(request):
	return render(request,'faceapp/charts.html',{})

def table(request):
	teacherdbs,sql_totstaff,sql_present,sql_absent=database_collection()
	return render(request,'faceapp/tables.html',{'teacherdbs':teacherdbs})


#######

# def home(request):
# 	return render(request,'faceapp/index.html',{})

