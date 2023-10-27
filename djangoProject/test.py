from datetime import datetime, timedelta,date
import random

import django

from ctptypublicinfo.views import publicinfoflow
from djangoProject import models
import cx_Oracle
import os
from django.db import connection
from djangoProject.models import OtcDerivativeCounterparty, AmlCounterparty, AmlBeneficiary
from django.utils import log
os.environ.setdefault("DJANGO_SETTINGS_MODULE","settings")
django.setup()


def getid() -> str:
    char = ''
    str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(32):
        char += random.choice(str)
    log.info('Detail.ID={0}'.format(char))
    return char


def getidno():
    char = ''
    str = '0123456789'
    for i in range(18):
        char += random.choice(str)
    return char

def add_Beneficiary(corporatename):

        try :
            date = datetime.today() - timedelta(days=30)
            id_validdate_end = datetime.strftime(date,'%Y-%m-%d')
            log.info('流程发起时间:{}'.format(id_validdate_end))
            #......
            #进行流操作兼容超大数据处理

            # ......
            #判断原来是否有受益人和法定代表人
            clientidList = [client['client_id'] for client in models.OtcDerivativeCounterparty.objects.filter(corporate_name=corporatename).all().values('client_id')]
            unifiedsocialcode = [code["unifiedsocial_code"] for code in models.CounterpartyOrg.objects.filter(corporate_name=corporatename).all().values("unifiedsocial_code")]
            print(unifiedsocialcode)
            #筛选出没有Amlcounterparty中的对象
            noncounterpartList = list(filter(lambda client : len(models.AmlCounterparty.objects.filter(client_id=client).values())==0,clientidList))
            print(noncounterpartList)
#添加counaterparty和受益人
            # if  len(noncounterpartList)!=0 :
            if noncounterpartList :
                for tmp in noncounterpartList:
                    log.info(tmp)
                    prodname = [prod['signature_name'] for prod in models.OtcDerivativeCounterparty.objects.filter(client_id=tmp).values()]
                    print(prodname[0])
                    counterparty = AmlCounterparty(id=getid(),
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
                                                   prodname=prodname[0] if prodname else None )
                    counterparty.save()
                    id = [id["id"] for id in models.AmlCounterparty.objects.filter(client_id=tmp).values("id")]
                    print(id)
                    beneificiary = AmlBeneficiary(name='回访9527',
                                                  id = getid(),
                                                  id_no=getidno(),
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
            else :
                existscounterpartyid = [id["id"] for id in models.AmlCounterparty.objects.filter(client_id__in=clientidList).values()]
                print('1')
                existbeneficiary = list(filter(lambda x : len(models.AmlBeneficiary.objects.filter(counterparty_id=x,category='1'))!=0,existscounterpartyid))
                log.info("输出existbeneficiary")
                print(existbeneficiary)
                nonexistbeneficiary = list(filter(lambda  y: y not in existbeneficiary,existscounterpartyid))

                models.AmlBeneficiary.objects.filter(counterparty_id__in=existbeneficiary,category='1').update(id_validdate_end=id_validdate_end)
                for abvs in nonexistbeneficiary:
                    log.info(abvs)
                    beneificiary1 = AmlBeneficiary(name='回访9527',
                                                   id=getid(),
                                                  id_no=getidno(),
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
        except Exception as e :
            log.info(str(e))
add_Beneficiary('云合资本管理(北京)有限公司')

#查询操作
#     msg = models.OtcDerivativeCounterparty.objects.values("client_id","corporate_name",
#                                                           "unifiedsocial_code",
#                                                           "abbreviation").filter(corporate_name='测试产品关注类')
#     # 获取查询的 SQL 语句
#     # sql, params = msg.query.sql_with_params()
#     # models.OtcDerivativeCounterparty.objects.all()
#     #
#     for i in msg:
#         print(i)
# #更新操作
#     update_sql = models.OtcDerivativeCounterparty.objects.filter(corporate_name='测试产品关注类').update(aml_monitor_flag='true')
'''
#插入操作
    obj = OtcDerivativeCounterparty(corporate_name='测试产品关注类')
    obj.save()
#删除操作
    models.OtcDerivativeCounterparty.objects.filter(corporate_name='').delete()
'''






