from django.urls import  path
from . import views
import cx_Oracle
urlpatterns = [

    path('certificatesjob',views.certificatesjob,name='job1'),
    path('publicinfojob',views.publicinfojob,name='job2'),
    path('reviewjob',views.reviewjob,name='job3'),
    path('processexpiredjob',views.processexpiredjob,name='job'),
    path('form',views.form,name='form'),

]