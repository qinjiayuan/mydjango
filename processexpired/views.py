import os
import jsonpath
from django.shortcuts import render
from django.http import JsonResponse, request, HttpResponse
from djangoProject import models
from datetime  import date,datetime,timedelta
import logging
# from django.utils import log
import random,requests
from django.db.models import Q
# #创建到期流程的数据
from djangoProject.models import AmlCounterparty, AmlBeneficiary, CounterpartyBenefitOverList, ClientReviewDetail

ENV = os.environ.get("ENV")

log = logging.getLogger("django.request")

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


class Clientreviewflow():

    def __init__(self, corporateName, customerManager, isnewflow, ):
        self.corporateName = corporateName
        self.customerManager = customerManager
        self.clientIdList = []
        self.isnewflow = isnewflow


    # 判断交易对手是否存在
    def isExist(self):

        try:

            counterpartyOrg = models.CounterpartyOrg.objects.filter(corporate_name=self.corporateName).values(
                "corporate_name")
            counterparty = models.OtcDerivativeCounterparty.objects.filter(corporate_name=self.corporateName).values(
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
        user_list = list(models.Auser.objects.filter(username=self.customerManager).values("userid", "orgid"))

        if not user_list:
            return None, None
        dept_code = list(models.Aorg.objects.filter(orgid=user_list[0]["orgid"]).values("dept_code"))
        department = dept_code[0]["dept_code"]
        customerManager = user_list[0]["userid"]
        return customerManager, department

    # 调用后端接口上传附件获取s3Fileid
    def gets3fileid(self,enviroment):

        file_name = ['主体/管理人文件', '32', 'CSRC', 'QCC_CREDIT_RECORD', 'CEIDN', 'QCC_ARBITRATION', 'QCC_AUDIT_INSTITUTION',
                     'CCPAIMIS', 'CC', 'P2P', 'OTHERS', 'NECIPS', 'CJO']
        s3fileid = []
        url = enviroment + "/clientreview/file/upload"
        headers = {"name": "sunbin"}
        files = {"files": open('D:/djangoProject/clientreview/20220318144757.png', 'rb')}
        for i in range(0, 13):
            json = {"fileBelong": file_name[i], "productName": file_name[i]}
            response = requests.post(url=url,
                                     headers=headers,
                                     json=json,
                                     files=files)
            s3id = jsonpath.jsonpath(response.json(), "$..s3FileId")
            s3fileid.append(s3id[0])
            log.info(response.json())
        log.info("获取s3fileid成功")
        return s3fileid

    def getid(self) -> str:

        char = ''
        str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(32):
            char += random.choice(str)
        log.info('Detail.ID={0}'.format(char))
        return char


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
    def add_Beneficiary(self,corporatename,expired):

        try:
            date=datetime.today() - (timedelta(days=27) if expired == "0" else timedelta(days=31))

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

def certificatesjob(request,corporatename,customermanager,expired,enviroment):

    print("corporatename : {} , customermanager : {}".format(str(corporatename), str(customermanager)))
    log.info("**********************开始生成证件过期流程**************************")
    try:
        cert = certificates(corporatename, customermanager)
        flag = cert.isExist()
        if flag:
            user, department = cert.iscustomerExist()
            if user is None or department is None:
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")

            # 先处理受益人信息
            cert.add_Beneficiary(corporatename,expired)
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
                         models.CrtExpiredRecord.objects.filter(unifiedsocial_code=unifiedsocialcode,
                                                                current_status='PROCESSING').values("title")]
            log.info(titleList)
            for i in range(len(titleList)):
                title["title{}".format(i + 1)] = titleList[i]
            log.info("title is {}".format(title))
            log.info("****************************证件过期流程已生成*************************")
            return JsonResponse({"status": "successfully",
                                 "data": title,
                                 "code": '200'}
                                )

        else:
            return JsonResponse({"status": "failed",
                                 "error": "{}不存在".format(corporatename),
                                 "code": '500'}
                                )
    except Exception as e:
        log.info(str(e))
        return JsonResponse({"status": "failed",
                             "error": str(e),
                             "code": '500'}
                            )


