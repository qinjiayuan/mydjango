from django.urls import  path
from . import views
import cx_Oracle
urlpatterns = [

    # path('clientreviewjob',views.Clientreviewflow.startjob,name='clientreviewjob'),
    path('startjob',views.startjob,name='job'),
    # path('getfile',views.gets3fileid,name='upload')
    path('form',views.form,name ='job1'),
    # path('test',views.test,name='test')
    path('test',views.test,name='job3')



]