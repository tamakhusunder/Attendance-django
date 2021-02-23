from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('',views.home,name='home')
    path('register/',views.register,name='register'),
    path('addstaff/',views.addstaff,name='addnewstaff'),
    path('face-application/',views.face_exe,name='face_exe'),
    path('chart/',views.chart,name='chart'),
    path('table/',views.table,name='table'),
    path(r'face-application/facecapture', views.captureface, name='capturefaces'),
    path('recognization/', views.recognization, name='recognizations'),
    path('offline/',views.offline,name='offline'),

]