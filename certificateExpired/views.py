from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
import logging
from djangoProject.models import CrtExpiredRecord
# Create your views here.
def createcertificateflow():
    #定义日志
    log = logging.getLogger()
    # clientexisit : bool =




