from django.urls import  path
from . import views
import cx_Oracle
urlpatterns = [

    # path('clientreviewjob',views.Clientreviewflow.startjob,name='clientreviewjob'),
    path('startjob',views.startjob,name='job'),
    path('processjob',views.startjob1,name='job2'),
    path('form',views.form,name ='job1'),
    path('processtype',views.processtype,name ='job5')




]