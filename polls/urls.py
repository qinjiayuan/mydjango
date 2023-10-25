from django.urls import  path
from . import views
import cx_Oracle
urlpatterns = [

    # path('helloworld', views.helloworld, name='hellod'),
    # path('queryClient',views.queryClient,name='client'),
    path('index',views.index,name='index'),
    path('form',views.form,name='form')

]