from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chart/',views.chart,name='chart'),
    path('table/',views.table,name='table'),
    # path('',views.home,name='home')
]