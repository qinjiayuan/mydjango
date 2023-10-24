import datetime
import logging
from datetime import date,datetime
import jsonpath
from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse,request
from django.shortcuts import render
from djangoProject import models
from djangoProject import logger
import requests,json
import random
from django.utils import log
from djangoProject.models import ClientReviewDetail,ClientReviewRecord,ClientReviewFileRecord,ClientReviewCounterparty
from django.http import JsonResponse

# Create your views here.
class Clientreviewflow():

    def __init__(self):
        self.corporateName = '测试产品关注类'
        self.customerManager = '孙滨'
        self.clientIdList=[]
        self.env = "http://10.2.145.216:9090"
        self.isnewflow = '1'
        self.ENV = '216'
    

#判断交易对手是否存在
    def isExist(self) :
        
        try:

            counterpartyOrg = models.CounterpartyOrg.objects.filter(corporate_name=self.corporateName).values("corporate_name")
            counterparty = models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.corporateName).values("corporate_name","client_id")

            if not counterpartyOrg:
                # logging.error("该机构不存在")
               log.info('该机构不存在')
            if not counterparty:
                log.info('该机构不存在')
            return False if ((len(counterparty) == 0) or len(counterpartyOrg) == 0) else True
        except Exception as e:
            log.info("error is {}".format(str(e)))
            return HttpResponse(e)



#查询用户是否存在
    def iscustomerExist(self):
        user_list = list(models.Auser.objects.filter(username=self.customerManager).values("userid","orgid"))
        dept_code = list(models.Aorg.objects.filter(orgid=user_list[0]["orgid"]).values("dept_code"))
        if not user_list or not dept_code:
            return None, None
        department = dept_code[0]["dept_code"]
        customerManager = user_list[0]["userid"]
        return customerManager, department

    # def startjob(self):
    #     file_name = ['主体/管理人文件', '32', 'CSRC', 'QCC_CREDIT_RECORD', 'CEIDN', 'QCC_ARBITRATION', 'QCC_AUDIT_INSTITUTION',
    #                  'CCPAIMIS', 'CC', 'P2P', 'OTHERS', 'NECIPS', 'CJO']
    #
    #     try:
    #
    #         if self.isExist():
    #             user , department = self.iscustomerExist();
    #             if user is None or department is None:
    #                 raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
    #             #删除在途流程
    #             record_list = [record["record_id"] for record in models.ClientReviewRecord.objects.filter(client_name=self.corporateName).exclude(current_status='CLOSED').values("record_id")]
    #             log.info(record_list)
    #             models.ClientReviewCounterparty.objects.filter(record_id__in=record_list).delete()
    #             models.ClientReviewFileRecord.objects.filter(record_id__in=record_list).delete()
    #             models.ClientReviewDetail.objects.filter(record_id__in=record_list).delete()
    #             models.ClientReviewRecord.objects.filter(record_id__in=record_list).delete()
    #             log.info("{}的在途流程已删除".format(self.corporateName))
    #
    #             #设置台账中发起的条件
    #             models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.corporateName).update(return_visit_date=date.today(),
    #                                                                                                       aml_monitor_flag='true',
    #                                                                                                       no_auto_visit='false',
    #                                                                                                       delete_flag='0')
    #             models.CounterpartyOrg.objects.filter(corporate_name=self.corporateName).update(aml_monitor_flag='true')
    #
    #             unifiledsocialcode = list(models.CounterpartyOrg.objects.filter(corporate_name=self.corporateName).values("unifiedsocial_code"))
    #             procount = models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.corporateName,
    #                                                                        is_prod_holder='03').values("client_id")
    #             orgcount = models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.corporateName,
    #                                                                        is_prod_holder='02').values()
    #             if 1 < len(procount):
    #                 multplurl = self.env + '/clientreview/checkMultipleClient'
    #                 datas = {'checkDateEnd':date.today(),
    #                          'checkDateStart':date.today(),
    #                          'uniCodeList':unifiledsocialcode[0]["unifiedsocial_code"]}
    #                 log.info("请求 url:{}".format(multplurl))
    #                 log.info("paramas is:" + str(datas))
    #                 responese = requests.post(url=multplurl,
    #                                           data=datas)
    #                 log.info(responese.json())
    #                 log.info("多产品的产品客户回访流程创建成功")
    #             if 1 <= len(orgcount) or len(procount) ==1 :
    #                 singleurl = self.env + '/clientreview/checkSingleClient'
    #                 response1 = requests.post(url=singleurl,
    #                                           data=datas)
    #                 log.info("请求url：{}".format(singleurl))
    #                 log.info("paramas is {}".format(str(datas)))
    #                 log.info("机构客户或者单产品回访流程创建成功")
    #
    #                 # 查出最新流程的所有recordid
    #                 flow_list = [record['record_id'] for record in models.ClientReviewRecord.objects.filter(client_name=self.corporateName
    #                                                                                                         ).exclude(current_status='CLOSED').values("record_id")]
    #                 log.info('recordid列表:{}'.format(flow_list))
    #                 for newrecordid in flow_list :
    #                     s3fileidList = self.gets3fileid()
    #                     obj = ClientReviewDetail(id=self.getid(),
    #                                              record_id=newrecordid,
    #                                              client_name='11',
    #                                              client_position='老师',
    #                                              email='123@qq.com',
    #                                              phone='13112345678',
    #                                              review_log='123',
    #                                              suitability='N',
    #                                              suitability_log='123',
    #                                              created_datetime=datetime.now())
    #                     obj.save()
    #
    #                     models.ClientReviewCounterparty.objects.filter(record_id__in=flow_list).update(agree_info='Y',
    #                                                                                                    benefit_over_flag='1')
    #                     models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(accounting_firm_name='测试专用',version=None) if self.isnewflow =='0' \
    #                         else models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(accounting_firm_name='测试专用', version='202210')
    #
    #                     models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(sale_person="renyu") if self.ENV =='216' \
    #                         else  models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(sale_person="renyu")
    #
    #
    #
    #                     for i in range(len(s3fileidList)):
    #                         models.ClientReviewFileRecord.objects.filter(s3_file_id=s3fileidList[i]).update(record_id=newrecordid,
    #                                                                                                         file_belong=file_name[i])
    #                 return JsonResponse({"date":response1,'code':'200'})
    #
    #     except Exception as e :
    #         log.info("error is {}".format(e))
    #         return JsonResponse({"error":str(e),'code':'500'})



