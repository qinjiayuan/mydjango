from django.urls import  path
from . import views
import cx_Oracle
urlpatterns = [

    path('startjob',views.startjob,name='job'),
    path('form',views.form,name='form')



]