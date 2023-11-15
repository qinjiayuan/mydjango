import datetime
import os
from datetime import date,datetime,timedelta
from random import random

import requests
from django.shortcuts import render
from django.http import  HttpResponse,request,JsonResponse
from djangoProject.models import OtcDerivativeCounterparty,AmlCounterparty,AmlBeneficiary,CrtExpiredRecord
from django.utils import log
import random
from djangoProject import models
from os import environ
ENV = os.environ.get("ENV")
# Create your views here.
class certificates():
    def __init__(self,corporatename,customermanager):
        self.coporatename = corporatename
        self.customermanager = customermanager

    def isExist(self):

        try:

            counterpartyOrg = models.CounterpartyOrg.objects.filter(corporate_name=self.coporatename).values(
                "corporate_name")
            counterparty = models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.coporatename).values(
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

    def getid(self) -> str:

        char = ''
        str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(32):
            char += random.choice(str)
        log.info('Detail.ID={0}'.format(char))
        return char

    def getidno(self):
        char =''
        str  = '0123456789'
        for i in range(18):
            char += random.choice(str)
        return char
    def add_Beneficiary(self,corporatename):

        try:

            date = datetime.today() - timedelta(days=27)
            id_validdate_end = datetime.strftime(date, '%Y-%m-%d')
            log.info('流程发起时间:{}'.format(id_validdate_end))

            # 判断原来是否有受益人和法定代表人
            clientidList = [client['client_id'] for client in
                            models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).all().values(
                                'client_id')]
            unifiedsocialcode = [code["unifiedsocial_code"] for code in
                                 models.CounterpartyOrg.objects.filter(corporate_name=corporatename).all().values(
                                     "unifiedsocial_code")]
            print(unifiedsocialcode)
            # 筛选出没有Amlcounterparty中的对象
            noncounterpartList = list(
                filter(lambda client: len(models.AmlCounterparty.objects.filter(client_id=client).values("client_id")) == 0,
                       clientidList))
            # 添加counaterparty和受益人
            # if  len(noncounterpartList)!=0 :
            if noncounterpartList:
                for tmp in noncounterpartList:
                    log.info(tmp)
                    prodname = [prod['signature_name'] for prod in
                                models.OtcDerivativeCounterparty.objects.filter(client_id=tmp).values()]
                    counterparty = AmlCounterparty(id=self.getid(),
                                                   client_name=corporatename,
                                                   organ_type='0',
                                                   creator='sunbin',
                                                   create_time=date.now(),
                                                   updater='sunbin',
                                                   update_time=date.now(),
                                                   id_no=unifiedsocialcode[0],
                                                   version='1',
                                                   id_kind='business_license',
                                                   client_id=tmp,
                                                   prodname=prodname[0] if prodname else None)
                    counterparty.save()
                    id = [id["id"] for id in models.AmlCounterparty.objects.filter(client_id=tmp).values("id")]
                    beneificiary = AmlBeneficiary(name='回访9527',
                                                  id=self.getid(),
                                                  id_no=self.getidno(),
                                                  id_kind='0',
                                                  birth='1990-10-10',
                                                  gender='Female',
                                                  client_kind='F',
                                                  id_validdate_start='1990-10-10',
                                                  id_validdate_end=id_validdate_end,
                                                  counterparty_id=id[0],
                                                  category='1')
                    log.info("新更改的身份证:{}".format(beneificiary["id"]))
                    beneificiary.save()
                    log.info("受益人添加完成")
            else:
                existscounterpartyid = [id["id"] for id in
                                        models.AmlCounterparty.objects.filter(client_id__in=clientidList).values("id")]
                existbeneficiary = list(
                    filter(lambda x: len(models.AmlBeneficiary.objects.filter(counterparty_id=x, category='1').values())!= 0,
                           existscounterpartyid))

                nonexistbeneficiary = list(filter(lambda y: y not in existbeneficiary, existscounterpartyid))

                models.AmlBeneficiary.objects.filter(counterparty_id__in=existbeneficiary, category='1').update(
                    id_validdate_end=id_validdate_end)
                #对不存在受益人的进行操作
                for abvs in nonexistbeneficiary:
                    log.info(abvs)
                    beneificiary1 = AmlBeneficiary(name='回访9527',
                                                   id=self.getid(),
                                                   id_no=self.getidno(),
                                                   id_kind='0',
                                                   birth='1990-10-10',
                                                   gender='Female',
                                                   client_kind='F',
                                                   id_validdate_start='1990-10-10',
                                                   id_validdate_end=id_validdate_end,
                                                   counterparty_id=abvs,
                                                   category='1')
                    log.info("新更改的身份证:{}".format(beneificiary1["id"]))
                    beneificiary1.save()
                    log.info("受益人已成功添加")
                for newperson in existbeneficiary :
                    models.AmlBeneficiary.objects.filter(category='1',counterparty_id=newperson).update(name='回访9527',
                                                                                                        id_no=self.getidno(),
                                                                                                        id_validdate_end=id_validdate_end,
                                                                                                        birth='1990-10-10',
                                                                                                        id_validdate_start='1990-10-10')

        except Exception as e:
            log.info(str(e))