def publicinfojob(request,corporatename,customermanager,expired,enviroment):

    try :
        log.info("**************************生成公开信息流程开始******************************")

        public = publicinfoflow(customermanager)
        if public.isExisits():
            customer_manager ,department = public.iscustomerExist()
            print(customer_manager)
            print(department)
            if  customer_manager is None  and department is None   :
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
            #删除存量流程
            unifiledsocialcode = [uni["unifiedsocial_code"] for uni in
                                  models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).values(
                                      "unifiedsocial_code")]
            models.CtptyInfoUpdateRecord.objects.filter(unifiedsocial_code__in=[public.unifiledsocialcode,unifiledsocialcode[0]]).exclude(current_status='CLOSED').delete()
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

            log.info("请求url:{}".format(url))
            log.info("请求参数:{}".format(playload))
            response = requests.post(url=url,
                                     data=playload)
            log.info(response.json())


            # 设置过期时间
            created_datetime = datetime.now() - (timedelta(days=21) if expired == '0' else timedelta(days=31))
            now = datetime.strftime(created_datetime,"20%y-%m-%d")
            log.info("公开信息设置的过期时间是{}".format(now))
            #查出该公司的统一信用代码和公司名称

            client_id = [client['client_id'] for client in models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).values('client_id')]
            titlehead = '客户{0}公开信息发生变更确认流程{1}'.format(corporatename, now)
            #将云合资本变成入参中的公司
            models.CtptyInfoUpdateRecord.objects.filter(Q(unifiedsocial_code='911101080828461726',
                                                          title__contains='云合资本管理(北京)有限公司',
                                                          current_status='PROCESSING')).update(unifiedsocial_code=unifiledsocialcode[0],
                                                                                               created_datetime=now,
                                                                                               title=titlehead,
                                                                                                client_id=client_id[0])
            title = {}
            titleList = [title["title"] for title in models.CtptyInfoUpdateRecord.objects.filter(unifiedsocial_code=unifiledsocialcode[0]).exclude(
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




#直接返回json报文
def reviewjob(request,corporateName,customermanager,expired,enviroment):

    isnew = '1'
    print(corporateName)
    print(customermanager)
    print(isnew)
    reviewflow = Clientreviewflow(corporateName, customermanager, isnew)
    file_name = ['主体/管理人文件', '32', 'CSRC', 'QCC_CREDIT_RECORD', 'CEIDN', 'QCC_ARBITRATION', 'QCC_AUDIT_INSTITUTION',
                 'CCPAIMIS', 'CC', 'P2P', 'OTHERS', 'NECIPS', 'CJO']
    try:
        if reviewflow.isExist():
            user, department = reviewflow.iscustomerExist()
            if user is None or department is None:
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")
            # 删除在途流程
            models.OtcDerivativeCounterparty.objects.filter(corporate_name=reviewflow.corporateName).update(customer_manager=user,
                                                                                                            introduction_department=department)
            record_list = [record["record_id"] for record in
                           models.ClientReviewRecord.objects.filter(client_name=reviewflow.corporateName).exclude(
                               current_status='CLOSED').values("record_id")]
            log.info(record_list)
            log.info("*****************开始生成回访流程*******************")
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
            models.CounterpartyOrg.objects.filter(corporate_name=reviewflow.corporateName).update(
                aml_monitor_flag='true')
            unifiledsocialcode = list(
                models.CounterpartyOrg.objects.filter(corporate_name=reviewflow.corporateName).values(
                    "unifiedsocial_code"))
            procount = models.OtcDerivativeCounterparty.objects.filter(corporate_name=reviewflow.corporateName,
                                                                       is_prod_holder='03').values("client_id")
            orgcount = models.OtcDerivativeCounterparty.objects.filter(corporate_name=reviewflow.corporateName,
                                                                       is_prod_holder='02').values()
            # 设置投资者明细
            clientIdlist = [clientid['client_id'] for clientid in models.OtcDerivativeCounterparty.objects.filter(
                corporate_name=reviewflow.corporateName,
                is_prod_holder='03').values
            ('client_id')]
            for client_id in clientIdlist:
                flag: bool = True if len(
                    models.CounterpartyBenefitOverList.objects.filter(client_id=client_id).all()) else False
                if not flag:
                    info_benefit = CounterpartyBenefitOverList(client_id=client_id,
                                                               name='测试',
                                                               id_no='1928382942342',
                                                               proportion='88',
                                                               professional_investor_flag='1',
                                                               invest_3year_exp_flag='1',
                                                               financial_assets_of_lastyear='1',
                                                               assets_20million_flag='true'
                                                               )
                    info_benefit.save()
            datas = {'checkDateEnd': date.today(),
                     'checkDateStart': date.today(),
                     'uniCodeList': unifiledsocialcode[0]["unifiedsocial_code"]}
            if 1 < len(procount):
                multplurl = enviroment + '/clientreview/checkMultipleClient'

                log.info("请求 url:{}".format(multplurl))
                log.info("paramas is:" + str(datas))
                responese = requests.post(url=multplurl,
                                          data=datas)
                log.info(responese.json())
                log.info("多产品的产品客户回访流程创建成功")
            if 1 <= len(orgcount) or len(procount) == 1:
                singleurl = enviroment + '/clientreview/checkSingleClient'
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
                        sale_person="renyu")
                    for i in range(len(s3fileidList)):
                        models.ClientReviewFileRecord.objects.filter(s3_file_id=s3fileidList[i]).update(
                            record_id=newrecordid,
                            file_belong=file_name[i])
                log.info("**********************生成回访流程结束**************************")
                titleList = [flowid["title"] for flowid in models.ClientReviewRecord.objects.filter(client_name=corporateName,
                                                                                                     current_status__in=['PROCESSING',"TEMPORARY"]).values("title")]
                log.info(titleList)
                # return render(request, 'result.html', {"data": response1.json(), 'code': '200'})
                data = {}
                for i in range(len(titleList)):
                    data["title{}".format(i+1)]=titleList[i]

                flowdate = datetime.now() - (timedelta(days=27) if expired =='0' else timedelta(days=31))
                # limitdate = datetime.strftime(flowdate,"20%y-%m-%d")
                log.info("缓冲期开始时间设置为{}".format(flowdate))
                client_id = [client['client_id'] for client in models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporateName).values('client_id')]
                models.ClientReviewBuffer.objects.filter(client_id__in=client_id).update(review_buffer_start=flowdate)
                return JsonResponse(
                    {"status": "successful",
                     "data": data,
                     "code": "200"}
                )
        # return render(request, 'result.html', {"data": "客户经理或者机构不存在", "code": "500"})


        return JsonResponse({"status":"failed",
                             "error":"客户经理或者机构不存在",
                             "code":"500"})
    except Exception as e:
        log.info("error is {}".format(e))
        # return render(request, 'result.html', {"data": str(e), 'code': '500'})
        return JsonResponse({"status": "failed",
                             "error":str(e),
                             "code":"500"})


