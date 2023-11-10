from django.urls import  path

import clientreview.views
from . import views
import cx_Oracle
urlpatterns = [


    path('startjob',views.startjob,name='job'),
    path('processjob',views.startjob1,name='job2'),
    path('form',views.form,name ='job1'),




]