from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chart/',views.chart,name='chart'),
    path('table/',views.table,name='table'),
    # path('',views.home,name='home')
    path('register/',views.register,name='register'),
    path('face-recognization/',views.face_exe,name='face_exe'),
    path('offline/',views.offline,name='offline'),

]