from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacherdb

# Create your views here.
# def index(request):
#     return HttpResponse('Hello world 2')
def index(request):
	teacherdbs=Teacherdb.objects
	return render(request,'faceapp/index.html',{'teacherdbs':teacherdbs})


# def home(request):
# 	return render(request,'faceapp/index.html')
