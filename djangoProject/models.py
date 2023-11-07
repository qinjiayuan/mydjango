# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
import django
# django.setup()
class AmlBeneficiary(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    entity_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.TextField(unique=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    id_kind = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_no = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    birth = models.TextField(blank=True, null=True)  # This field type is a guess.
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_validdate_start = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_validdate_end = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    mobile = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    hold_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    special_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    hold_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    beneficiary_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    locked = models.TextField(blank=True, null=True)  # This field type is a guess.
    counterparty_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.IntegerField(blank=True, null=True)
    client_kind = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AML_BENEFICIARY'



class AmlCounterparty(models.Model):
    id = models.TextField(primary_key=True,db_index=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    client_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    organ_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    capital_account = models.TextField(blank=True, null=True)  # This field type is a guess.
    creator = models.TextField(blank=True, null=True)  # This field type is a guess.
    create_time = models.DateField(blank=True, null=True)  # This field type is a guess.
    updater = models.TextField(blank=True, null=True)  # This field type is a guess.
    update_time = models.DateField(blank=True, null=True)  # This field type is a guess.
    id_no = models.TextField(unique=True)  # This field type is a guess.
    prodname = models.TextField(blank=True, null=True)  # This field type is a guess.
    remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    creator_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    updater_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.IntegerField(blank=True, null=True)
    id_kind = models.TextField(unique=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AML_COUNTERPARTY'


class Aorg(models.Model):
    orgid = models.TextField(primary_key=True)  # This field type is a guess.
    parentid = models.TextField(blank=True, null=True)  # This field type is a guess.
    orgname = models.TextField(blank=True, null=True)  # This field type is a guess.
    orgtype = models.TextField(blank=True, null=True)  # This field type is a guess.
    orglevel = models.IntegerField(blank=True, null=True)
    o = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    creator = models.TextField(blank=True, null=True)  # This field type is a guess.
    createtime = models.DateTimeField(blank=True, null=True)
    modifier = models.TextField(blank=True, null=True)  # This field type is a guess.
    modifytime = models.DateTimeField(blank=True, null=True)
    leader_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    dept_code = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AORG'



class Auser(models.Model):
    userid = models.TextField(primary_key=True)  # This field type is a guess.
    username = models.TextField(blank=True, null=True)  # This field type is a guess.
    adminid = models.TextField(blank=True, null=True)  # This field type is a guess.
    orgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    password = models.TextField(unique=True)  # This field type is a guess.
    stamppassword = models.TextField(blank=True, null=True)  # This field type is a guess.
    userlevel = models.BooleanField(unique=True)
    isleader = models.NullBooleanField()
    expireddate = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    expired = models.NullBooleanField()
    logintime = models.DateTimeField(blank=True, null=True)
    loginip = models.TextField(blank=True, null=True)  # This field type is a guess.
    lasttime = models.DateTimeField(blank=True, null=True)
    lastip = models.TextField(blank=True, null=True)  # This field type is a guess.
    skin = models.TextField(blank=True, null=True)  # This field type is a guess.
    ipconfig = models.TextField(blank=True, null=True)  # This field type is a guess.
    langcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    usertype = models.TextField(blank=True, null=True)  # This field type is a guess.
    postid = models.IntegerField(blank=True, null=True)
    sex = models.NullBooleanField()
    birthday = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    idcard = models.TextField(blank=True, null=True)  # This field type is a guess.
    school = models.TextField(blank=True, null=True)  # This field type is a guess.
    graduation = models.IntegerField(blank=True, null=True)
    degree = models.IntegerField(blank=True, null=True)
    major = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    province = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.TextField(blank=True, null=True)  # This field type is a guess.
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    postcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    fax = models.TextField(blank=True, null=True)  # This field type is a guess.
    mobile = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    creator = models.TextField(blank=True, null=True)  # This field type is a guess.
    createtime = models.DateTimeField(blank=True, null=True)
    modifier = models.TextField(blank=True, null=True)  # This field type is a guess.
    modifytime = models.DateTimeField(blank=True, null=True)
    erpid = models.TextField(blank=True, null=True)  # This field type is a guess.
    superiorleader = models.TextField(blank=True, null=True)  # This field type is a guess.
    post = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AUSER'


class BeneficiaryOrg(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    entity_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    category = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_kind = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_no = models.TextField(blank=True, null=True)  # This field type is a guess.
    birth = models.TextField(blank=True, null=True)  # This field type is a guess.
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    country = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_validdate_start = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_validdate_end = models.TextField(blank=True, null=True)  # This field type is a guess.
    hold_rate = models.TextField(blank=True, null=True)  # This field type is a guess.
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    hold_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    counterparty_org_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    locked = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'BENEFICIARY_ORG'


class ClientReviewBuffer(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    review_start_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    review_buffer_start = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    review_buffer_end = models.DateTimeField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CLIENT_REVIEW_BUFFER'



class ClientReviewCounterparty(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    record_id = models.TextField(unique=True)  # This field type is a guess.
    product_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    ignore = models.TextField(blank=True, null=True)  # This field type is a guess.
    benefit_over_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    agree_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    allow_busi_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_qualify_review = models.TextField(blank=True, null=True)  # This field type is a guess.
    seq = models.BigIntegerField(blank=True, null=True)
    review_buffer_start = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    supplementary_materials_note = models.TextField(blank=True, null=True)  # This field type is a guess.
    show_note = models.TextField(blank=True, null=True)  # This field type is a guess.
    allow_busi_type_his = models.TextField(blank=True, null=True)  # This field type is a guess.
    manual_del_allow_busi_type = models.TextField(blank=True, null=True)  # This field type is a guess.


    class Meta:
        managed = False
        db_table = 'CLIENT_REVIEW_COUNTERPARTY'


class ClientReviewDetail(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    record_id = models.TextField(unique=True)  # This field type is a guess.
    client_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_position = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    review_log = models.TextField(blank=True, null=True)
    suitability = models.CharField(max_length=1, blank=True, null=True)
    suitability_log = models.TextField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CLIENT_REVIEW_DETAIL'



class ClientReviewFileRecord(models.Model):
    s3_file_id = models.TextField(primary_key=True)  # This field type is a guess.
    otc_derivative_counterparty_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    record_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    file_name = models.TextField(unique=True)  # This field type is a guess.
    file_size = models.FloatField(unique=True)
    file_belong = models.TextField(blank=True, null=True)  # This field type is a guess.
    upload_activity = models.TextField(unique=True)  # This field type is a guess.
    created_user = models.TextField(unique=True)  # This field type is a guess.
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CLIENT_REVIEW_FILE_RECORD'


class ClientReviewRecord(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    doc_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    unifiedsocial_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    review_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    review_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    review_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_activity_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    record_id = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    work_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level_detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level_reason = models.TextField(blank=True, null=True)  # This field type is a guess.
    sale_person = models.TextField(blank=True, null=True)  # This field type is a guess.
    review_term = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    review_process_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    special_mentioned_customer = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_more_review = models.TextField(blank=True, null=True)  # This field type is a guess.
    accounting_firm_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    supplementary_materials_time = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    supplementary_materials = models.TextField(blank=True, null=True)  # This field type is a guess.
    reach_to_03_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    serial_number = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CLIENT_REVIEW_RECORD'


class CounterpartyOrg(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    corporate_name = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    unifiedsocial_code = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    id_kind = models.TextField(blank=True, null=True)  # This field type is a guess.
    secondray_trader_client = models.TextField(blank=True, null=True)  # This field type is a guess.
    secondray_trader = models.TextField(blank=True, null=True)  # This field type is a guess.
    industry = models.TextField(blank=True, null=True)  # This field type is a guess.
    scope_business = models.TextField(blank=True, null=True)  # This field type is a guess.
    list_attribute = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    end_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    capital_attribute = models.TextField(blank=True, null=True)  # This field type is a guess.
    nature = models.TextField(blank=True, null=True)  # This field type is a guess.
    aptitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    nontaxresident = models.TextField(blank=True, null=True)  # This field type is a guess.
    register_country = models.TextField(blank=True, null=True)  # This field type is a guess.
    registered_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    office_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    setup_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    registered_capital = models.FloatField(blank=True, null=True)
    client_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    create_time = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    create_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    update_time = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    update_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    audit_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    organ_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    introduction_department = models.TextField(blank=True, null=True)  # This field type is a guess.
    customer_manager = models.TextField(blank=True, null=True)  # This field type is a guess.
    aml_monitor_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    lastest_client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    concern_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    register_province = models.TextField(blank=True, null=True)  # This field type is a guess.
    register_city = models.TextField(blank=True, null=True)  # This field type is a guess.
    issuing_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    big_client = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'COUNTERPARTY_ORG'



class CounterpartyProdMonitorFlow(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    document_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    corporate_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    unifiedsocial_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    review_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    current_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_activity_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    work_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level_detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level_reason = models.TextField(blank=True, null=True)  # This field type is a guess.
    bpm_doc_no = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    handle_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'COUNTERPARTY_PROD_MONITOR_FLOW'


class CrtExpiredRecord(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    doc_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(unique=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    check_date = models.DateTimeField(unique=True)  # This field type is a guess.
    current_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_activity_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    record_id = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    remind_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    access_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    editable_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    work_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level_detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level_reason = models.TextField(blank=True, null=True)  # This field type is a guess.
    has_stock_trading = models.CharField(max_length=1, blank=True, null=True)
    unifiedsocial_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    version = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CRT_EXPIRED_RECORD'



class CtptyInfoUpdateRecord(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    doc_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    title = models.TextField(unique=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    check_date = models.DateTimeField(unique=True)  # This field type is a guess.
    current_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_activity_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    record_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    access_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    editable_user = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    work_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    security_level_detail = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    urgency_level_reason = models.TextField(blank=True, null=True)  # This field type is a guess.
    unifiedsocial_code = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CTPTY_INFO_UPDATE_RECORD'

class CrtExpiredRecordUnion(models.Model):
    id = models.TextField(primary_key=True)
    client_id = models.TextField(null=True,blank=True)
    crt_expired_record_id = models.TextField(null=True,blank=True,db_index=True)
    create_time = models.DateTimeField(null=True,blank=True)

    class  Meta:
        managed =False
        db_table = 'CRT_EXPIRED_RECORD_UNION'


class OtcDerivativeCounterparty(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    corporate_name = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    abbreviation = models.TextField(blank=True, null=True)  # This field type is a guess.
    name_abbreviation = models.TextField(blank=True, null=True)  # This field type is a guess.
    organization_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    registered_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    office_address = models.TextField(blank=True, null=True)  # This field type is a guess.
    scope_business = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    end_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    limited_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    major_mechanism = models.TextField(blank=True, null=True)  # This field type is a guess.
    nature = models.TextField(blank=True, null=True)  # This field type is a guess.
    aptitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    list_attribute = models.TextField(blank=True, null=True)  # This field type is a guess.
    capital_attribute = models.TextField(blank=True, null=True)  # This field type is a guess.
    investment_varieties = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_contactman = models.TextField(blank=True, null=True)  # This field type is a guess.
    actual_controller = models.TextField(blank=True, null=True)  # This field type is a guess.
    legal_person = models.TextField(blank=True, null=True)  # This field type is a guess.
    professional_investors = models.TextField(blank=True, null=True)  # This field type is a guess.
    mobile_phone = models.TextField(blank=True, null=True)  # This field type is a guess.
    unifiedsocial_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    signature_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    master_agreement_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    agreement_signing_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    audit_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_b_contact = models.TextField(blank=True, null=True)  # This field type is a guess.
    our_contractual_side = models.TextField(blank=True, null=True)  # This field type is a guess.
    credit_rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    protocol_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    nontaxresident = models.TextField(blank=True, null=True)  # This field type is a guess.
    risk_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    termof_investment = models.TextField(blank=True, null=True)  # This field type is a guess.
    expected_income = models.CharField(max_length=500, blank=True, null=True)
    report_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    introduction_department = models.TextField(blank=True, null=True)  # This field type is a guess.
    customer_manager = models.TextField(blank=True, null=True)  # This field type is a guess.
    net_trading = models.TextField(blank=True, null=True)  # This field type is a guess.
    performance_protocol_sign_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    classification_rating = models.TextField(blank=True, null=True)  # This field type is a guess.
    shareholder_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    host_department = models.TextField(blank=True, null=True)  # This field type is a guess.
    fax_tel = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_credited = models.TextField(blank=True, null=True)  # This field type is a guess.
    updater = models.TextField(blank=True, null=True)  # This field type is a guess.
    update_time = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    aml_risk_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    registered_capital = models.FloatField(blank=True, null=True)
    is_prod_holder = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True,db_index=True)  # This field type is a guess.
    client_qualify_review = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_qualify_review_des = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    allow_option_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    delete_flag = models.CharField(max_length=1, blank=True, null=True)
    master_agreement_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    supplement_agreement_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    valid_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    invalid_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    secondray_trader_client = models.TextField(blank=True, null=True)  # This field type is a guess.
    secondray_trader = models.TextField(blank=True, null=True)  # This field type is a guess.
    prod_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    advisor_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    advisor_cert_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    advisor_cert_no = models.TextField(blank=True, null=True)  # This field type is a guess.
    ecif_cust_no = models.TextField(blank=True, null=True)  # This field type is a guess.
    setup_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    industry = models.TextField(blank=True, null=True)  # This field type is a guess.
    return_visit_date = models.DateField(blank=True, null=True)  # This field type is a guess.
    return_visit_data_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    extran_proscale_ratio = models.FloatField(blank=True, null=True)
    margin_balance = models.FloatField(blank=True, null=True)
    product_estab_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    payee_min_transfer_amount = models.FloatField(blank=True, null=True)
    payer_min_transfer_amount = models.FloatField(blank=True, null=True)
    client_coefficient = models.FloatField(blank=True, null=True)
    op_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    put_take_balance = models.FloatField(blank=True, null=True)
    guarantee_agreement_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execute_price_precision = models.FloatField(blank=True, null=True)
    block_price_precision = models.FloatField(blank=True, null=True)
    initial_price_precision = models.FloatField(blank=True, null=True)
    final_price_precision = models.FloatField(blank=True, null=True)
    create_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    create_time = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    audit_status_bak = models.TextField(blank=True, null=True)  # This field type is a guess.
    stamp_count = models.IntegerField(blank=True, null=True)
    stamp_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    stamp_first_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    master_agreement_id_both = models.TextField(blank=True, null=True)  # This field type is a guess.
    supplement_agreement_id_both = models.TextField(blank=True, null=True)  # This field type is a guess.
    fill_role = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    master_agreement_file_path = models.TextField(blank=True, null=True)  # This field type is a guess.
    supplement_agreement_file_path = models.TextField(blank=True, null=True)  # This field type is a guess.
    signed_product_file_path = models.TextField(blank=True, null=True)  # This field type is a guess.
    rpt_prodcode = models.TextField(blank=True, null=True)  # This field type is a guess.
    guarantee_agrmt_file_path = models.TextField(blank=True, null=True)  # This field type is a guess.
    commission_rate = models.FloatField(blank=True, null=True)
    allow_busi_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    partial_margin_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    commission_rate_hk = models.FloatField(blank=True, null=True)
    premium_fee_ratio = models.FloatField(blank=True, null=True)
    interest_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    interest_interval = models.TextField(blank=True, null=True)  # This field type is a guess.
    exchange_rate_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    aml_monitor_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    cpty_notional_limit = models.FloatField(blank=True, null=True)
    benefit_over_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    fiid = models.IntegerField(blank=True, null=True)
    hk_fee_rate_us = models.FloatField(blank=True, null=True)
    hk_fee_rate_hk = models.FloatField(blank=True, null=True)
    hk_fixed_rate = models.FloatField(blank=True, null=True)
    related_party_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    related_party_result = models.TextField(blank=True, null=True)  # This field type is a guess.
    register_country = models.TextField(blank=True, null=True)  # This field type is a guess.
    remark = models.TextField(blank=True, null=True)  # This field type is a guess.
    option_duration_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    trs_duration_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    aml_exclude_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_kind = models.TextField(blank=True, null=True)  # This field type is a guess.
    grant_balance = models.FloatField(blank=True, null=True)
    grant_balance_expire_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    margin_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    concern_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    prod_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    prod_end_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    ab_futures_premium_rate = models.FloatField(blank=True, null=True)
    ab_futures_level_factor = models.FloatField(blank=True, null=True)
    prod_type_other = models.TextField(blank=True, null=True)  # This field type is a guess.
    spread = models.FloatField(blank=True, null=True)
    lei_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_protocol = models.TextField(blank=True, null=True)  # This field type is a guess.
    public_related = models.TextField(blank=True, null=True)  # This field type is a guess.
    public_stock_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    introduction_operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_qualify_review_reason = models.TextField(blank=True, null=True)  # This field type is a guess.
    prod_public_related = models.TextField(blank=True, null=True)  # This field type is a guess.
    prod_public_stock_code = models.TextField(blank=True, null=True)  # This field type is a guess.
    exchange_report_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    chat_room_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_auto_visit = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_report_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    department = models.TextField(blank=True, null=True)  # This field type is a guess.
    option_product_quality_reason = models.TextField(blank=True, null=True)  # This field type is a guess.
    his_allow_busi_type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'OTC_DERIVATIVE_COUNTERPARTY'

class CounterpartyBenefitOverList(models.Model):
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_no = models.TextField(blank=True, null=True)  # This field type is a guess.
    proportion = models.FloatField(blank=True, null=True)
    id = models.TextField(primary_key=True)  # This field type is a guess.
    fiid = models.BigIntegerField(blank=True, null=True)
    professional_investor_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    financial_assets_of_lastyear = models.FloatField(blank=True, null=True)
    invest_3year_exp_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    prod_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    assets_20million_flag = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'COUNTERPARTY_BENEFIT_OVER_LIST'

class ProcessExpiredRemind(models.Model):
    id = models.TextField(primary_key=True)  # This field type is a guess.
    process_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    corporate_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    signed_product_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_qualify_review = models.TextField(blank=True, null=True)  # This field type is a guess.
    process_create_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    process_end_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    process_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    master_agreement_date = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    review_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    process_link = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    updated_datetime = models.DateTimeField(blank=True, null=True)  # This field type is a guess.
    expired_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    actual_operator = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    unifiedsocial_code = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PROCESS_EXPIRED_REMIND'
class CrtExpiredPersonRecord(models.Model):
    id =  models.TextField(primary_key=True)
    crt_expired_record_id = models.TextField(blank=False,null=False,db_index=True)
    aml_beneficiary_id = models.TextField(blank=True,null=True)
    file_record_id = models.TextField(blank=True,null=True)
    handle_type = models.TextField(blank=True,null=True)
    otc_deriv_ctpty_id = models.TextField(blank=True,null=True)
    valid_date_start_old = models.TextField(blank=True,null=True)
    valid_date_end_old = models.DateField(blank=True,null=True)
    valid_date_start_new = models.DateField(blank=True,null=True)
    valid_date_end_new = models.DateField(blank=True,null=True)
    created_datetime = models.DateField(blank=True,null=True)
    entity_type = models.TextField(blank=True,null=True)
    name = models.TextField(blank=True,null=True)
    id_kind = models.TextField(blank=True,null=True)
    id_no = models.TextField(blank=True,null=True)
    entity_id = models.TextField(blank=True,null=True)
    category = models.TextField(blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'CRT_EXPIRED_PERSON_RECORD'