def startjob(request):
    corporatename = request.POST.get("corporatename")
    customermanager = request.POST.get("customermanager")
    env = request.POST.get("env")
    enviroment = ENV if env is None or env == '' else ("http://" + env)
    print("corporatename : {} , customermanager : {},env ：{}".format(str(corporatename), str(customermanager),env))
    log.info("env的类型是{}".format(type(env)))
    log.info(enviroment)
    log.info("**********************开始生成证件过期流程**************************")
    try:
        cert = certificates(corporatename, customermanager)
        flag = cert.isExist()
        if flag:
            user, department = cert.iscustomerExist()
            if user is None or department is None:
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")

            # 先处理受益人信息
            cert.add_Beneficiary(corporatename)
            # 更改客户经理
            models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).update(customer_manager=user,
                                                                                                 introduction_department=department)
            # 通过证件来找到在途流程并且进行更改
            counterpartyId = [id["id"] for id in
                              models.AmlCounterparty.objects.filter(client_name=corporatename).all().values("id")]
            log.info("counterpartyId is :{}".format(counterpartyId))
            if counterpartyId:
                idno = [idno["id_no"] for idno in models.AmlBeneficiary.objects.filter(category='1',
                                                                                       counterparty_id__in=counterpartyId,
                                                                                       name='回访9527').values('id_no')]
                recordList = [record['crt_expired_record_id'] for record in
                              models.CrtExpiredPersonRecord.objects.filter(id_no__in=idno).values(
                                  'crt_expired_record_id')]
                models.CrtExpiredRecord.objects.filter(record_id__in=recordList).update(current_status='CLOSED')

            unifiedsocialcode = [item["unifiedsocial_code"] for item in models.OtcDerivativeCounterparty.objects.filter(
                corporate_name=corporatename).all().values("unifiedsocial_code")][0]
            models.CrtExpiredRecord.objects.filter(unifiedsocial_code=unifiedsocialcode).exclude(
                current_status='CLOSED').delete()
            url = enviroment + '/certificates/expired/NATURE_PERSON'
            params = {"checkDate": date.today(),
                      "unifiedsocialCodeList": unifiedsocialcode}
            log.info("request paramas is {}".format(params))
            responsed = requests.post(url=url,
                                      data=params)
            log.info(responsed.json())

            title = {}
            titleList = [title['title'] for title in
                         models.CrtExpiredRecord.objects.filter(unifiedsocial_code=unifiedsocialcode).exclude(
                             current_status__in=['CLOSED', 'CANCELLED']).values("title")]
            log.info("title1 is {}".format(titleList))
            for i in range(len(titleList)):
                title["title{}".format(i + 1)] = titleList[i]
            log.info("流程标题 : {}".format(title))
            log.info("****************************证件过期流程已生成*************************")
            return render(request,'result.html',{"data":"发起成功!"})
            # return render(request, 'result.html', {"data":
            #                                                  {"status": "successfully",
            #                                                   "data": title,
            #                                                   "code": '200'}
            #                                              }
            #               )

        else:
            raise ValueError("该机构不存在")
    except Exception as e :
        log.info("error is :".format(str(e)))
        return render(request,'result.html',{"data":str(e)})

def form(request):
    return render(request,'certexpired.html')


def startjob1(request):
    corporatename = request.POST.get("corporatename")
    customermanager = request.POST.get("customermanager")
    env = request.POST.get("env")
    enviroment = ENV if env is None or '' else ("http://" + env)
    print("corporatename : {} , customermanager : {}".format(str(corporatename),str(customermanager)))
    log.info("**********************开始生成证件过期流程**************************")
    try:
        cert = certificates(corporatename,customermanager)
        flag = cert.isExist()
        if flag :
            user , department = cert.iscustomerExist()
            if  user is None or department is None :
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")

           #先处理受益人信息
            cert.add_Beneficiary(corporatename)
            #更改客户经理
            models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).update(customer_manager=user,
                                                                                                 introduction_department=department)
            #通过证件来找到在途流程并且进行更改
            counterpartyId = [id["id"] for id in models.AmlCounterparty.objects.filter(client_name=corporatename).all().values("id")]
            log.info("counterpartyId is :{}".format(counterpartyId))
            if counterpartyId :
                idno = [idno["id_no"] for idno in models.AmlBeneficiary.objects.filter(category='1',
                                                                                       counterparty_id__in=counterpartyId,
                                                                                       name='回访9527').values('id_no')]
                recordList = [record['crt_expired_record_id'] for record in models.CrtExpiredPersonRecord.objects.filter(id_no__in=idno).values('crt_expired_record_id')]
                models.CrtExpiredRecord.objects.filter(record_id__in=recordList).update(current_status='CLOSED')





            unifiedsocialcode = [item["unifiedsocial_code"] for item in models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).all().values("unifiedsocial_code")][0]
            models.CrtExpiredRecord.objects.filter(unifiedsocial_code=unifiedsocialcode).exclude(current_status='CLOSED').delete()
            url = enviroment + '/certificates/expired/NATURE_PERSON'
            params = {"checkDate":date.today(),
                      "unifiedsocialCodeList":unifiedsocialcode}
            log.info("request paramas is {}".format(params))
            responsed = requests.post(url=url,
                                     data=params)
            log.info(responsed.json())

            title = {}
            titleList = [title['title'] for title in models.CrtExpiredRecord.objects.filter(unifiedsocial_code=unifiedsocialcode).exclude(current_status__in=['CLOSED','CANCELLED']).values("title")]
            log.info("title1 is {}".format(title))
            for i in range(len(titleList)):
                title["title{}".format(i+1)] = titleList[i]

            log.info("****************************证件过期流程已生成*************************")
            return JsonResponse({"status":"successfully",
                                 "data":title,
                                 "code":'200'}
                                )

        else:
            return JsonResponse({"status": "failed",
                                 "error": "{}不存在".format(corporatename),
                                 "code": '500'}
                                )
    except Exception as e :
        log.info(str(e))
        return JsonResponse({"status": "failed",
                             "error": str(e),
                             "code": '500'}
                            )