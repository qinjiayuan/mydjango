import django

import os
from django.utils import log
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","settings")
# django.setup()




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




if __name__ == '__main__':
    log.debug('这个是什么错误啊')