#调用后端接口上传附件获取s3Fileid
    def gets3fileid(self):
        log = logger.logger()
        file_name = ['主体/管理人文件', '32', 'CSRC', 'QCC_CREDIT_RECORD', 'CEIDN', 'QCC_ARBITRATION', 'QCC_AUDIT_INSTITUTION',
                     'CCPAIMIS', 'CC', 'P2P', 'OTHERS', 'NECIPS', 'CJO']
        s3fileid = []
        url = self.env +"/clientreview/file/upload"
        headers = {"name":"sunbin"}
        files = {"files": open('D:/djangoProject/clientreview/20220318144757.png', 'rb')}
        for i in range(0,13):
            json = {"fileBelong":file_name[i],"productName":file_name[i]}
            response = requests.post(url=url,
                                     headers=headers,
                                     json=json,
                                     files=files)
            s3id = jsonpath.jsonpath(response.json(),"$..s3FileId")
            s3fileid.append(s3id[0])
            log.info(response.json())
        log.info("获取s3fileid成功")
        return s3fileid

    def getid(self) -> str:
        log = logger.logger()
        char = ''
        str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(32):
            char += random.choice(str)
        log.info('Detail.ID={0}'.format(char))
        return char

def startjob(request):
        reviewflow = Clientreviewflow()
        file_name = ['主体/管理人文件', '32', 'CSRC', 'QCC_CREDIT_RECORD', 'CEIDN', 'QCC_ARBITRATION', 'QCC_AUDIT_INSTITUTION',
                     'CCPAIMIS', 'CC', 'P2P', 'OTHERS', 'NECIPS', 'CJO']

        try:

            if reviewflow.isExist():
                user, department = reviewflow.iscustomerExist();
                if user is None or department is None:
                    raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
                # 删除在途流程
                record_list = [record["record_id"] for record in
                               models.ClientReviewRecord.objects.filter(client_name=reviewflow.corporateName).exclude(
                                   current_status='CLOSED').values("record_id")]
                log.info(record_list)
                models.ClientReviewCounterparty.objects.filter(record_id__in=record_list).delete()
                models.ClientReviewFileRecord.objects.filter(record_id__in=record_list).delete()
                models.ClientReviewDetail.objects.filter(record_id__in=record_list).delete()
                models.ClientReviewRecord.objects.filter(record_id__in=record_list).delete()
                log.info("{}的在途流程已删除".format(reviewflow.corporateName))

                # 设置台账中发起的条件
                models.OtcDerivativeCounterparty.objects.filter(corporate_name=reviewflow.corporateName).update(
                    return_visit_date=date.today(),
                    aml_monitor_flag='true',
                    no_auto_visit='false',
                    delete_flag='0')
                models.CounterpartyOrg.objects.filter(corporate_name=reviewflow.corporateName).update(aml_monitor_flag='true')

                unifiledsocialcode = list(
                    models.CounterpartyOrg.objects.filter(corporate_name=reviewflow.corporateName).values(
                        "unifiedsocial_code"))
                procount = models.OtcDerivativeCounterparty.objects.filter(corporate_name=reviewflow.corporateName,
                                                                           is_prod_holder='03').values("client_id")
                orgcount = models.OtcDerivativeCounterparty.objects.filter(corporate_name=reviewflow.corporateName,
                                                                           is_prod_holder='02').values()
                if 1 < len(procount):
                    multplurl = reviewflow.env + '/clientreview/checkMultipleClient'
                    datas = {'checkDateEnd': date.today(),
                             'checkDateStart': date.today(),
                             'uniCodeList': unifiledsocialcode[0]["unifiedsocial_code"]}
                    log.info("请求 url:{}".format(multplurl))
                    log.info("paramas is:" + str(datas))
                    responese = requests.post(url=multplurl,
                                              data=datas)
                    log.info(responese.json())
                    log.info("多产品的产品客户回访流程创建成功")
                if 1 <= len(orgcount) or len(procount) == 1:
                    singleurl = reviewflow.env + '/clientreview/checkSingleClient'
                    response1 = requests.post(url=singleurl,
                                              data=datas)
                    log.info("请求url：{}".format(singleurl))
                    log.info("paramas is {}".format(str(datas)))
                    log.info("机构客户或者单产品回访流程创建成功")

                    # 查出最新流程的所有recordid
                    flow_list = [record['record_id'] for record in
                                 models.ClientReviewRecord.objects.filter(client_name=reviewflow.corporateName
                                                                          ).exclude(current_status='CLOSED').values(
                                     "record_id")]
                    log.info('recordid列表:{}'.format(flow_list))
                    for newrecordid in flow_list:
                        s3fileidList = reviewflow.gets3fileid()
                        obj = ClientReviewDetail(id=reviewflow.getid(),
                                                 record_id=newrecordid,
                                                 client_name='11',
                                                 client_position='老师',
                                                 email='123@qq.com',
                                                 phone='13112345678',
                                                 review_log='123',
                                                 suitability='N',
                                                 suitability_log='123',
                                                 created_datetime=datetime.now())
                        obj.save()

                        models.ClientReviewCounterparty.objects.filter(record_id__in=flow_list).update(agree_info='Y',
                                                                                                       benefit_over_flag='1')
                        models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(
                            accounting_firm_name='测试专用', version=None) if reviewflow.isnewflow == '0' \
                            else models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(
                            accounting_firm_name='测试专用', version='202210')

                        models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(
                            sale_person="renyu") if reviewflow.ENV == '216' \
                            else models.ClientReviewRecord.objects.filter(record_id=newrecordid).update(
                            sale_person="renyu")

                        for i in range(len(s3fileidList)):
                            models.ClientReviewFileRecord.objects.filter(s3_file_id=s3fileidList[i]).update(
                                record_id=newrecordid,
                                file_belong=file_name[i])
                    return JsonResponse({"date": response1, 'code': '200'})

        except Exception as e:
            log.info("error is {}".format(e))
            return JsonResponse({"error": str(e), 'code': '500'})

# if __name__ == '__main__':
#     a = Clientreviewflow()
#     a .startjob()










