import datetime
from datetime import date,datetime,timedelta
from random import random

from django.shortcuts import render
from django.http import  HttpResponse,request
from djangoProject.models import OtcDerivativeCounterparty,AmlCounterparty,AmlBeneficiary,CrtExpiredRecord
from django.utils import log
import random
from djangoProject import models
# Create your views here.
class certificates():
    def __init__(self,corporatename,customermanager):
        self.coporatename = corporatename
        self.customermanager = customermanager

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
            date = datetime.today() - timedelta(days=30)
            id_validdate_end = datetime.strftime(date, '%Y-%m-%d')
            log.info('流程发起时间:{}'.format(id_validdate_end))
            # ......
            # 进行流操作兼容超大数据处理

            # ......
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
                filter(lambda client: len(models.AmlCounterparty.objects.filter(client_id=client).values()) == 0,
                       clientidList))
            print(noncounterpartList)
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
                    beneificiary.save()
                    log.info("受益人添加完成")
            else:
                existscounterpartyid = [id["id"] for id in
                                        models.AmlCounterparty.objects.filter(client_id__in=clientidList).values()]
                existbeneficiary = list(
                    filter(lambda x: len(models.AmlBeneficiary.objects.filter(counterparty_id=x, category='1')) != 0,
                           existscounterpartyid))
                log.info("输出existbeneficiary")
                nonexistbeneficiary = list(filter(lambda y: y not in existbeneficiary, existscounterpartyid))

                models.AmlBeneficiary.objects.filter(counterparty_id__in=existbeneficiary, category='1').update(
                    id_validdate_end=id_validdate_end)
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
                    beneificiary1.save()
            log.info("受益人已成功添加")
        except Exception as e:
            log.info(str(e))






def startjob(request):
    corporatename = request.POST.get("corporatename")
    customermanager = request.POST.get("customermanager")
    print("corporatename : {} , customermanager : {}".format(str(corporatename),str(customermanager)))
    try:
        cert = certificates(corporatename,customermanager)
        flag = cert.isExist()
        if flag :
            user , department = cert.iscustomerExist()
            if  user is None or department is None :
                raise ValueError("该客户经理不存在,请输入中文名称且确认该用户存在")

           #先处理受益人信息
            cert.add_Beneficiary()



        else:
            raise ValueError("该机构不存在")
    except Exception as e :
        return render(request,'clientreview.html',{"data":str(e),"code":"500"})
