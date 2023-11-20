import datetime
import os
from datetime import datetime,timedelta
import requests
from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
# from django.utils import log
from djangoProject import models
import datetime
import os
from datetime import datetime, timedelta

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import logging

from djangoProject import models

# Create your views here.
ENV = os.environ.get("ENV")
log  = logging.getLogger('django.request')
class Option():

    def __init__(self,corporatename,customermanager):
        self.corporatename = corporatename
        self.customermanager = customermanager
    def isExist(self):
        try:

            counterpartyOrg = models.CounterpartyOrg.objects.filter(corporate_name=self.corporatename).values(
                "corporate_name")
            counterparty = models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.corporatename).values(
                "corporate_name", "client_id")

            if not counterpartyOrg:
                # logging.error("该机构不存在")
                log.info('该机构不存在')
            if not counterparty:
                log.info('该机构不存在')
            return False if ((len(counterparty) == 0) or len(counterpartyOrg) == 0) else True
        except Exception as e:
            log.info("error is {}".format(str(e)))
            return HttpResponse(e)

    # 查询用户是否存在
    def iscustomerExist(self):
        user_list = list(models.Auser.objects.filter(username=self.customermanager).values("userid", "orgid"))

        if not user_list:
            return None, None
        dept_code = list(models.Aorg.objects.filter(orgid=user_list[0]["orgid"]).values("dept_code"))
        department = dept_code[0]["dept_code"]
        customerManager = user_list[0]["userid"]
        return customerManager, department
    def getClientid(self):
        for client in models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.corporatename).values('client_id'):
            yield client['client_id']


def startjob(request):
    log.info('11')
    corporatename = request.POST.get("corporatename")
    customermanager = request.POST.get("customermanager")
    publicinfo = Option(corporatename, customermanager)
    env = request.POST.get('env')
    enviroment = ENV if env is None or env == '' else ("http://" + env)
    try:
        log.info("*************************开始生成期权产品监测流程*************************")
        if publicinfo.isExist():
            user, department = publicinfo.iscustomerExist()
            if user is None or department is None:
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
            else:
                log.info("userid is {},department is {}".format(user, department))
            # 备份处理在途回访流程，然后过滤后恢复
            review = [flow["doc_id"] for flow in
                      models.ClientReviewRecord.objects.filter(client_name=corporatename).exclude(
                          current_status__in=['CLOSED', 'CANCELLED']).values("doc_id")]
            log.info({"未关闭的回访": "".format(review)})
            models.ClientReviewRecord.objects.filter(doc_id__in=review).update(current_status='CLOSED')

            # 处理期权产品检测在途流程
            models.CounterpartyProdMonitorFlow.objects.filter(corporate_name=corporatename).exclude(
                current_status='CANCELLED').delete()

            # 设置满足条件
            process_date = datetime.now() - timedelta(days=181)
            models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename,
                                                            is_prod_holder='03').update(
                aml_monitor_flag='true',
                client_qualify_review='true',
                master_agreement_date=process_date,
                return_visit_date=process_date,
                allow_busi_type='OPTION,TRS,PRODUCT',
                customer_manager=user,
                introduction_department=department)
            client_id = [client['client_id'] for client in
                         models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).values(
                             "client_id")]
            if client_id:
                today = datetime.now()
                current_date = datetime.strftime(today, '%Y-%m-%d')
                for client in publicinfo.getClientid():
                    url = enviroment + '/api/test/optionProdMonitor'
                    params = {"clientId": client, "date": current_date}
                    log.info("params is {}".format(params))
                    response = requests.get(url=url, params=params)
                    log.info(response.json())
            if review:
                # 还原回访流程
                models.ClientReviewRecord.objects.filter(doc_id__in=review).update(current_status='PROCESSING')
            title = {}
            titleList = [title["title"] for title in
                         models.CounterpartyProdMonitorFlow.objects.filter(corporate_name=corporatename,
                                                                           current_status__in=['PROCESSING',
                                                                                               'TEMPORARY']).values(
                             'title')]
            for i in range(len(titleList)):
                title["title{}".format(i + 1)] = titleList[i]
            log.info("titleList is {}".format(title))
            log.info("***************************期权产品监测流程已生成****************************")



            return render(request,'result.html',{"data":"发起成功!"})
        else :
             raise ValueError("机构不存在")

    except  Exception as e :
        log.info("error is :".format(str(e)))

        return render(request,'result.html', {"data": str(e)})
def form(request):
    return render(request,'counterpartyoption.html')


def startjob1(request):
    corporatename = request.POST.get("corporatename")
    customermanager = request.POST.get("customermanager")
    env = request.POST.get('env')
    enviroment = ENV if env is None or env == '' else ("http://"+env)
    publicinfo = Option(corporatename,customermanager)
    try:
        log.info("*************************开始生成期权产品监测流程*************************")
        if publicinfo.isExist():
            user , department = publicinfo.iscustomerExist()
            if user is None or department is None:
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
            else :
                log.info("userid is {},department is {}".format(user,department))
            #备份处理在途回访流程，然后过滤后恢复
            review = [flow["doc_id"] for flow in models.ClientReviewRecord.objects.filter(client_name=corporatename).exclude(current_status__in=['CLOSED','CANCELLED']).values("doc_id")]
            log.info({"未关闭的回访":"".format(review)})
            models.ClientReviewRecord.objects.filter(doc_id__in=review).update(current_status='CLOSED')

            #处理期权产品检测在途流程
            models.CounterpartyProdMonitorFlow.objects.filter(corporate_name=corporatename).exclude(current_status='CANCELLED').delete()

            #设置满足条件
            process_date =datetime.now() - timedelta(days=181)
            models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename,
                                                            is_prod_holder='03').update(
                aml_monitor_flag='true',
                client_qualify_review='true',
                master_agreement_date=process_date,
                return_visit_date=process_date,
                allow_busi_type='OPTION,TRS,PRODUCT',
                customer_manager=user,
                introduction_department=department)
            client_id = [client['client_id'] for client in models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).values("client_id")]
            if client_id :
                today = datetime.now()
                current_date= datetime.strftime(today,'%Y-%m-%d')
                for client in publicinfo.getClientid():
                    url = enviroment + '/api/test/optionProdMonitor'
                    params = {"clientId": client, "date": current_date}
                    log.info("params is {}".format(params))
                    response = requests.get(url=url, params=params)
                    log.info(response.json())
            if review :
                # 还原回访流程
                models.ClientReviewRecord.objects.filter(doc_id__in=review).update(current_status='PROCESSING')
            title = {}
            titleList = [title["title"] for title in models.CounterpartyProdMonitorFlow.objects.filter(corporate_name=corporatename,
                                                                                                       current_status__in=['PROCESSING','TEMPORARY']).values('title')]
            for i in range(len(titleList)):
                title["title{}".format(i+1)] = titleList[i]
            log.info("titleList is {}".format(titleList))
            log.info("***************************期权产品监测流程已生成****************************")


            return JsonResponse({"status":"successfully",
                                 "data":title,
                                 "code":'200'})

        return JsonResponse({"status": "failed",
                             "error": "{}不存在".format(corporatename),
                             "code": '500'})
    except  Exception as e :
        log.info("error is :".format(str(e)))
        return JsonResponse({"status": "failed",
                             "error": str(e),
                             "code": '500'})