def optionjob(request,corporatename,customermanager,expired,enviroment):

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
            now = datetime.now() -  (timedelta(days=27) if expired =='0' else timedelta(days=31))
            models.CounterpartyProdMonitorFlow.objects.filter(corporate_name=corporatename,
                                                              current_status__in=['PROCESSING','TEMPORARY']).update(created_datetime=now)
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



def startjob(request):
    try:
        job_type = {'CLIENT_REVIEW': reviewjob,
                    'CTPTY_INFO': publicinfojob,
                    'CERTIFICATES': certificatesjob,
                    'OPTION_PROD_MONITOR': optionjob}
        flow_type = ['CLIENT_REVIEW', 'CTPTY_INFO', 'CERTIFICATES', 'OPTION_PROD_MONITOR']
        response_type = {'CLIENT_REVIEW': '回访',
                         'CTPTY_INFO': "公开信息",
                         'CERTIFICATES': '证件到期',
                         'OPTION_PROD_MONITOR': '期权产品监测'}
        corporateName = request.POST.get('corporatename')
        customermanager = request.POST.get('customermanager')
        expired = request.POST.get("expired")
        env = request.POST.get('env')
        env = ENV if env is None or env == '' else ("http://" + env)
        trigger4ProcessType = request.POST.get("trigger4ProcessType")
        if trigger4ProcessType in flow_type:
            trigger4ProcessType = trigger4ProcessType
        else:
            raise ValueError({
                "error":
                    {"data": "流程类型错误",
                     "code": " 500"}})

        indata = {}
        indata["corporateName"] = corporateName
        indata['customermanager'] = customermanager
        indata['expired'] = expired
        indata['trigger4ProcessType'] = trigger4ProcessType
        log.info("接受到的参数为{}".format(indata))

        if trigger4ProcessType in job_type:
            job = job_type[trigger4ProcessType](request, corporateName, customermanager, expired, env)
        else:
            raise ValueError(
                {"error": {"data": "流程类型错误",
                           "code": " 500"}
                 }
            )
        # 触发下到期提醒
        log.info("*********************开始触发即将到期提醒*********************")
        url = env + "/api/manualTriggerJob/1.0.0/processExpiredRemindJob"
        params = {'trigger4ProcessType': trigger4ProcessType}
        response = requests.post(url=url, data=params)
        log.info(response.json())
        log.info("********************即将到期提醒已触发***********************")
        if trigger4ProcessType in response_type:
            log.info("trigger4ProcessType is {}".format(trigger4ProcessType))
            response = "{}流程生成成功".format(response_type[trigger4ProcessType])

        return render(request,'result.html',{"data":"已成功触发!"})
    except Exception as e :
        log.info("error is {}".format(str(e)))
        return render(request,'result.html',{"data":str(e)})


