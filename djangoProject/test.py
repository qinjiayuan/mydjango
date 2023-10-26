import django

from ctptypublicinfo.views import publicinfoflow
from djangoProject import models
import cx_Oracle
import os
from django.db import connection
from djangoProject.models import OtcDerivativeCounterparty

os.environ.setdefault("DJANGO_SETTINGS_MODULE","settings")
# django.setup()


def startjob():
    # customermanager = request.POST.get("customermanager")
    customermanager = 'sunbin'
    public = publicinfoflow(customermanager)

    # 删除存量流程
    models.CtptyInfoUpdateRecord.objects.filter(unifiedsocial_code=public.unifiledsocialcode).exclude(
        current_status='CLOSED').delete()
    last_client_id = list(models.OtcDerivativeCounterparty.objects.filter(unifiedsocial_code='911101080828461726',
                                                                          corporate_name='云合资本管理(北京)有限公司').all().values(
        'client_id'))
    last = [client['client_id'] for client in models.OtcDerivativeCounterparty.objects.filter(unifiedsocial_code='911101080828461726',
                                                                          corporate_name='云合资本管理(北京)有限公司').all().values('client_id')]
    print(last_client_id)
    print(last)


if __name__ == '__main__':
    startjob()

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






