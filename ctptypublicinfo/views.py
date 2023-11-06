import datetime

import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from django.utils import log
from djangoProject import models
from djangoProject.models import OtcDerivativeCounterparty,CtptyInfoUpdateRecord
from djangoProject.models import CrtExpiredRecord
import os ,django
from datetime import date , datetime
# Create your views here.
import json
env = os.environ.get('ENV')
class publicinfoflow(object):

    def __init__(self,customerManager):

        self.unifiledsocialcode = '911101080828461726'
        self.customerManager = customerManager
        self.clientIdList = []


    def isExisits(self,):
        counterpartyOrg = models.CounterpartyOrg.objects.filter(unifiedsocial_code=self.unifiledsocialcode).all()
        clientId = models.OtcDerivativeCounterparty.objects.filter(unifiedsocial_code=self.unifiledsocialcode).all()
        return True if len(counterpartyOrg) and len(clientId) else False

    def iscustomerExist(self):
        user_list = list(models.Auser.objects.filter(username=self.customerManager).values("userid", "orgid"))

        if not user_list:
            return None, None
        dept_code = list(models.Aorg.objects.filter(orgid=user_list[0]["orgid"]).values("dept_code"))
        department = dept_code[0]["dept_code"]
        customerManager = user_list[0]["userid"]
        return customerManager, department



def startjob(request):
    try :

        customermanager = request.POST.get("customermanager")
        public = publicinfoflow(customermanager)
        if public.isExisits():
            customer_manager ,department = public.iscustomerExist()
            print(customer_manager)
            print(department)
            if  customer_manager is None  and department is None   :
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
            #删除存量流程
            models.CtptyInfoUpdateRecord.objects.filter(unifiedsocial_code=public.unifiledsocialcode).exclude(current_status='CLOSED').delete()
            last_client_id = [client['client_id'] for client in models.OtcDerivativeCounterparty.objects.filter(unifiedsocial_code='911101080828461726',
                                                                            corporate_name='云合资本管理(北京)有限公司').all().values('client_id')]
            models.CounterpartyOrg.objects.filter(unifiedsocial_code=public.unifiledsocialcode).update(lastest_client_id=last_client_id[0],
                                                                                                       customer_manager=customer_manager,
                                                                                                       introduction_department=department,
                                                                                                       aml_monitor_flag='true'
                                                                                                       )
            models.OtcDerivativeCounterparty.objects.filter(unifiedsocial_code=public.unifiledsocialcode).update(customer_manager=customer_manager,
                                                                                                                 introduction_department=department,
                                                                                                                 aml_monitor_flag='true')
            url = env+'/ctptyInfoUpdate/remind/check'
            playload = {'checkDayAfter': '2010-10-10',
                        'checkDbData': 'false',
                        'checkInDate': '2022-08-31',
                        'isNewCheck': 'true',
                        'startProcess': 'true',
                        'today': date.today(),
                        'uniCodeList': '911101080828461726'}
            log.info("***********开始生成公开信息变更流程*************")
            log.info("请求url：{}".format(url))
            log.info("请求参数：")
            print(playload)
            response = requests.post(url=url,
                                     data=playload)
            log.info(response.json())
            log.info("***********公开信息变更流程生成已完成*************")
            return render(request,'clientreview.html',{"data":response.json(),"code":"200"})
        else :
            raise ValueError("机构不存在")
    except Exception as e :
        return render(request,'clientreview.html',{"data":str(e),"code":"500"})


def form(request):
    return render(request,'ctptypublicinfo.html')




