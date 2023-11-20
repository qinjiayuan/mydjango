import datetime

import requests
from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from django.http import request
# from django.utils import log
import logging
from djangoProject import models
from djangoProject.models import OtcDerivativeCounterparty,CtptyInfoUpdateRecord
from djangoProject.models import CrtExpiredRecord
import os ,django
from datetime import date , datetime
# Create your views here.
import json
ENV = os.environ.get('ENV')
log = logging.getLogger("django.request")
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
    try:
        log.info("**************************生成公开信息流程开始******************************")
        customermanager = request.POST.get("customermanager")
        env = request.POST.get('env')
        enviroment = ENV if env is None or env == '' else ("http://" + env)
        log.info("客户经理:{},环境:{}".format(customermanager, env))
        public = publicinfoflow(customermanager)
        if public.isExisits():
            customer_manager, department = public.iscustomerExist()
            print(customer_manager)
            print(department)
            if customer_manager is None and department is None:
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
            # 删除存量流程
            models.CtptyInfoUpdateRecord.objects.filter(unifiedsocial_code=public.unifiledsocialcode).exclude(
                current_status='CLOSED').delete()
            last_client_id = [client['client_id'] for client in
                              models.OtcDerivativeCounterparty.objects.filter(unifiedsocial_code='911101080828461726',
                                                                              corporate_name='云合资本管理(北京)有限公司').all().values(
                                  'client_id')]
            models.CounterpartyOrg.objects.filter(unifiedsocial_code=public.unifiledsocialcode).update(
                lastest_client_id=last_client_id[0],
                customer_manager=customer_manager,
                introduction_department=department,
                aml_monitor_flag='true'
                )
            models.OtcDerivativeCounterparty.objects.filter(unifiedsocial_code=public.unifiledsocialcode).update(
                customer_manager=customer_manager,
                introduction_department=department,
                aml_monitor_flag='true')
            url = enviroment + '/ctptyInfoUpdate/remind/check'
            playload = {'checkDayAfter': '2010-10-10',
                        'checkDbData': 'false',
                        'checkInDate': '2022-08-31',
                        'isNewCheck': 'true',
                        'startProcess': 'true',
                        'today': date.today(),
                        'uniCodeList': '911101080828461726'}

            log.info("请求url:{}".format(url))
            log.info("请求参数:{}".format(playload))

            response = requests.post(url=url,
                                     data=playload)
            log.info(response.json())
            title = {}
            titleList = [title["title"] for title in
                         models.CtptyInfoUpdateRecord.objects.filter(unifiedsocial_code='911101080828461726').exclude(
                             current_status__in=['CLOSED', 'CANCELLED']).values('title')]
            for i in range(len(titleList)):
                title["title{}".format(i + 1)] = titleList[i]
            log.info("title is {}".format(title))
            log.info("***********公开信息变更流程生成已完成*************")
            return render(request,'result.html',{"data":"发起成功!"})
        else :
            raise ValueError("机构不存在")
    except Exception as e :
        log.info("error is :".format(str(e)))
        return render(request,'result.html',{"data":str(e)})


def form(request):
    return render(request,'ctptypublicinfo.html')



def startjob1(request):

    try :
        log.info("**************************生成公开信息流程开始******************************")
        customermanager = request.POST.get("customermanager")
        env = request.POST.get('env')
        enviroment = ENV if env is None or env == '' else ("http://" + env)
        log.info("客户经理:{},环境:{}".format(customermanager,env))
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
            url = enviroment+'/ctptyInfoUpdate/remind/check'
            playload = {'checkDayAfter': '2010-10-10',
                        'checkDbData': 'false',
                        'checkInDate': '2022-08-31',
                        'isNewCheck': 'true',
                        'startProcess': 'true',
                        'today': date.today(),
                        'uniCodeList': '911101080828461726'}

            log.info("请求url：{}".format(url))
            log.info("请求参数：")
            print(playload)
            response = requests.post(url=url,
                                     data=playload)
            log.info(response.json())
            title = {}
            titleList = [title["title"] for title in models.CtptyInfoUpdateRecord.objects.filter(unifiedsocial_code='911101080828461726').exclude(
                current_status__in=['CLOSED','CANCELLED']).values('title')]
            for i in range(len(titleList)):
                title["title{}".format(i+1)] = titleList[i]
            log.info("***********公开信息变更流程生成已完成*************")
            return JsonResponse({"status":"successfully",
                                 "data":title,
                                 "code":"200"})
        else :
            return JsonResponse({"status": "failed",
                                 "error": "云合资本管理(北京)有限公司不存在，请核查!",
                                 "code": "500"})
    except Exception as e :
        return JsonResponse({"status": "failed",
                             "error": str(e),
                             "code": "500"})