def form(request):
    return render(request,'processexpired.html')

def processexpiredjob(request):
    try:
        job_type = {'CLIENT_REVIEW': reviewjob,
                    'CTPTY_INFO': publicinfojob,
                    'CERTIFICATES': certificatesjob,
                    'OPTION_PROD_MONITOR': optionjob}
        flow_type = ['CLIENT_REVIEW', 'CTPTY_INFO', 'CERTIFICATES', 'OPTION_PROD_MONITOR']
        response_type = {'CLIENT_REVIEW': '回访',
                         'CTPTY_INFO': "公开信息",
                         'CERTIFICATES': '证件到期',
                         'OPTION_PROD_MONITOR': '期权产品监测'}
        corporateName = request.POST.get('corporatename')
        customermanager = request.POST.get('customermanager')
        expired = request.POST.get("expired")
        env = request.POST.get('env')
        env = ENV if env is None or env == '' else ("http://" + env)
        trigger4ProcessType = request.POST.get("trigger4ProcessType")
        if trigger4ProcessType in flow_type:
            trigger4ProcessType = trigger4ProcessType
        else:
            raise ValueError({
                "error":
                    {"data": "流程类型错误",
                     "code": " 500"}})

        indata = {}
        indata["corporateName"] = corporateName
        indata['customermanager'] = customermanager
        indata['expired'] = expired
        indata['trigger4ProcessType'] = trigger4ProcessType
        log.info("接受到的参数为{}".format(indata))

        if trigger4ProcessType in job_type:
            job = job_type[trigger4ProcessType](request, corporateName, customermanager, expired,env)
        else:
            raise ValueError(
                {"error": {"data": "流程类型错误",
                           "code": " 500"}
                 }
            )
        # 触发下到期提醒
        log.info("*********************开始触发即将到期提醒*********************")
        url = env + "/api/manualTriggerJob/1.0.0/processExpiredRemindJob"
        params = {'trigger4ProcessType': trigger4ProcessType}
        response = requests.post(url=url, data=params)
        log.info(response.json())
        log.info("********************即将到期提醒已触发***********************")
        if trigger4ProcessType in response_type:
            log.info("trigger4ProcessType is {}".format(trigger4ProcessType))
            response = "{}流程生成成功".format(response_type[trigger4ProcessType])

        return JsonResponse({"status": "successfully",
                             "data": response,
                             "code": "200"})

    except Exception as e:
        log.info(str(e))
        return JsonResponse({"status": 'failed',
                             "code": "500",
                             "error": str(e)})