# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AqMgmtLoaderQtableG(models.Model):
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    address_field = models.FloatField(db_column='address#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sign = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbs_sign = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_loader_qtable_g'
        unique_together = (('msgid', 'subscriber_field', 'name', 'address_field'),)


class AqMgmtLoaderQtableH(models.Model):
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    address_field = models.FloatField(db_column='address#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dequeue_time = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    dequeue_user = models.CharField(max_length=30, blank=True, null=True)
    propagated_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    retry_count = models.FloatField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)  # This field type is a guess.
    spare = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_loader_qtable_h'
        unique_together = (('msgid', 'subscriber_field', 'name', 'address_field'),)


class AqMgmtLoaderQtableI(models.Model):
    subscriber_field = models.FloatField(db_column='subscriber#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    queue_field = models.FloatField(db_column='queue#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    msg_enq_time = models.DateTimeField()
    msg_step_no = models.FloatField()
    msg_chain_no = models.FloatField()
    msg_local_order_no = models.FloatField()
    msgid = models.TextField()  # This field type is a guess.
    hint = models.TextField(blank=True, null=True)  # This field type is a guess.
    spare = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_loader_qtable_i'
        unique_together = (('subscriber_field', 'name', 'queue_field', 'msg_enq_time', 'msg_step_no', 'msg_chain_no', 'msg_local_order_no', 'msgid'),)


class AqMgmtLoaderQtableL(models.Model):
    msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30, blank=True, null=True)
    address_field = models.FloatField(db_column='address#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dequeue_time = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    dequeue_user = models.CharField(max_length=30, blank=True, null=True)
    flags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_loader_qtable_l'


class AqMgmtLoaderQtableS(models.Model):
    subscriber_id = models.FloatField(primary_key=True)
    queue_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    protocol = models.FloatField(blank=True, null=True)
    subscriber_type = models.FloatField(blank=True, null=True)
    rule_name = models.CharField(max_length=30, blank=True, null=True)
    trans_name = models.CharField(max_length=65, blank=True, null=True)
    ruleset_name = models.CharField(max_length=65, blank=True, null=True)
    negative_ruleset_name = models.CharField(max_length=65, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    deletion_time = models.DateTimeField(blank=True, null=True)
    scn_at_remove = models.FloatField(blank=True, null=True)
    scn_at_add = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_loader_qtable_s'


class AqMgmtLoaderQtableT(models.Model):
    next_date = models.DateTimeField(primary_key=True)
    txn_id = models.CharField(max_length=30)
    msgid = models.TextField()  # This field type is a guess.
    action = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_loader_qtable_t'
        unique_together = (('next_date', 'txn_id', 'msgid'),)


class AqMgmtNotifyQtableG(models.Model):
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    address_field = models.FloatField(db_column='address#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sign = models.TextField(blank=True, null=True)  # This field type is a guess.
    dbs_sign = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_notify_qtable_g'
        unique_together = (('msgid', 'subscriber_field', 'name', 'address_field'),)


class AqMgmtNotifyQtableH(models.Model):
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    address_field = models.FloatField(db_column='address#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dequeue_time = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    dequeue_user = models.CharField(max_length=30, blank=True, null=True)
    propagated_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    retry_count = models.FloatField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)  # This field type is a guess.
    spare = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_notify_qtable_h'
        unique_together = (('msgid', 'subscriber_field', 'name', 'address_field'),)


class AqMgmtNotifyQtableI(models.Model):
    subscriber_field = models.FloatField(db_column='subscriber#', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30)
    queue_field = models.FloatField(db_column='queue#')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    msg_enq_time = models.DateTimeField()
    msg_step_no = models.FloatField()
    msg_chain_no = models.FloatField()
    msg_local_order_no = models.FloatField()
    msgid = models.TextField()  # This field type is a guess.
    hint = models.TextField(blank=True, null=True)  # This field type is a guess.
    spare = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_notify_qtable_i'
        unique_together = (('subscriber_field', 'name', 'queue_field', 'msg_enq_time', 'msg_step_no', 'msg_chain_no', 'msg_local_order_no', 'msgid'),)


class AqMgmtNotifyQtableL(models.Model):
    msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    subscriber_field = models.FloatField(db_column='subscriber#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=30, blank=True, null=True)
    address_field = models.FloatField(db_column='address#', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dequeue_time = models.DateTimeField(blank=True, null=True)
    transaction_id = models.CharField(max_length=30, blank=True, null=True)
    dequeue_user = models.CharField(max_length=30, blank=True, null=True)
    flags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_notify_qtable_l'


class AqMgmtNotifyQtableS(models.Model):
    subscriber_id = models.FloatField(primary_key=True)
    queue_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    protocol = models.FloatField(blank=True, null=True)
    subscriber_type = models.FloatField(blank=True, null=True)
    rule_name = models.CharField(max_length=30, blank=True, null=True)
    trans_name = models.CharField(max_length=65, blank=True, null=True)
    ruleset_name = models.CharField(max_length=65, blank=True, null=True)
    negative_ruleset_name = models.CharField(max_length=65, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    deletion_time = models.DateTimeField(blank=True, null=True)
    scn_at_remove = models.FloatField(blank=True, null=True)
    scn_at_add = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_notify_qtable_s'


class AqMgmtNotifyQtableT(models.Model):
    next_date = models.DateTimeField(primary_key=True)
    txn_id = models.CharField(max_length=30)
    msgid = models.TextField()  # This field type is a guess.
    action = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aq$_mgmt_notify_qtable_t'
        unique_together = (('next_date', 'txn_id', 'msgid'),)


class DbUserPreferences(models.Model):
    target_name = models.CharField(primary_key=True, max_length=256)
    target_type = models.CharField(max_length=64)
    page_name = models.CharField(max_length=64)
    user_name = models.CharField(max_length=64)
    preference_name = models.CharField(max_length=256)
    preference_value = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_user_preferences'
        unique_together = (('target_name', 'target_type', 'page_name', 'user_name', 'preference_name'),)


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True, null=True)
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EmComparisonSummary(models.Model):
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_type = models.CharField(max_length=32, blank=True, null=True)
    job_name = models.CharField(max_length=256, blank=True, null=True)
    template_owner = models.CharField(max_length=256, blank=True, null=True)
    job_owner = models.CharField(max_length=256, blank=True, null=True)
    template_name = models.CharField(max_length=256, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    target_name = models.CharField(max_length=256, blank=True, null=True)
    result = models.CharField(max_length=10, blank=True, null=True)
    area_of_diff = models.CharField(max_length=10, blank=True, null=True)
    apply_option = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'em_comparison_summary'


class EmIpwInfo(models.Model):
    pwd_idx = models.CharField(primary_key=True, max_length=256)
    ipw = models.CharField(max_length=256, blank=True, null=True)
    desc_str = models.CharField(max_length=256, blank=True, null=True)
    pwd_type = models.CharField(max_length=64, blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'em_ipw_info'


class EmPageConditionMetadata(models.Model):
    page_name = models.CharField(primary_key=True, max_length=64)
    condition_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'em_page_condition_metadata'
        unique_together = (('page_name', 'condition_name'),)


class EmPageCustMetadata(models.Model):
    page_name = models.CharField(primary_key=True, max_length=64)
    cust_name = models.CharField(max_length=64)
    def_cust_value = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'em_page_cust_metadata'
        unique_together = (('page_name', 'cust_name'),)


class EmPageCustomConditions(models.Model):
    condition_set_id = models.TextField(primary_key=True)  # This field type is a guess.
    condition_name = models.CharField(max_length=64)
    condition_value = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'em_page_custom_conditions'
        unique_together = (('condition_set_id', 'condition_name'),)


class EmPageCustomizations(models.Model):
    page_name = models.CharField(primary_key=True, max_length=64)
    cust_name = models.CharField(max_length=64)
    cust_value = models.CharField(max_length=64)
    condition_set_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'em_page_customizations'
        unique_together = (('page_name', 'cust_name', 'condition_set_id'),)


class EmdwTraceConfig(models.Model):
    context_type_id = models.IntegerField(primary_key=True)
    context_type = models.CharField(max_length=30)
    trace_level = models.BooleanField()
    create_date = models.DateField()
    last_update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'emdw_trace_config'


class EmdwTraceData(models.Model):
    context_type = models.ForeignKey(EmdwTraceConfig, models.DO_NOTHING)
    context_identifier = models.CharField(max_length=30, blank=True, null=True)
    log_level = models.BooleanField()
    log_timestamp = models.DateTimeField()
    log_message = models.CharField(max_length=1000, blank=True, null=True)
    module = models.CharField(max_length=100, blank=True, null=True)
    oms_host = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emdw_trace_data'


class EsmCollection(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=512)
    value2 = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'esm_collection'
        unique_together = (('ecm_snapshot', 'property', 'value', 'value2'),)


class Eume2EAssocsLookup(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    assoc_guid = models.TextField()  # This field type is a guess.
    is_group = models.FloatField()
    expand_group = models.FloatField()

    class Meta:
        managed = False
        db_table = 'eume2e_assocs_lookup'
        unique_together = (('target_type', 'assoc_guid'),)


class Items(models.Model):
    id = models.BooleanField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class MgmtAdminLicenses(models.Model):
    pack_name = models.CharField(primary_key=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_admin_licenses'


class MgmtAdminMetricThresholds(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    key_value = models.CharField(max_length=256)
    warning_operator = models.FloatField(blank=True, null=True)
    warning_threshold = models.CharField(max_length=256, blank=True, null=True)
    critical_operator = models.FloatField(blank=True, null=True)
    critical_threshold = models.CharField(max_length=256, blank=True, null=True)
    num_occurences = models.FloatField(blank=True, null=True)
    num_warnings = models.FloatField(blank=True, null=True)
    num_criticals = models.FloatField(blank=True, null=True)
    eval_order = models.FloatField(blank=True, null=True)
    fixit_job = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_admin_metric_thresholds'
        unique_together = (('target_guid', 'metric_guid', 'coll_name', 'key_value'),)


class MgmtAgentSecInfo(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    agent_key = models.CharField(max_length=128, blank=True, null=True)
    agent_host = models.CharField(max_length=256, blank=True, null=True)
    agent_seed = models.CharField(max_length=256, blank=True, null=True)
    oms_seed = models.CharField(max_length=256, blank=True, null=True)
    request_status = models.CharField(max_length=30, blank=True, null=True)
    agent_version = models.CharField(max_length=30, blank=True, null=True)
    agent_ewallet = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_agent_sec_info'


class MgmtAllTargetProps(models.Model):
    property_name = models.CharField(primary_key=True, max_length=64)
    property_type = models.CharField(max_length=64)
    property_display_name = models.CharField(max_length=64)
    property_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    required_flag = models.NullBooleanField()
    credential_flag = models.NullBooleanField()
    default_value = models.CharField(max_length=1024, blank=True, null=True)
    computed_flag = models.NullBooleanField()
    read_only_flag = models.NullBooleanField()
    hidden_flag = models.NullBooleanField()
    system_flag = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_all_target_props'
        unique_together = (('property_name', 'property_type'),)


class MgmtAnnotation(models.Model):
    source_obj_type = models.IntegerField()
    source_obj_guid = models.TextField()  # This field type is a guess.
    timestamp = models.DateField()
    annotation_type = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=256, blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_annotation'


class MgmtAruCredentials(models.Model):
    aru_username = models.CharField(max_length=255, blank=True, null=True)
    aru_password = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_credentials'


class MgmtAruFamilyProductMap(models.Model):
    family = models.ForeignKey('MgmtAruProducts', models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey('MgmtAruProducts', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_family_product_map'
        unique_together = (('family', 'product'),)


class MgmtAruLanguages(models.Model):
    language_id = models.IntegerField(primary_key=True)
    nls_language = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_languages'


class MgmtAruOuiComponents(models.Model):
    component_id = models.FloatField(primary_key=True)
    component_name = models.CharField(max_length=256, blank=True, null=True)
    component_release = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_oui_components'


class MgmtAruPlatforms(models.Model):
    platform_id = models.IntegerField(primary_key=True)
    platform_name = models.CharField(max_length=40)
    em_os_name = models.CharField(max_length=64)
    em_os_bitlength = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_platforms'


class MgmtAruProductReleaseMap(models.Model):
    product = models.ForeignKey('MgmtAruProducts', models.DO_NOTHING, primary_key=True)
    release = models.ForeignKey('MgmtAruReleases', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_product_release_map'
        unique_together = (('product', 'release'),)


class MgmtAruProducts(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    em_target_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_products'


class MgmtAruReleases(models.Model):
    release_id = models.IntegerField(primary_key=True)
    release_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mgmt_aru_releases'


class MgmtAuditCustomAttribs(models.Model):
    ca_name = models.CharField(primary_key=True, max_length=256)
    ca_display_name = models.CharField(max_length=256, blank=True, null=True)
    ca_description = models.CharField(max_length=4000, blank=True, null=True)
    ca_required = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_audit_custom_attribs'


class MgmtAuditDestination(models.Model):
    audit_mode = models.NullBooleanField()
    audit_destination = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_audit_destination'


class MgmtAuditLogs(models.Model):
    user_session_id_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    audit_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    op_code = models.FloatField(blank=True, null=True)
    object_name = models.CharField(max_length=4000, blank=True, null=True)
    object_type = models.CharField(max_length=4000, blank=True, null=True)
    object_owner = models.CharField(max_length=4000, blank=True, null=True)
    time_stamp = models.DateField(blank=True, null=True)
    audit_column_value1 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value2 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value3 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value4 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value5 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value6 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value7 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value8 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value9 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value10 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value11 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value12 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value13 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value14 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_value15 = models.CharField(max_length=4000, blank=True, null=True)
    audit_clob_value1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_audit_logs'


class MgmtAuditMaster(models.Model):
    audit_level = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_audit_master'


class MgmtAvailability(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_status = models.FloatField()
    start_collection_timestamp = models.DateField()
    end_collection_timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_availability'
        unique_together = (('target_guid', 'start_collection_timestamp', 'current_status'),)


class MgmtAvailabilityMarker(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    marker_timestamp = models.DateField()
    marker_avail_status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_availability_marker'


class MgmtAvailabilityRbk(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rbk_guid = models.TextField()  # This field type is a guess.
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_status = models.FloatField()
    start_collection_timestamp = models.DateField()
    end_collection_timestamp = models.DateField(blank=True, null=True)
    reason_id = models.FloatField(blank=True, null=True)
    create_timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_availability_rbk'
        unique_together = (('target_guid', 'rbk_guid', 'current_status', 'start_collection_timestamp'),)


class MgmtAvailableSearches(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    classname = models.CharField(max_length=256)
    srch_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_available_searches'
        unique_together = (('target_type', 'classname', 'srch_type'),)


class MgmtBackupConfiguration(models.Model):
    target_guid = models.TextField(unique=True)  # This field type is a guess.
    dbid = models.FloatField(blank=True, null=True)
    autobackuplocation = models.CharField(max_length=128, blank=True, null=True)
    use_disk = models.CharField(max_length=4, blank=True, null=True)
    disk_parallelism = models.FloatField(blank=True, null=True)
    disk_location = models.CharField(max_length=128, blank=True, null=True)
    use_tape = models.CharField(max_length=4, blank=True, null=True)
    tape_parallelism = models.FloatField(blank=True, null=True)
    tape_parms = models.CharField(max_length=1024, blank=True, null=True)
    piece_size_unit = models.CharField(max_length=4, blank=True, null=True)
    max_piece_size = models.FloatField(blank=True, null=True)
    tape_df_copies = models.FloatField(blank=True, null=True)
    tape_al_copies = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_backup_configuration'


class MgmtBamDataHubs(models.Model):
    hub_guid = models.TextField(primary_key=True)  # This field type is a guess.
    hub_name = models.CharField(max_length=64)
    jndi_provider_url = models.CharField(max_length=200)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_data_hubs'


class MgmtBamDataIsessions(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    session_name = models.CharField(max_length=200)
    hub_guid = models.ForeignKey(MgmtBamDataHubs, models.DO_NOTHING, db_column='hub_guid')

    class Meta:
        managed = False
        db_table = 'mgmt_bam_data_isessions'


class MgmtBamDataOsessions(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    session_name = models.CharField(max_length=64)
    users = models.CharField(max_length=200, blank=True, null=True)
    hub_guid = models.ForeignKey(MgmtBamDataHubs, models.DO_NOTHING, db_column='hub_guid')
    message_format = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_data_osessions'


class MgmtBamIsessionDatasource(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    datasource_name = models.CharField(max_length=64)
    ds_namespace = models.CharField(max_length=256, blank=True, null=True)
    jms_topic_connection_factory = models.CharField(max_length=200)
    jms_topic_name = models.CharField(max_length=200)
    jms_subscriber_id = models.CharField(max_length=100, blank=True, null=True)
    jms_username = models.CharField(max_length=64, blank=True, null=True)
    jms_password = models.CharField(max_length=64, blank=True, null=True)
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    source_type = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_isession_datasource'
        unique_together = (('session_guid', 'datasource_name'),)


class MgmtBamIsessionDiag(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    data_type = models.FloatField()
    last_received_timestamp = models.DateField(blank=True, null=True)
    number_received = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_isession_diag'
        unique_together = (('session_guid', 'data_type'),)


class MgmtBamIsessionKpis(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    datasource_name = models.CharField(max_length=64)
    kpi_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_isession_kpis'
        unique_together = (('session_guid', 'datasource_name', 'kpi_name'),)


class MgmtBamOsessionAlerts(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_osession_alerts'
        unique_together = (('session_guid', 'target_guid', 'metric_guid', 'key_value'),)


class MgmtBamOsessionDiag(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    data_type = models.FloatField()
    last_sent_timestamp = models.DateField(blank=True, null=True)
    number_sent = models.FloatField(blank=True, null=True)
    status = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_osession_diag'
        unique_together = (('session_guid', 'data_type'),)


class MgmtBamOsessionMetrics(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_osession_metrics'
        unique_together = (('session_guid', 'target_guid', 'metric_guid', 'key_value'),)


class MgmtBamOsessionStatus(models.Model):
    session_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    last_sent_status = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bam_osession_status'
        unique_together = (('session_guid', 'target_guid'),)


class MgmtBcnAvailDef(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64, blank=True, null=True)
    key_part1 = models.CharField(max_length=256, blank=True, null=True)
    key_part2 = models.CharField(max_length=256, blank=True, null=True)
    key_part3 = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_avail_def'


class MgmtBcnAvailJob(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    insert_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_avail_job'


class MgmtBcnAvailLog(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    availability_status = models.IntegerField()
    collection_timestamp = models.DateField(blank=True, null=True)
    compute_timestamp = models.DateField(blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_avail_log'


class MgmtBcnBcnstepProps(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    step_guid = models.TextField()  # This field type is a guess.
    bcn_guid = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=64)
    string_part = models.FloatField()
    string_value = models.CharField(max_length=4000, blank=True, null=True)
    num_value = models.FloatField(blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    char_value = models.CharField(max_length=1, blank=True, null=True)
    prop_type = models.FloatField()
    encrypted = models.CharField(max_length=1, blank=True, null=True)
    template = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_bcnstep_props'
        unique_together = (('target_guid', 'step_guid', 'bcn_guid', 'name', 'string_part'),)


class MgmtBcnBcntxnProps(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    txn_guid = models.TextField()  # This field type is a guess.
    bcn_guid = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=64)
    string_part = models.FloatField()
    string_value = models.CharField(max_length=4000, blank=True, null=True)
    num_value = models.FloatField(blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    char_value = models.CharField(max_length=1, blank=True, null=True)
    prop_type = models.FloatField()
    encrypted = models.CharField(max_length=1, blank=True, null=True)
    template = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_bcntxn_props'
        unique_together = (('target_guid', 'txn_guid', 'bcn_guid', 'name', 'string_part'),)


class MgmtBcnStepDefn(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    txn_guid = models.TextField()  # This field type is a guess.
    step_guid = models.TextField()  # This field type is a guess.
    step = models.FloatField()
    name = models.CharField(max_length=64)
    step_type = models.CharField(max_length=64)
    parent_step_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_step_defn'
        unique_together = (('target_guid', 'txn_guid', 'step_guid', 'step_type', 'name'),)


class MgmtBcnStepProps(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    step_guid = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=64)
    string_part = models.FloatField()
    string_value = models.CharField(max_length=4000, blank=True, null=True)
    num_value = models.FloatField(blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    char_value = models.CharField(max_length=1, blank=True, null=True)
    prop_type = models.FloatField()
    encrypted = models.CharField(max_length=1, blank=True, null=True)
    template = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_step_props'
        unique_together = (('target_guid', 'step_guid', 'name', 'string_part'),)


class MgmtBcnStepgroupDefn(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    txn_guid = models.TextField()  # This field type is a guess.
    stepgroup_guid = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=64)
    stepgroup_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_stepgroup_defn'
        unique_together = (('target_guid', 'txn_guid', 'stepgroup_guid', 'stepgroup_type', 'name'),)


class MgmtBcnStepgroupSteps(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    txn_guid = models.TextField()  # This field type is a guess.
    stepgroup_guid = models.TextField()  # This field type is a guess.
    step_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_stepgroup_steps'
        unique_together = (('target_guid', 'txn_guid', 'stepgroup_guid', 'step_guid'),)


class MgmtBcnTarget(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    beacon_target_guid = models.TextField()  # This field type is a guess.
    participates_avail = models.CharField(max_length=1)
    is_removing = models.CharField(max_length=1)
    is_local = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_target'
        unique_together = (('target_guid', 'beacon_target_guid'),)


class MgmtBcnTxnAudit(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    txn_guid = models.TextField()  # This field type is a guess.
    audit_timestamp = models.DateField()
    change_type = models.FloatField()
    is_version_change = models.CharField(max_length=1)
    version = models.FloatField(blank=True, null=True)
    details = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_txn_audit'
        unique_together = (('target_guid', 'txn_guid', 'audit_timestamp'),)


class MgmtBcnTxnDefn(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    txn_guid = models.TextField()  # This field type is a guess.
    txn_type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=2000, blank=True, null=True)
    version = models.FloatField()
    modified_date = models.DateField(blank=True, null=True)
    is_representative = models.CharField(max_length=1, blank=True, null=True)
    state = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_txn_defn'
        unique_together = (('target_guid', 'name'), ('target_guid', 'txn_guid', 'txn_type', 'name'),)


class MgmtBcnTxnProps(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    txn_guid = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=64)
    string_part = models.FloatField()
    string_value = models.CharField(max_length=4000, blank=True, null=True)
    num_value = models.FloatField(blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    char_value = models.CharField(max_length=1, blank=True, null=True)
    prop_type = models.FloatField()
    encrypted = models.CharField(max_length=1, blank=True, null=True)
    template = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bcn_txn_props'
        unique_together = (('target_guid', 'txn_guid', 'name', 'string_part'),)


class MgmtBlackoutFlatTargets(models.Model):
    blackout_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    host_blackout = models.NullBooleanField()
    job_status = models.IntegerField(blank=True, null=True)
    blackout_status = models.IntegerField(blank=True, null=True)
    error_message = models.CharField(max_length=2000, blank=True, null=True)
    last_updated_time = models.DateField(blank=True, null=True)
    edit_state = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_flat_targets'
        unique_together = (('blackout_guid', 'target_guid'),)


class MgmtBlackoutHistory(models.Model):
    blackout_guid = models.ForeignKey('MgmtBlackouts', models.DO_NOTHING, db_column='blackout_guid', primary_key=True)
    occurrence_number = models.IntegerField()
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_history'
        unique_together = (('blackout_guid', 'occurrence_number'),)


class MgmtBlackoutProxyTargets(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_proxy_targets'


class MgmtBlackoutReason(models.Model):
    reason_id = models.FloatField(primary_key=True)
    reason = models.CharField(max_length=64)
    reason_nls_id = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_reason'


class MgmtBlackoutSchedule(models.Model):
    blackout_guid = models.TextField(primary_key=True)  # This field type is a guess.
    schedule_index = models.IntegerField()
    frequency_code = models.IntegerField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    execution_hours = models.IntegerField(blank=True, null=True)
    execution_minutes = models.IntegerField(blank=True, null=True)
    interval = models.FloatField(blank=True, null=True)
    months = models.TextField(blank=True, null=True)  # This field type is a guess.
    days = models.TextField(blank=True, null=True)  # This field type is a guess.
    duration = models.FloatField(blank=True, null=True)
    timezone_info = models.NullBooleanField()
    timezone_offset = models.FloatField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    duration_source = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_schedule'
        unique_together = (('blackout_guid', 'schedule_index'),)


class MgmtBlackoutState(models.Model):
    blackout_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    collection_timestamp = models.DateField()
    load_timestamp = models.DateField(blank=True, null=True)
    blackout_code = models.BooleanField()
    target_status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_state'
        unique_together = (('blackout_guid', 'target_guid', 'blackout_code', 'collection_timestamp'),)


class MgmtBlackoutTargetDetails(models.Model):
    blackout_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    include_members = models.NullBooleanField()
    last_updated_time = models.DateField(blank=True, null=True)
    edit_state = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_target_details'
        unique_together = (('blackout_guid', 'target_guid'),)


class MgmtBlackoutWindows(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    end_time = models.DateField(blank=True, null=True)
    start_time = models.DateField()
    utc_start_time = models.DateField(blank=True, null=True)
    utc_end_time = models.DateField(blank=True, null=True)
    blackout_guid = models.TextField(primary_key=True)  # This field type is a guess.
    occurrence_number = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_blackout_windows'
        unique_together = (('blackout_guid', 'target_guid', 'start_time', 'status'),)


class MgmtBlackouts(models.Model):
    blackout_guid = models.TextField(primary_key=True)  # This field type is a guess.
    blackout_name = models.CharField(max_length=64)
    reason_id = models.FloatField(blank=True, null=True)
    blackout_desc = models.CharField(max_length=2000, blank=True, null=True)
    blackout_status = models.IntegerField(blank=True, null=True)
    job_flag = models.NullBooleanField()
    created_by = models.CharField(max_length=256)
    created_thru = models.CharField(max_length=256, blank=True, null=True)
    last_updated_by = models.CharField(max_length=256, blank=True, null=True)
    last_updated_time = models.DateField(blank=True, null=True)
    last_start_time = models.DateField(blank=True, null=True)
    last_end_time = models.DateField(blank=True, null=True)
    scheduled_time = models.DateField(blank=True, null=True)
    start_job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    end_job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    occurrence_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_blackouts'


class MgmtBslnBaselines(models.Model):
    bsln_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_uid = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=1)
    subinterval_key = models.CharField(max_length=8)
    status = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'mgmt_bsln_baselines'
        unique_together = (('target_uid', 'name'),)


class MgmtBslnDatasources(models.Model):
    datasource_guid = models.TextField(primary_key=True)  # This field type is a guess.
    source_type = models.CharField(max_length=2)
    target_uid = models.TextField()  # This field type is a guess.
    metric_uid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    dbid = models.FloatField(blank=True, null=True)
    instance_num = models.FloatField(blank=True, null=True)
    instance_name = models.CharField(max_length=16, blank=True, null=True)
    metric_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bsln_datasources'
        unique_together = (('target_uid', 'metric_uid', 'key_value'),)


class MgmtBslnIntervals(models.Model):
    bsln_guid = models.ForeignKey(MgmtBslnBaselines, models.DO_NOTHING, db_column='bsln_guid')
    interval_begin = models.DateField(blank=True, null=True)
    interval_end = models.DateField(blank=True, null=True)
    interval_days = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bsln_intervals'


class MgmtBslnMetrics(models.Model):
    metric_uid = models.TextField(primary_key=True)  # This field type is a guess.
    tail_estimator = models.CharField(max_length=16)
    threshold_method_default = models.CharField(max_length=16)
    num_occurrences_default = models.FloatField()
    warning_param_default = models.FloatField()
    critical_param_default = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_bsln_metrics'


class MgmtBslnRawdata(models.Model):
    datasource_guid = models.TextField(primary_key=True)  # This field type is a guess.
    obs_time = models.DateField()
    obs_value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_bsln_rawdata'
        unique_together = (('datasource_guid', 'obs_time'),)


class MgmtBslnStatistics(models.Model):
    bsln_guid = models.ForeignKey(MgmtBslnBaselines, models.DO_NOTHING, db_column='bsln_guid')
    datasource_guid = models.ForeignKey(MgmtBslnDatasources, models.DO_NOTHING, db_column='datasource_guid', primary_key=True)
    compute_date = models.DateField()
    subinterval_code = models.TextField()  # This field type is a guess.
    sample_count = models.FloatField()
    average = models.FloatField(blank=True, null=True)
    minimum = models.FloatField(blank=True, null=True)
    maximum = models.FloatField(blank=True, null=True)
    sdev = models.FloatField(blank=True, null=True)
    pctile_25 = models.FloatField(blank=True, null=True)
    pctile_50 = models.FloatField(blank=True, null=True)
    pctile_75 = models.FloatField(blank=True, null=True)
    pctile_90 = models.FloatField(blank=True, null=True)
    pctile_95 = models.FloatField(blank=True, null=True)
    est_sample_count = models.FloatField(blank=True, null=True)
    est_slope = models.FloatField(blank=True, null=True)
    est_intercept = models.FloatField(blank=True, null=True)
    est_fit_quality = models.FloatField(blank=True, null=True)
    est_pctile_99 = models.FloatField(blank=True, null=True)
    est_pctile_999 = models.FloatField(blank=True, null=True)
    est_pctile_9999 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bsln_statistics'
        unique_together = (('datasource_guid', 'compute_date', 'subinterval_code', 'bsln_guid'),)


class MgmtBslnThresholdParms(models.Model):
    bsln_guid = models.ForeignKey(MgmtBslnBaselines, models.DO_NOTHING, db_column='bsln_guid', primary_key=True)
    datasource_guid = models.ForeignKey(MgmtBslnDatasources, models.DO_NOTHING, db_column='datasource_guid')
    threshold_method = models.CharField(max_length=16)
    num_occurrences = models.FloatField()
    warning_param = models.FloatField(blank=True, null=True)
    critical_param = models.FloatField(blank=True, null=True)
    fail_action = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bsln_threshold_parms'
        unique_together = (('bsln_guid', 'datasource_guid'),)


class MgmtBugAdvHomePatch(models.Model):
    advisory_name = models.CharField(primary_key=True, max_length=128)
    bug_number = models.FloatField()
    host_name = models.CharField(max_length=256)
    home_location = models.CharField(max_length=128)
    patch_guid = models.TextField()  # This field type is a guess.
    prereq_release = models.CharField(max_length=256, blank=True, null=True)
    home_location_display = models.CharField(max_length=256, blank=True, null=True)
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    patch_id = models.FloatField()
    patch_release_id = models.FloatField()
    patch_platform_id = models.FloatField()
    container_guid = models.TextField()  # This field type is a guess.
    patch_valid_status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'mgmt_bug_adv_home_patch'
        unique_together = (('advisory_name', 'host_name', 'home_location', 'bug_number', 'patch_guid'),)


class MgmtBugAdvisory(models.Model):
    advisory_name = models.CharField(primary_key=True, max_length=128)
    impact = models.CharField(max_length=128, blank=True, null=True)
    severity = models.FloatField(blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    abstract = models.CharField(max_length=1024, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bug_advisory'


class MgmtBugAdvisoryBug(models.Model):
    bug_number = models.FloatField(primary_key=True)
    advisory_name = models.ForeignKey(MgmtBugAdvisory, models.DO_NOTHING, db_column='advisory_name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bug_advisory_bug'


class MgmtBugAvailablePatch(models.Model):
    ap_guid = models.TextField(primary_key=True)  # This field type is a guess.
    patch_id = models.FloatField(blank=True, null=True)
    product_id = models.FloatField(blank=True, null=True)
    release_id = models.FloatField(blank=True, null=True)
    language_id = models.FloatField(blank=True, null=True)
    patch_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bug_available_patch'
        unique_together = (('patch_id', 'product_id', 'release_id', 'language_id'),)


class MgmtBugFixApplicCompList(models.Model):
    ap_guid = models.ForeignKey('MgmtBugPatchFixesBug', models.DO_NOTHING, db_column='ap_guid')
    bug_number = models.ForeignKey('MgmtBugPatchFixesBug', models.DO_NOTHING, db_column='bug_number')
    component_list_guid = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_bug_fix_applic_comp_list'


class MgmtBugFixApplicableComp(models.Model):
    oui_component_release_id = models.FloatField()
    component_list_guid = models.ForeignKey(MgmtBugFixApplicCompList, models.DO_NOTHING, db_column='component_list_guid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'mgmt_bug_fix_applicable_comp'
        unique_together = (('component_list_guid', 'oui_component_release_id'),)


class MgmtBugPatchCertificate(models.Model):
    patch_id = models.FloatField(primary_key=True)
    release_id = models.FloatField()
    platform_id = models.FloatField()
    product = models.FloatField()
    patch_type = models.CharField(max_length=32)
    certify_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_bug_patch_certificate'
        unique_together = (('patch_id', 'release_id', 'platform_id'),)


class MgmtBugPatchFixesBug(models.Model):
    ap_guid = models.ForeignKey(MgmtBugAvailablePatch, models.DO_NOTHING, db_column='ap_guid', primary_key=True)
    bug_number = models.ForeignKey(MgmtBugAdvisoryBug, models.DO_NOTHING, db_column='bug_number')

    class Meta:
        managed = False
        db_table = 'mgmt_bug_patch_fixes_bug'
        unique_together = (('ap_guid', 'bug_number'),)


class MgmtBugPatchPlatform(models.Model):
    patch_guid = models.TextField(primary_key=True)  # This field type is a guess.
    ap_guid = models.ForeignKey(MgmtBugAvailablePatch, models.DO_NOTHING, db_column='ap_guid')
    platform_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_bug_patch_platform'
        unique_together = (('ap_guid', 'platform_id'),)


class MgmtCallbacks(models.Model):
    callback_type = models.IntegerField()
    callback_name = models.CharField(primary_key=True, max_length=100)
    selector_1 = models.CharField(max_length=64)
    selector_2 = models.CharField(max_length=64)
    selector_3 = models.CharField(max_length=64, blank=True, null=True)
    eval_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_callbacks'
        unique_together = (('callback_name', 'callback_type', 'selector_1', 'selector_2'),)


class MgmtCategories(models.Model):
    class_name = models.CharField(primary_key=True, max_length=64)
    category_name = models.CharField(max_length=64)
    category_name_nlsid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_categories'
        unique_together = (('class_name', 'category_name'),)


class MgmtCategoryClasses(models.Model):
    class_name = models.CharField(primary_key=True, max_length=64)
    class_name_nlsid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_category_classes'


class MgmtCategoryMap(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=8)
    object_guid = models.TextField()  # This field type is a guess.
    class_name = models.CharField(max_length=64)
    category_name = models.CharField(max_length=64)
    object_type = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_category_map'
        unique_together = (('target_type', 'type_meta_ver', 'object_guid', 'class_name'),)


class MgmtChangeAgentUrl(models.Model):
    last_emd_url = models.CharField(primary_key=True, max_length=1024)
    emd_url = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'mgmt_change_agent_url'
        unique_together = (('last_emd_url', 'emd_url'),)


class MgmtCmBaselineConsGroups(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    grantee_name = models.CharField(max_length=30)
    cons_group = models.CharField(max_length=30)
    flag = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_cons_groups'
        unique_together = (('baseline_guid', 'grantee_name', 'cons_group', 'first_version'),)


class MgmtCmBaselineDependencies(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    type = models.FloatField()
    owner = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    referenced_type = models.FloatField()
    referenced_owner = models.CharField(max_length=30)
    referenced_name = models.CharField(max_length=30)
    dependency_type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_dependencies'
        unique_together = (('baseline_guid', 'type', 'owner', 'name', 'referenced_type', 'referenced_owner', 'referenced_name', 'first_version'),)


class MgmtCmBaselineDependents(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    base_object_type = models.FloatField()
    base_object_schema = models.CharField(max_length=30, blank=True, null=True)
    base_object_name = models.CharField(max_length=128)
    dependent_type = models.FloatField()
    hash_value = models.CharField(max_length=32, blank=True, null=True)
    first_version = models.FloatField()
    last_version = models.FloatField()
    definition = models.BinaryField(blank=True, null=True)
    base_object_column = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_dependents'
        unique_together = (('baseline_guid', 'base_object_type', 'base_object_schema', 'base_object_name', 'dependent_type', 'hash_value', 'first_version'),)


class MgmtCmBaselineInitParams(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    param_name = models.CharField(max_length=64)
    param_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_init_params'
        unique_together = (('baseline_guid', 'param_name', 'first_version'),)


class MgmtCmBaselineObjects(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    object_type = models.FloatField()
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=128)
    object_longname = models.TextField(blank=True, null=True)
    last_ddl_time = models.DateField(blank=True, null=True)
    hash_value = models.CharField(max_length=32, blank=True, null=True)
    first_version = models.FloatField()
    last_version = models.FloatField()
    definition = models.BinaryField(blank=True, null=True)
    addnl_info = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_objects'
        unique_together = (('baseline_guid', 'object_type', 'object_schema', 'object_name', 'first_version'),)


class MgmtCmBaselineObjgrants(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    grantee_name = models.CharField(max_length=30)
    obj_owner = models.CharField(max_length=30)
    obj_name = models.CharField(max_length=30)
    col_name = models.CharField(max_length=30, blank=True, null=True)
    grantor_name = models.CharField(max_length=30)
    privilege = models.CharField(max_length=40)
    flag = models.FloatField(blank=True, null=True)
    obj_type = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_objgrants'
        unique_together = (('baseline_guid', 'grantee_name', 'obj_owner', 'obj_name', 'col_name', 'grantor_name', 'privilege', 'first_version'),)


class MgmtCmBaselineProxygrants(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    grantee_name = models.CharField(max_length=30)
    proxy_user = models.CharField(max_length=30)
    direction = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_proxygrants'
        unique_together = (('baseline_guid', 'grantee_name', 'proxy_user', 'first_version'),)


class MgmtCmBaselineQuotagrants(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    grantee_name = models.CharField(max_length=30)
    tablespace = models.CharField(max_length=30)
    maxbytes = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_quotagrants'
        unique_together = (('baseline_guid', 'grantee_name', 'tablespace', 'first_version'),)


class MgmtCmBaselineRolegrants(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    grantee_name = models.CharField(max_length=30)
    rolepriv = models.CharField(max_length=30)
    flag = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_rolegrants'
        unique_together = (('baseline_guid', 'grantee_name', 'rolepriv', 'first_version'),)


class MgmtCmBaselineSysgrants(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    grantee_name = models.CharField(max_length=30)
    privilege = models.CharField(max_length=40)
    flag = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_sysgrants'
        unique_together = (('baseline_guid', 'grantee_name', 'privilege', 'first_version'),)


class MgmtCmBaselineVersions(models.Model):
    baseline_guid = models.ForeignKey('MgmtCmBaselines', models.DO_NOTHING, db_column='baseline_guid')
    baseline_version = models.FloatField()
    capture_time = models.DateField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    db_version = models.CharField(max_length=20, blank=True, null=True)
    job_execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    version_status = models.CharField(max_length=3, blank=True, null=True)
    ddl = models.BinaryField(blank=True, null=True)
    ddl_status = models.FloatField()
    ddl_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baseline_versions'
        unique_together = (('baseline_guid', 'baseline_version'),)


class MgmtCmBaselines(models.Model):
    baseline_guid = models.TextField(primary_key=True)  # This field type is a guess.
    baseline_owner = models.CharField(max_length=30)
    baseline_name = models.CharField(max_length=40)
    baseline_ss = models.TextField()  # This field type is a guess.
    source_id = models.TextField()  # This field type is a guess.
    source_name = models.CharField(max_length=256)
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=2000, blank=True, null=True)
    temp_bl = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cm_baselines'
        unique_together = (('baseline_owner', 'baseline_name'),)


class MgmtCmComparisonInitPrms(models.Model):
    comparison_guid = models.ForeignKey('MgmtCmComparisons', models.DO_NOTHING, db_column='comparison_guid')
    first_version = models.FloatField()
    last_version = models.FloatField()
    param_name = models.CharField(max_length=64)
    state = models.FloatField()
    left_param_value = models.CharField(max_length=4000, blank=True, null=True)
    right_param_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_comparison_init_prms'
        unique_together = (('comparison_guid', 'param_name', 'first_version'),)


class MgmtCmComparisonObjects(models.Model):
    comparison_guid = models.ForeignKey('MgmtCmComparisons', models.DO_NOTHING, db_column='comparison_guid')
    object_type = models.FloatField()
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=128)
    object_longname = models.TextField(blank=True, null=True)
    first_version = models.FloatField()
    last_version = models.FloatField()
    last_left_ddl_time = models.DateField(blank=True, null=True)
    left_hash_value = models.CharField(max_length=32, blank=True, null=True)
    last_right_ddl_time = models.DateField(blank=True, null=True)
    right_hash_value = models.CharField(max_length=32, blank=True, null=True)
    grants_diff_hash = models.CharField(max_length=32, blank=True, null=True)
    state = models.FloatField()
    annotation_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    ignored = models.NullBooleanField()
    differences = models.BinaryField(blank=True, null=True)
    comments_diff_hash = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_comparison_objects'
        unique_together = (('comparison_guid', 'object_type', 'object_schema', 'object_name', 'first_version'),)


class MgmtCmComparisonVersions(models.Model):
    comparison_guid = models.ForeignKey('MgmtCmComparisons', models.DO_NOTHING, db_column='comparison_guid')
    comparison_version = models.FloatField()
    job_execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    version_status = models.CharField(max_length=3, blank=True, null=True)
    left_version = models.FloatField(blank=True, null=True)
    right_version = models.FloatField(blank=True, null=True)
    comparison_time = models.DateField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_comparison_versions'
        unique_together = (('comparison_guid', 'comparison_version'),)


class MgmtCmComparisons(models.Model):
    comparison_guid = models.TextField(primary_key=True)  # This field type is a guess.
    comparison_owner = models.CharField(max_length=30)
    comparison_name = models.CharField(max_length=30)
    comparison_ss = models.TextField()  # This field type is a guess.
    description = models.CharField(max_length=2000, blank=True, null=True)
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    left_type = models.CharField(max_length=1)
    left_id = models.TextField()  # This field type is a guess.
    left_name = models.CharField(max_length=256)
    left_version = models.FloatField(blank=True, null=True)
    right_type = models.CharField(max_length=1)
    right_id = models.TextField()  # This field type is a guess.
    right_name = models.CharField(max_length=256)
    right_version = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_comparisons'
        unique_together = (('comparison_owner', 'comparison_name'),)


class MgmtCmSchemaMaps(models.Model):
    owner_id = models.TextField()  # This field type is a guess.
    left_schema = models.CharField(max_length=30)
    right_schema = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_schema_maps'
        unique_together = (('owner_id', 'left_schema'), ('owner_id', 'right_schema'),)


class MgmtCmScopespecNames(models.Model):
    ss_guid = models.ForeignKey('MgmtCmScopespecs', models.DO_NOTHING, db_column='ss_guid')
    match_types = models.FloatField()
    schema = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=128)
    longname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_scopespec_names'
        unique_together = (('ss_guid', 'match_types', 'schema', 'name'),)


class MgmtCmScopespecs(models.Model):
    ss_guid = models.TextField(primary_key=True)  # This field type is a guess.
    object_types = models.FloatField()
    flags = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_cm_scopespecs'


class MgmtCmSynchImpactReports(models.Model):
    synch_guid = models.ForeignKey('MgmtCmSynchronizations', models.DO_NOTHING, db_column='synch_guid')
    synch_version = models.FloatField()
    message_type = models.CharField(max_length=20)
    message_severity = models.FloatField()
    object_type = models.FloatField(blank=True, null=True)
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=128, blank=True, null=True)
    problem = models.BinaryField(blank=True, null=True)
    action = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_synch_impact_reports'


class MgmtCmSynchObjects(models.Model):
    synch_guid = models.ForeignKey('MgmtCmSynchronizations', models.DO_NOTHING, db_column='synch_guid')
    object_type = models.FloatField()
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=128)
    object_longname = models.TextField(blank=True, null=True)
    first_version = models.FloatField()
    last_version = models.FloatField()
    source_hash_value = models.CharField(max_length=32, blank=True, null=True)
    target_hash_value = models.CharField(max_length=32, blank=True, null=True)
    grants_diff_hash = models.CharField(max_length=32, blank=True, null=True)
    comments_diff_hash = models.CharField(max_length=32, blank=True, null=True)
    addnl_info = models.CharField(max_length=30, blank=True, null=True)
    comp_state = models.FloatField()
    processing_state = models.FloatField()
    sxml_document = models.BinaryField(blank=True, null=True)
    excluded = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cm_synch_objects'
        unique_together = (('synch_guid', 'object_type', 'object_schema', 'object_name', 'first_version'),)


class MgmtCmSynchScripts(models.Model):
    synch_guid = models.ForeignKey('MgmtCmSynchronizations', models.DO_NOTHING, db_column='synch_guid')
    synch_version = models.FloatField()
    object_type = models.FloatField(blank=True, null=True)
    object_schema = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=128, blank=True, null=True)
    script_line_no = models.FloatField()
    script_step_no = models.FloatField()
    script_line_type = models.CharField(max_length=15)
    script_section = models.CharField(max_length=10)
    line_edited = models.CharField(max_length=1)
    script_line = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_synch_scripts'


class MgmtCmSynchVersions(models.Model):
    synch_guid = models.ForeignKey('MgmtCmSynchronizations', models.DO_NOTHING, db_column='synch_guid')
    synch_version = models.FloatField()
    version_status = models.CharField(max_length=3, blank=True, null=True)
    version_state = models.FloatField()
    job_execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    source_version = models.FloatField(blank=True, null=True)
    generation_time = models.DateField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    execution_time = models.DateField(blank=True, null=True)
    impact_report = models.BinaryField(blank=True, null=True)
    script = models.BinaryField(blank=True, null=True)
    comparison_job_exec_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    generation_job_exec_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    processing_mode = models.FloatField()
    max_ir_severity = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cm_synch_versions'
        unique_together = (('synch_guid', 'synch_version'),)


class MgmtCmSynchronizations(models.Model):
    synch_guid = models.TextField(primary_key=True)  # This field type is a guess.
    synch_owner = models.CharField(max_length=30)
    synch_name = models.CharField(max_length=30)
    synch_ss = models.TextField()  # This field type is a guess.
    description = models.CharField(max_length=2000, blank=True, null=True)
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    source_type = models.CharField(max_length=1)
    source_id = models.TextField()  # This field type is a guess.
    source_name = models.CharField(max_length=256)
    source_version = models.FloatField(blank=True, null=True)
    source_temp_bl_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_id = models.TextField()  # This field type is a guess.
    target_name = models.CharField(max_length=256)
    target_temp_bl_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_cm_synchronizations'
        unique_together = (('synch_owner', 'synch_name'),)


class MgmtCollItemMetrics(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=8)
    coll_name = models.CharField(max_length=64)
    metric_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_coll_item_metrics'
        unique_together = (('target_type', 'type_meta_ver', 'coll_name', 'metric_guid'),)


class MgmtCollItemProperties(models.Model):
    object_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    property_name = models.CharField(max_length=64)
    object_type = models.NullBooleanField()
    property_value = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'mgmt_coll_item_properties'
        unique_together = (('object_guid', 'metric_guid', 'coll_name', 'property_name'),)


class MgmtCollItems(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=8)
    coll_name = models.CharField(max_length=64)
    category_prop_1 = models.CharField(max_length=64)
    category_prop_2 = models.CharField(max_length=64)
    category_prop_3 = models.CharField(max_length=64)
    category_prop_4 = models.CharField(max_length=64)
    category_prop_5 = models.CharField(max_length=64)
    is_enabled = models.BooleanField()
    is_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_coll_items'
        unique_together = (('target_type', 'type_meta_ver', 'coll_name', 'category_prop_1', 'category_prop_2', 'category_prop_3', 'category_prop_4', 'category_prop_5'),)


class MgmtCollectionCredentials(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    credential_set_name = models.CharField(max_length=32)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_collection_credentials'
        unique_together = (('target_guid', 'metric_guid', 'coll_name', 'credential_set_name'),)


class MgmtCollectionMetricTasks(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    metric_guid = models.TextField()  # This field type is a guess.
    task_id = models.FloatField(blank=True, null=True)
    last_collected_timestamp = models.DateField(blank=True, null=True)
    status_message = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_collection_metric_tasks'
        unique_together = (('target_guid', 'coll_name', 'metric_guid'),)


class MgmtCollectionTaskContext(models.Model):
    task_id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_collection_task_context'
        unique_together = (('task_id', 'name'),)


class MgmtCollectionTasks(models.Model):
    task_id = models.FloatField(primary_key=True)
    task_type = models.FloatField()
    task_class = models.FloatField()
    priority = models.FloatField()
    timezone_region = models.CharField(max_length=64)
    frequency_code = models.FloatField()
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    execution_hours = models.FloatField(blank=True, null=True)
    execution_minutes = models.FloatField(blank=True, null=True)
    interval = models.FloatField(blank=True, null=True)
    months = models.TextField(blank=True, null=True)  # This field type is a guess.
    days = models.TextField(blank=True, null=True)  # This field type is a guess.
    task_proc = models.CharField(max_length=4000, blank=True, null=True)
    task_status = models.FloatField()
    task_start_time = models.DateField(blank=True, null=True)
    last_collection_timestamp = models.DateField(blank=True, null=True)
    next_collection_timestamp = models.DateField(blank=True, null=True)
    error_message = models.CharField(max_length=4000, blank=True, null=True)
    failures = models.FloatField(blank=True, null=True)
    worker_id = models.FloatField(blank=True, null=True)
    total_runs = models.FloatField()
    min_wait_time = models.FloatField()
    max_wait_time = models.FloatField()
    avg_wait_time = models.FloatField()
    min_run_time = models.FloatField()
    max_run_time = models.FloatField()
    avg_run_time = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_collection_tasks'


class MgmtCollectionTemplateCreds(models.Model):
    object_guid = models.TextField(primary_key=True)  # This field type is a guess.
    object_type = models.BooleanField()
    target_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    credential_set_name = models.CharField(max_length=32)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_collection_template_creds'
        unique_together = (('object_guid', 'object_type', 'target_guid', 'metric_guid', 'coll_name', 'credential_set_name'),)


class MgmtCollectionWorkers(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    task_class_list = models.CharField(max_length=64)
    worker_status = models.FloatField()
    job_id = models.FloatField(blank=True, null=True)
    worker_start_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_collection_workers'


class MgmtCollections(models.Model):
    object_guid = models.TextField(primary_key=True)  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    object_type = models.NullBooleanField()
    is_enabled = models.BooleanField()
    schedule_ex = models.CharField(max_length=1024, blank=True, null=True)
    store_metric = models.BooleanField()
    upload_frequency = models.FloatField(blank=True, null=True)
    is_transient = models.BooleanField()
    frequency_code = models.FloatField()
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    execution_hours = models.FloatField(blank=True, null=True)
    execution_minutes = models.FloatField(blank=True, null=True)
    interval = models.FloatField(blank=True, null=True)
    months = models.TextField(blank=True, null=True)  # This field type is a guess.
    days = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_collections'
        unique_together = (('object_guid', 'coll_name'),)


class MgmtCompResultToJobMap(models.Model):
    execution_id = models.TextField()  # This field type is a guess.
    delta_comp_guid = models.ForeignKey('MgmtDeltaSavedComparison', models.DO_NOTHING, db_column='delta_comp_guid')
    rhs_host_name = models.CharField(max_length=256, blank=True, null=True)
    rhs_snapshot_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_comp_result_to_job_map'


class MgmtCompSnapshotToStepMap(models.Model):
    step_id = models.FloatField(primary_key=True)
    rhs_snapshot_guid = models.TextField()  # This field type is a guess.
    execution_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_comp_snapshot_to_step_map'
        unique_together = (('step_id', 'execution_id'),)


class MgmtConfigActivities(models.Model):
    txn_id = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    cluster_name = models.CharField(max_length=64, blank=True, null=True)
    status_code = models.FloatField(blank=True, null=True)
    config_type = models.CharField(max_length=32, blank=True, null=True)
    occurence_time = models.DateTimeField(blank=True, null=True)
    host_name = models.CharField(max_length=64, blank=True, null=True)
    source_host_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_config_activities'
        unique_together = (('target_guid', 'txn_id'),)


class MgmtContainerCredentials(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    container_location = models.CharField(max_length=1024)
    credential_set_name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=256)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_container_credentials'
        unique_together = (('target_guid', 'container_location', 'credential_set_name', 'user_name'),)


class MgmtCorrectiveAction(models.Model):
    job_id = models.TextField(primary_key=True)  # This field type is a guess.
    ca_scope = models.NullBooleanField()
    ca_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    ca_template_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    ca_reference_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_corrective_action'


class MgmtCpfMetricSource(models.Model):
    advisory_name = models.CharField(max_length=128)
    impact = models.CharField(max_length=128, blank=True, null=True)
    advisory_abstract = models.CharField(max_length=1024, blank=True, null=True)
    home_location_display = models.CharField(max_length=1000, blank=True, null=True)
    home_location = models.CharField(max_length=128)
    host_name = models.CharField(max_length=256)
    advisory_url = models.CharField(max_length=256, blank=True, null=True)
    patch_guids = models.CharField(max_length=4000)
    target_guid = models.TextField()  # This field type is a guess.
    patches = models.CharField(max_length=2000, blank=True, null=True)
    container_guid = models.TextField(primary_key=True)  # This field type is a guess.
    is_valid = models.CharField(max_length=10)
    cpf_violation_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_cpf_metric_source'
        unique_together = (('container_guid', 'target_guid', 'host_name', 'home_location', 'advisory_name'),)


class MgmtCreatedUsers(models.Model):
    user_name = models.CharField(primary_key=True, max_length=256)
    system_user = models.NullBooleanField()
    deleting = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_created_users'


class MgmtCredentialSetColVals(models.Model):
    target_type = models.ForeignKey('MgmtCredentialSets', models.DO_NOTHING, db_column='target_type', primary_key=True)
    target_type_meta_ver = models.ForeignKey('MgmtCredentialSets', models.DO_NOTHING, db_column='target_type_meta_ver')
    set_name = models.ForeignKey('MgmtCredentialSets', models.DO_NOTHING, db_column='set_name')
    set_column_name = models.CharField(max_length=64)
    default_value = models.NullBooleanField()
    value = models.CharField(max_length=1024)
    value_nlsid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_credential_set_col_vals'
        unique_together = (('target_type', 'target_type_meta_ver', 'set_name', 'set_column_name', 'value'),)


class MgmtCredentialSetColumns(models.Model):
    target_type = models.ForeignKey('MgmtCredentialSets', models.DO_NOTHING, db_column='target_type', primary_key=True)
    target_type_meta_ver = models.ForeignKey('MgmtCredentialSets', models.DO_NOTHING, db_column='target_type_meta_ver')
    set_name = models.ForeignKey('MgmtCredentialSets', models.DO_NOTHING, db_column='set_name')
    set_column_name = models.CharField(max_length=64)
    set_column_display_name = models.CharField(max_length=128, blank=True, null=True)
    set_column_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    type_column_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_credential_set_columns'
        unique_together = (('target_type', 'target_type_meta_ver', 'set_name', 'set_column_name'),)


class MgmtCredentialSets(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    target_type_meta_ver = models.CharField(max_length=8)
    set_name = models.CharField(max_length=64)
    set_display_name = models.CharField(max_length=128, blank=True, null=True)
    set_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    credential_type_name = models.CharField(max_length=64, blank=True, null=True)
    set_usage = models.CharField(max_length=64, blank=True, null=True)
    set_context_type = models.CharField(max_length=64, blank=True, null=True)
    set_context = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_credential_sets'
        unique_together = (('target_type', 'target_type_meta_ver', 'set_name'),)


class MgmtCredentialTypeColVals(models.Model):
    target_type = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='target_type', primary_key=True)
    target_type_meta_ver = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='target_type_meta_ver')
    type_name = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='type_name')
    type_column_name = models.CharField(max_length=64)
    default_value = models.NullBooleanField()
    value = models.CharField(max_length=1024)
    value_nlsid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_credential_type_col_vals'
        unique_together = (('target_type', 'target_type_meta_ver', 'type_name', 'type_column_name', 'value'),)


class MgmtCredentialTypeColumns(models.Model):
    target_type = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='target_type', primary_key=True)
    target_type_meta_ver = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='target_type_meta_ver')
    type_name = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='type_name')
    type_column_name = models.CharField(max_length=64)
    ref_name = models.CharField(max_length=64, blank=True, null=True)
    ref_column_name = models.CharField(max_length=64, blank=True, null=True)
    type_column_display_name = models.CharField(max_length=128, blank=True, null=True)
    type_column_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    key = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_credential_type_columns'
        unique_together = (('target_type', 'target_type_meta_ver', 'type_name', 'type_column_name'),)


class MgmtCredentialTypeRef(models.Model):
    target_type = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='target_type', primary_key=True)
    target_type_meta_ver = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='target_type_meta_ver')
    type_name = models.ForeignKey('MgmtCredentialTypes', models.DO_NOTHING, db_column='type_name')
    ref_name = models.CharField(max_length=64)
    ref_type_name = models.CharField(max_length=64)
    ref_target_type = models.CharField(max_length=64)
    ref_type_meta_ver = models.CharField(max_length=8, blank=True, null=True)
    association = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_credential_type_ref'
        unique_together = (('target_type', 'target_type_meta_ver', 'type_name', 'ref_name', 'ref_type_name', 'ref_target_type'),)


class MgmtCredentialTypes(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    target_type_meta_ver = models.CharField(max_length=8)
    type_name = models.CharField(max_length=64)
    type_display_name = models.CharField(max_length=128, blank=True, null=True)
    type_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_credential_types'
        unique_together = (('target_type', 'target_type_meta_ver', 'type_name'),)


class MgmtCredentials(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    container_location = models.CharField(max_length=1024)
    credential_column = models.CharField(max_length=32)
    user_name = models.CharField(max_length=256)
    credential_value = models.CharField(max_length=256, blank=True, null=True)
    monitoring_credential = models.FloatField()
    monitoring_column_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_credentials'
        unique_together = (('target_guid', 'container_location', 'credential_column', 'user_name', 'monitoring_credential'),)


class MgmtCredentials2(models.Model):
    credential_guid = models.TextField(primary_key=True)  # This field type is a guess.
    credential_set_column = models.CharField(max_length=64)
    credential_value = models.CharField(max_length=256, blank=True, null=True)
    credential_type_name = models.CharField(max_length=32, blank=True, null=True)
    credential_type_column = models.CharField(max_length=32, blank=True, null=True)
    key_value = models.CharField(max_length=256, blank=True, null=True)
    assoc_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_credentials2'
        unique_together = (('credential_guid', 'credential_set_column'),)


class MgmtCsConfigStandard(models.Model):
    cs_guid = models.TextField(primary_key=True)  # This field type is a guess.
    cs_iname = models.CharField(max_length=128)
    cs_dname = models.CharField(max_length=128)
    target_type = models.CharField(max_length=128)
    created_date = models.DateField(blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=256, blank=True, null=True)
    author = models.CharField(max_length=256, blank=True, null=True)
    owner = models.CharField(max_length=256, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    lifecycle_status = models.NullBooleanField()
    usage_type = models.NullBooleanField()
    is_locked = models.NullBooleanField()
    locked_by = models.CharField(max_length=256, blank=True, null=True)
    locked_time = models.DateField(blank=True, null=True)
    is_hidden = models.NullBooleanField()
    description = models.CharField(max_length=256, blank=True, null=True)
    reference_url = models.CharField(max_length=4000, blank=True, null=True)
    front_matter = models.CharField(max_length=500, blank=True, null=True)
    rear_matter = models.CharField(max_length=500, blank=True, null=True)
    notice = models.CharField(max_length=500, blank=True, null=True)
    repo_timing_enabled = models.NullBooleanField()
    cqs_package_name = models.CharField(max_length=30, blank=True, null=True)
    cqs_date = models.DateField(blank=True, null=True)
    cqs_valid = models.NullBooleanField()
    rqs_hierarchy_valid = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_config_standard'


class MgmtCsEvalSummRqs(models.Model):
    rqs_guid = models.TextField()  # This field type is a guess.
    root_cs_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    root_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    compliant_rules = models.FloatField()
    non_compliant_rules = models.FloatField()
    error_rules = models.FloatField()
    unknown_rules = models.FloatField()
    crit_violations = models.FloatField()
    warn_violations = models.FloatField()
    info_violations = models.FloatField()
    last_evaluation_date = models.DateField(blank=True, null=True)
    compliance_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_eval_summ_rqs'
        unique_together = (('target_guid', 'rqs_guid'),)


class MgmtCsEvalSummRule(models.Model):
    rqs_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rule_guid = models.TextField()  # This field type is a guess.
    root_cs_guid = models.TextField()  # This field type is a guess.
    root_target_guid = models.TextField()  # This field type is a guess.
    total_violations = models.FloatField()
    status = models.BooleanField()
    evaluation_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_eval_summ_rule'
        unique_together = (('target_guid', 'rqs_guid', 'rule_guid'),)


class MgmtCsEvalSummRulefolder(models.Model):
    rqs_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rulefolder_guid = models.TextField()  # This field type is a guess.
    root_cs_guid = models.TextField()  # This field type is a guess.
    root_target_guid = models.TextField()  # This field type is a guess.
    compliant_rules = models.FloatField()
    non_compliant_rules = models.FloatField()
    error_rules = models.FloatField()
    unknown_rules = models.FloatField()
    crit_violations = models.FloatField()
    warn_violations = models.FloatField()
    info_violations = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_eval_summ_rulefolder'
        unique_together = (('target_guid', 'rqs_guid', 'rulefolder_guid'),)


class MgmtCsHierarchy(models.Model):
    parent_guid = models.TextField(primary_key=True)  # This field type is a guess.
    child_guid = models.TextField()  # This field type is a guess.
    child_type = models.BooleanField()
    child_position = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_hierarchy'
        unique_together = (('parent_guid', 'child_guid'),)


class MgmtCsInclusion(models.Model):
    cs_inclusion_guid = models.TextField(primary_key=True)  # This field type is a guess.
    parent_cs_guid = models.TextField()  # This field type is a guess.
    included_cs_iname = models.CharField(max_length=128)
    included_cs_author = models.CharField(max_length=256)
    included_cs_version = models.FloatField()
    context_query = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_inclusion'


class MgmtCsInclusionParameter(models.Model):
    cs_inclusion_guid = models.TextField(primary_key=True)  # This field type is a guess.
    param_iname = models.CharField(max_length=128)
    param_override_value = models.CharField(max_length=1024)
    ref_param_iname = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_inclusion_parameter'
        unique_together = (('cs_inclusion_guid', 'param_iname'),)


class MgmtCsKeyword(models.Model):
    keyword = models.CharField(primary_key=True, max_length=64)
    cs_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_cs_keyword'
        unique_together = (('keyword', 'cs_guid'),)


class MgmtCsParameter(models.Model):
    param_guid = models.TextField(primary_key=True)  # This field type is a guess.
    cs_guid = models.TextField()  # This field type is a guess.
    param_iname = models.CharField(max_length=128)
    param_type = models.NullBooleanField()
    param_value = models.CharField(max_length=1024)
    description = models.CharField(max_length=256, blank=True, null=True)
    prohibit_changes = models.NullBooleanField()
    num_choices = models.FloatField(blank=True, null=True)
    must_match = models.NullBooleanField()
    lower_bound = models.FloatField(blank=True, null=True)
    upper_bound = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_parameter'
        unique_together = (('cs_guid', 'param_iname'),)


class MgmtCsParameterChoices(models.Model):
    param_guid = models.TextField()  # This field type is a guess.
    choice_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_parameter_choices'


class MgmtCsReusableQuery(models.Model):
    reusable_query_guid = models.TextField(primary_key=True)  # This field type is a guess.
    cs_guid = models.TextField()  # This field type is a guess.
    reusable_query_iname = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True, null=True)
    reusable_query = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_reusable_query'
        unique_together = (('cs_guid', 'reusable_query_iname'),)


class MgmtCsRqsHierarchy(models.Model):
    child_rqs_guid = models.TextField(primary_key=True)  # This field type is a guess.
    root_cs_guid = models.TextField()  # This field type is a guess.
    child_guid = models.TextField()  # This field type is a guess.
    child_type = models.BooleanField()
    child_position = models.FloatField()
    parent_rqs_guid = models.TextField()  # This field type is a guess.
    parent_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_cs_rqs_hierarchy'
        unique_together = (('child_rqs_guid', 'parent_guid', 'child_guid'),)


class MgmtCsRqsInclusion(models.Model):
    rqs_guid = models.TextField(primary_key=True)  # This field type is a guess.
    parent_rqs_guid = models.TextField()  # This field type is a guess.
    cs_inclusion_guid = models.TextField()  # This field type is a guess.
    root_cs_guid = models.TextField()  # This field type is a guess.
    parent_cs_guid = models.TextField()  # This field type is a guess.
    included_cs_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_cs_rqs_inclusion'
        unique_together = (('root_cs_guid', 'parent_rqs_guid', 'cs_inclusion_guid'),)


class MgmtCsRule(models.Model):
    rule_guid = models.TextField(primary_key=True)  # This field type is a guess.
    cs_guid = models.TextField()  # This field type is a guess.
    rule_iname = models.CharField(max_length=128)
    rule_dname = models.CharField(max_length=128)
    importance_level = models.NullBooleanField()
    description = models.CharField(max_length=256, blank=True, null=True)
    reference_url = models.CharField(max_length=4000, blank=True, null=True)
    rationale = models.CharField(max_length=500, blank=True, null=True)
    fixtext = models.CharField(max_length=500, blank=True, null=True)
    warning = models.CharField(max_length=500, blank=True, null=True)
    test_type = models.NullBooleanField()
    test = models.CharField(max_length=4000, blank=True, null=True)
    policy_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    change_advisor_type = models.CharField(max_length=256, blank=True, null=True)
    change_advisor_subtype = models.CharField(max_length=256, blank=True, null=True)
    change_advisor_reason = models.CharField(max_length=256, blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)
    clear_message = models.CharField(max_length=4000, blank=True, null=True)
    severity = models.NullBooleanField()
    simple_test_condition = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_rule'
        unique_together = (('cs_guid', 'rule_iname'),)


class MgmtCsRuleFixLink(models.Model):
    rule_guid = models.TextField(primary_key=True)  # This field type is a guess.
    display_label = models.CharField(max_length=256)
    link_template = models.CharField(max_length=4000, blank=True, null=True)
    link_encode = models.NullBooleanField()
    is_link_em_page = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_rule_fix_link'
        unique_together = (('rule_guid', 'display_label'),)


class MgmtCsRuleSimpleTest(models.Model):
    rule_guid = models.TextField(primary_key=True)  # This field type is a guess.
    property = models.CharField(max_length=4000)
    operator = models.BooleanField()
    value = models.CharField(max_length=4000)
    position = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_rule_simple_test'
        unique_together = (('rule_guid', 'position'),)


class MgmtCsRuleViolCtx(models.Model):
    rule_guid = models.TextField()  # This field type is a guess.
    column_iname = models.CharField(max_length=128)
    column_dname = models.CharField(max_length=128, blank=True, null=True)
    column_type = models.NullBooleanField()
    column_position = models.FloatField(blank=True, null=True)
    is_key = models.NullBooleanField()
    is_hidden = models.NullBooleanField()
    link_template = models.CharField(max_length=4000, blank=True, null=True)
    link_encode = models.NullBooleanField()
    is_link_em_page = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cs_rule_viol_ctx'
        unique_together = (('rule_guid', 'column_iname'),)


class MgmtCsRulefolder(models.Model):
    rulefolder_guid = models.TextField(primary_key=True)  # This field type is a guess.
    cs_guid = models.TextField()  # This field type is a guess.
    rulefolder_iname = models.CharField(max_length=128)
    rulefolder_dname = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True, null=True)
    reference_url = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_rulefolder'
        unique_together = (('cs_guid', 'rulefolder_iname'),)


class MgmtCsScheduledEval(models.Model):
    cs_guid = models.TextField()  # This field type is a guess.
    job_id = models.TextField(primary_key=True)  # This field type is a guess.
    eval_name = models.CharField(max_length=64)
    eval_owner = models.CharField(max_length=256)
    eval_description = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cs_scheduled_eval'


class MgmtCstmzChartSeltargets(models.Model):
    comp_chart_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_cstmz_chart_seltargets'


class MgmtCstmzCharts(models.Model):
    comp_chart_guid = models.TextField()  # This field type is a guess.
    comp_target_guid = models.TextField()  # This field type is a guess.
    chart_type = models.BooleanField()
    member_metric_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    display_order = models.IntegerField(blank=True, null=True)
    targets_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cstmz_charts'


class MgmtCstmzCustomColumns(models.Model):
    composite_target_guid = models.TextField()  # This field type is a guess.
    column_type = models.IntegerField(blank=True, null=True)
    member_metric_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    property_name = models.CharField(max_length=64, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    abbreviation = models.CharField(max_length=64, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    view_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cstmz_custom_columns'


class MgmtCstmzDefaultChart(models.Model):
    comp_target_type = models.CharField(primary_key=True, max_length=64)
    chart_type = models.BooleanField()
    member_target_type = models.CharField(max_length=64)
    member_metric_name = models.CharField(max_length=64)
    member_metric_column = models.CharField(max_length=64)
    targets_count = models.IntegerField(blank=True, null=True)
    min_column = models.NullBooleanField()
    max_column = models.NullBooleanField()
    avg_column = models.NullBooleanField()
    sum_column = models.NullBooleanField()
    stdev_column = models.NullBooleanField()
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_cstmz_default_chart'
        unique_together = (('comp_target_type', 'chart_type', 'member_target_type', 'member_metric_name', 'member_metric_column'),)


class MgmtCstmzSummaryChartDef(models.Model):
    comp_chart_guid = models.TextField()  # This field type is a guess.
    comp_target_guid = models.TextField()  # This field type is a guess.
    comp_metric_guid = models.TextField()  # This field type is a guess.
    min_column = models.NullBooleanField()
    max_column = models.NullBooleanField()
    avg_column = models.NullBooleanField()
    sum_column = models.NullBooleanField()
    stdev_column = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_cstmz_summary_chart_def'


class MgmtCurrentAvailability(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_status = models.FloatField()
    start_collection_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_current_availability'


class MgmtCurrentMetricErrors(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    agent_guid = models.TextField()  # This field type is a guess.
    collection_timestamp = models.DateField()
    metric_error_message = models.CharField(max_length=4000, blank=True, null=True)
    metric_error_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_current_metric_errors'
        unique_together = (('target_guid', 'metric_guid', 'coll_name', 'agent_guid'),)


class MgmtCurrentMetrics(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    collection_timestamp = models.DateField()
    value = models.FloatField(blank=True, null=True)
    string_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_current_metrics'
        unique_together = (('target_guid', 'metric_guid', 'key_value'),)


class MgmtDbControlfilesEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    file_name = models.CharField(max_length=512)
    status = models.CharField(max_length=10, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    sequence_num = models.FloatField(blank=True, null=True)
    change_num = models.FloatField(blank=True, null=True)
    mod_date = models.DateField(blank=True, null=True)
    os_storage_entity = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_controlfiles_ecm'
        unique_together = (('ecm_snapshot', 'file_name'),)


class MgmtDbDatafilesEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    tablespace_name = models.CharField(max_length=30)
    file_name = models.CharField(max_length=512)
    status = models.CharField(max_length=9, blank=True, null=True)
    file_size = models.FloatField(blank=True, null=True)
    autoextensible = models.CharField(max_length=3, blank=True, null=True)
    increment_by = models.FloatField(blank=True, null=True)
    max_file_size = models.FloatField(blank=True, null=True)
    os_storage_entity = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_datafiles_ecm'
        unique_together = (('ecm_snapshot', 'tablespace_name', 'file_name'),)


class MgmtDbDbninstanceinfoEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    database_name = models.CharField(max_length=9, blank=True, null=True)
    global_name = models.CharField(max_length=4000, blank=True, null=True)
    banner = models.CharField(max_length=80, blank=True, null=True)
    host_name = models.CharField(max_length=64, blank=True, null=True)
    instance_name = models.CharField(max_length=16, blank=True, null=True)
    startup_time = models.DateField(blank=True, null=True)
    logins = models.CharField(max_length=10, blank=True, null=True)
    log_mode = models.CharField(max_length=12, blank=True, null=True)
    open_mode = models.CharField(max_length=10, blank=True, null=True)
    default_temp_tablespace = models.CharField(max_length=30, blank=True, null=True)
    characterset = models.CharField(max_length=64, blank=True, null=True)
    national_characterset = models.CharField(max_length=64, blank=True, null=True)
    dv_status_code = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_db_dbninstanceinfo_ecm'


class MgmtDbFeatureusage(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField(blank=True, null=True)
    dbid = models.FloatField()
    name = models.CharField(max_length=64)
    currently_used = models.CharField(max_length=5, blank=True, null=True)
    detected_usages = models.FloatField()
    first_usage_date = models.DateField(blank=True, null=True)
    last_usage_date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=17)
    last_sample_date = models.DateField(blank=True, null=True)
    last_sample_period = models.FloatField(blank=True, null=True)
    total_samples = models.FloatField()
    aux_count = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_featureusage'
        unique_together = (('target_guid', 'name', 'dbid', 'version'),)


class MgmtDbHdmMetricHelper(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField(blank=True, null=True)
    task_available = models.FloatField()
    task_count = models.FloatField(blank=True, null=True)
    requested_analysis = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_hdm_metric_helper'


class MgmtDbInitParamsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=80)
    value = models.CharField(max_length=4000, blank=True, null=True)
    isdefault = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_init_params_ecm'
        unique_together = (('ecm_snapshot', 'name'),)


class MgmtDbInvobjsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    object_type = models.IntegerField()
    object_owner = models.CharField(max_length=30)
    object_name = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'mgmt_db_invobjs_ecm'
        unique_together = (('ecm_snapshot', 'object_type', 'object_owner', 'object_name'),)


class MgmtDbLatestHdmFindings(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField(blank=True, null=True)
    task_id = models.FloatField()
    finding_id = models.FloatField()
    rec_type = models.CharField(max_length=1024)
    rec_count = models.FloatField(blank=True, null=True)
    impact_pct = models.FloatField(blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    finding_count = models.FloatField(blank=True, null=True)
    finding_name = models.CharField(max_length=4000, blank=True, null=True)
    active_sessions = models.FloatField(blank=True, null=True)
    instance_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_latest_hdm_findings'
        unique_together = (('target_guid', 'task_id', 'finding_id', 'rec_type'),)


class MgmtDbLicenseEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    sessions_max = models.FloatField()
    sessions_warning = models.FloatField(blank=True, null=True)
    sessions_current = models.FloatField(blank=True, null=True)
    sessions_highwater = models.FloatField(blank=True, null=True)
    users_max = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_license_ecm'
        unique_together = (('ecm_snapshot', 'sessions_max'),)


class MgmtDbOptionsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=30)
    selected = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_options_ecm'
        unique_together = (('ecm_snapshot', 'name'),)


class MgmtDbRecsegmentsettingsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    obj_type = models.IntegerField()
    obj_owner = models.CharField(max_length=30)
    obj_name = models.CharField(max_length=30)
    obj_partition = models.CharField(max_length=30)
    obj_lob_col = models.CharField(max_length=500)
    tablespace = models.CharField(max_length=30, blank=True, null=True)
    segment_type = models.IntegerField()
    problem_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_db_recsegmentsettings_ecm'
        unique_together = (('ecm_snapshot', 'obj_type', 'obj_owner', 'obj_name', 'obj_partition', 'obj_lob_col', 'segment_type', 'problem_code'),)


class MgmtDbRectssettingsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    tablespace = models.CharField(max_length=30)
    problem_code = models.IntegerField()
    value1 = models.IntegerField(blank=True, null=True)
    value2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_rectssettings_ecm'
        unique_together = (('ecm_snapshot', 'tablespace', 'problem_code'),)


class MgmtDbRecusersettingsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    user_name = models.CharField(max_length=30)
    problem_code = models.IntegerField()
    tablespace = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_recusersettings_ecm'
        unique_together = (('ecm_snapshot', 'user_name', 'problem_code'),)


class MgmtDbRedologsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    group_num = models.FloatField()
    status = models.CharField(max_length=16, blank=True, null=True)
    members = models.FloatField(blank=True, null=True)
    file_name = models.CharField(max_length=512)
    archived = models.CharField(max_length=3, blank=True, null=True)
    logsize = models.FloatField(blank=True, null=True)
    sequence_num = models.FloatField(blank=True, null=True)
    first_change_scn = models.FloatField(blank=True, null=True)
    os_storage_entity = models.CharField(max_length=512, blank=True, null=True)
    thread_num = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_redologs_ecm'
        unique_together = (('ecm_snapshot', 'group_num', 'file_name'),)


class MgmtDbRollbackSegsEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    rollname = models.CharField(max_length=64)
    status = models.CharField(max_length=16, blank=True, null=True)
    tablespace_name = models.CharField(max_length=30, blank=True, null=True)
    extents = models.FloatField(blank=True, null=True)
    rollsize = models.FloatField(blank=True, null=True)
    initial_size = models.FloatField(blank=True, null=True)
    next_size = models.FloatField(blank=True, null=True)
    maximum_extents = models.FloatField(blank=True, null=True)
    minimum_extents = models.FloatField(blank=True, null=True)
    pct_increase = models.FloatField(blank=True, null=True)
    optsize = models.FloatField(blank=True, null=True)
    aveactive = models.FloatField(blank=True, null=True)
    wraps = models.FloatField(blank=True, null=True)
    shrinks = models.FloatField(blank=True, null=True)
    aveshrink = models.FloatField(blank=True, null=True)
    hwmsize = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_rollback_segs_ecm'
        unique_together = (('ecm_snapshot', 'rollname'),)


class MgmtDbSgaEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    sganame = models.CharField(max_length=64)
    sgasize = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_sga_ecm'
        unique_together = (('ecm_snapshot', 'sganame'),)


class MgmtDbTablespacesEcm(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    tablespace_name = models.CharField(max_length=30)
    contents = models.CharField(max_length=9, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    extent_management = models.CharField(max_length=10, blank=True, null=True)
    allocation_type = models.CharField(max_length=10, blank=True, null=True)
    logging = models.CharField(max_length=10, blank=True, null=True)
    tablespace_size = models.FloatField(blank=True, null=True)
    initial_ext_size = models.FloatField(blank=True, null=True)
    next_extent = models.FloatField(blank=True, null=True)
    increment_by = models.FloatField(blank=True, null=True)
    max_extents = models.FloatField(blank=True, null=True)
    tablespace_used_size = models.FloatField(blank=True, null=True)
    segment_space_management = models.CharField(max_length=6, blank=True, null=True)
    block_size = models.FloatField(blank=True, null=True)
    min_extents = models.FloatField(blank=True, null=True)
    min_extlen = models.FloatField(blank=True, null=True)
    bigfile = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_db_tablespaces_ecm'
        unique_together = (('ecm_snapshot', 'tablespace_name'),)


class MgmtDbnetTnsAdmins(models.Model):
    host_guid = models.TextField()  # This field type is a guess.
    oracle_home = models.CharField(max_length=64)
    tns_admin = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_dbnet_tns_admins'


class MgmtDeltaCompDeltaDetails(models.Model):
    key_guid = models.ForeignKey('MgmtDeltaComparisonDeltas', models.DO_NOTHING, db_column='key_guid', primary_key=True)
    name = models.CharField(max_length=64)
    left_value = models.CharField(max_length=4000, blank=True, null=True)
    right_value = models.CharField(max_length=4000, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_delta_comp_delta_details'
        unique_together = (('key_guid', 'name'),)


class MgmtDeltaCompKeyCols(models.Model):
    delta_comp_guid = models.TextField()  # This field type is a guess.
    collection_type = models.CharField(max_length=64, blank=True, null=True)
    key_guid = models.ForeignKey('MgmtDeltaComparisonDeltas', models.DO_NOTHING, db_column='key_guid', primary_key=True)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=4000, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_delta_comp_key_cols'
        unique_together = (('key_guid', 'name'),)


class MgmtDeltaCompProperties(models.Model):
    delta_comp_guid = models.ForeignKey('MgmtDeltaSavedComparison', models.DO_NOTHING, db_column='delta_comp_guid')
    name = models.CharField(max_length=64)
    left_value = models.CharField(max_length=4000, blank=True, null=True)
    right_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_delta_comp_properties'


class MgmtDeltaCompSummaries(models.Model):
    delta_comp_guid = models.ForeignKey('MgmtDeltaSavedComparison', models.DO_NOTHING, db_column='delta_comp_guid', primary_key=True)
    collection_type = models.CharField(max_length=64)
    different_count = models.BigIntegerField(blank=True, null=True)
    left_count = models.BigIntegerField(blank=True, null=True)
    right_count = models.BigIntegerField(blank=True, null=True)
    errors = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_delta_comp_summaries'
        unique_together = (('delta_comp_guid', 'collection_type'),)


class MgmtDeltaComparisonDeltas(models.Model):
    delta_comp_guid = models.ForeignKey('MgmtDeltaSavedComparison', models.DO_NOTHING, db_column='delta_comp_guid', blank=True, null=True)
    collection_type = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    key_guid = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_delta_comparison_deltas'


class MgmtDeltaEntry(models.Model):
    delta_guid = models.TextField()  # This field type is a guess.
    row_guid = models.ForeignKey('MgmtDeltaIds', models.DO_NOTHING, db_column='row_guid')
    operation = models.CharField(max_length=10)
    delta_time = models.DateField()
    delta_entry_guid = models.TextField(unique=True)  # This field type is a guess.
    prev_delta_entry_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_delta_entry'


class MgmtDeltaEntryValues(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=4000, blank=True, null=True)
    old_value = models.CharField(max_length=4000, blank=True, null=True)
    delta_entry_guid = models.ForeignKey(MgmtDeltaEntry, models.DO_NOTHING, db_column='delta_entry_guid', primary_key=True)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_delta_entry_values'
        unique_together = (('delta_entry_guid', 'name'),)


class MgmtDeltaIdValues(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=4000, blank=True, null=True)
    delta_ids_guid = models.ForeignKey('MgmtDeltaIds', models.DO_NOTHING, db_column='delta_ids_guid', primary_key=True)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_delta_id_values'
        unique_together = (('delta_ids_guid', 'name'),)


class MgmtDeltaIds(models.Model):
    collection_type = models.CharField(max_length=64)
    row_guid = models.TextField(unique=True)  # This field type is a guess.
    last_delta_entry_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_updated_time = models.DateField()
    key_string = models.CharField(max_length=1024)
    key_string_rest = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_delta_ids'


class MgmtDeltaSavedComparison(models.Model):
    delta_comp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    comparison_type = models.CharField(max_length=64, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    saved_timestamp = models.DateField()
    session_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_delta_saved_comparison'


class MgmtDeltaSnap(models.Model):
    delta_guid = models.TextField(primary_key=True)  # This field type is a guess.
    transaction_id = models.CharField(max_length=1024)
    delta_timestamp = models.DateField()
    delta_type = models.CharField(max_length=30, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    snapshot_type = models.CharField(max_length=64, blank=True, null=True)
    new_left_snapshot_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    new_left_target_name = models.CharField(max_length=256, blank=True, null=True)
    new_left_timestamp = models.DateField(blank=True, null=True)
    old_right_snapshot_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    old_right_timestamp = models.DateField(blank=True, null=True)
    old_right_target_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_delta_snap'
# Unable to inspect table 'mgmt_delta_summary_errors'
# The error was: ORA-22812: cannot reference nested table column's storage table


class MgmtDeploymentSections(models.Model):
    class_name = models.CharField(primary_key=True, max_length=256)
    sequence_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_deployment_sections'


class MgmtDirobjUsersHotlist(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    dir_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mgmt_dirobj_users_hotlist'
        unique_together = (('target_guid', 'dir_name', 'user_name'),)


class MgmtDmAlitems(models.Model):
    rule_guid = models.ForeignKey('MgmtDmRuleentry', models.DO_NOTHING, db_column='rule_guid', primary_key=True)
    entry_order = models.ForeignKey('MgmtDmRuleentry', models.DO_NOTHING, db_column='entry_order')
    arraylist_item = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'mgmt_dm_alitems'
        unique_together = (('rule_guid', 'entry_order', 'arraylist_item'),)


class MgmtDmColumnRules(models.Model):
    ss_guid = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='ss_guid')
    table_schema = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='table_schema')
    table_name = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='table_name')
    column_name = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='column_name')
    rule_guid = models.ForeignKey('MgmtDmRuletemplates', models.DO_NOTHING, db_column='rule_guid')

    class Meta:
        managed = False
        db_table = 'mgmt_dm_column_rules'


class MgmtDmInfconsColumns(models.Model):
    ss_guid = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='ss_guid')
    table_schema = models.CharField(max_length=30)
    table_name = models.CharField(max_length=128)
    column_name = models.CharField(max_length=128)
    parent_schema = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='parent_schema')
    parent_table = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='parent_table')
    parent_column = models.ForeignKey('MgmtDmSsColumns', models.DO_NOTHING, db_column='parent_column')

    class Meta:
        managed = False
        db_table = 'mgmt_dm_infcons_columns'
        unique_together = (('ss_guid', 'table_schema', 'table_name', 'column_name'),)


class MgmtDmJobExecutions(models.Model):
    ss_guid = models.ForeignKey('MgmtDmScopespecs', models.DO_NOTHING, db_column='ss_guid', primary_key=True)
    execution_id = models.TextField()  # This field type is a guess.
    submission_ts = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_dm_job_executions'
        unique_together = (('ss_guid', 'execution_id'),)


class MgmtDmRuleentry(models.Model):
    rule_guid = models.ForeignKey('MgmtDmRuletemplates', models.DO_NOTHING, db_column='rule_guid', primary_key=True)
    entry_order = models.FloatField()
    rule_type = models.CharField(max_length=30, blank=True, null=True)
    rule_option = models.CharField(max_length=2, blank=True, null=True)
    rule_low = models.FloatField(blank=True, null=True)
    rule_high = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    fixed_string = models.CharField(max_length=30, blank=True, null=True)
    fixed_number = models.FloatField(blank=True, null=True)
    table_schema = models.CharField(max_length=30, blank=True, null=True)
    table_name = models.CharField(max_length=30, blank=True, null=True)
    column_name = models.CharField(max_length=30, blank=True, null=True)
    udf_name = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_dm_ruleentry'
        unique_together = (('rule_guid', 'entry_order'),)


class MgmtDmRuletemplates(models.Model):
    rule_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rule_owner = models.CharField(max_length=30)
    rule_name = models.CharField(max_length=40)
    description = models.CharField(max_length=2000, blank=True, null=True)
    output_type = models.FloatField()
    is_library = models.FloatField()
    rule_order = models.FloatField(blank=True, null=True)
    rule_condition = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_dm_ruletemplates'
        unique_together = (('rule_owner', 'rule_name'),)


class MgmtDmScopespecs(models.Model):
    ss_guid = models.TextField(primary_key=True)  # This field type is a guess.
    ss_owner = models.CharField(max_length=30)
    ss_name = models.CharField(max_length=40)
    source_id = models.TextField()  # This field type is a guess.
    source_name = models.CharField(max_length=256)
    description = models.CharField(max_length=2000, blank=True, null=True)
    modify_date = models.DateField(blank=True, null=True)
    script_date = models.DateField(blank=True, null=True)
    disable_logs = models.CharField(max_length=1)
    refresh_stats = models.CharField(max_length=1)
    drop_temp_tables = models.CharField(max_length=1)
    parallel_degree = models.CharField(max_length=10, blank=True, null=True)
    dm_flags = models.FloatField(blank=True, null=True)
    post_mask_script = models.TextField(blank=True, null=True)
    full_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_dm_scopespecs'
        unique_together = (('ss_owner', 'ss_name'),)


class MgmtDmSsColumns(models.Model):
    ss_guid = models.ForeignKey(MgmtDmScopespecs, models.DO_NOTHING, db_column='ss_guid')
    rule_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    table_schema = models.CharField(max_length=30)
    table_name = models.CharField(max_length=128)
    column_name = models.CharField(max_length=128)
    column_group = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_dm_ss_columns'
        unique_together = (('ss_guid', 'table_schema', 'table_name', 'column_name'),)


class MgmtDuplicateTargets(models.Model):
    target_name = models.CharField(max_length=256)
    target_type = models.CharField(max_length=64)
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    duplicate_emd_url = models.CharField(max_length=1024)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    detection_time = models.DateField(blank=True, null=True)
    resolved_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_duplicate_targets'
        unique_together = (('target_guid', 'duplicate_emd_url'),)


class MgmtE2EDetails(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    parent_key_guid = models.TextField()  # This field type is a guess.
    node_id = models.CharField(max_length=1000)
    node_attribute = models.CharField(max_length=1000, blank=True, null=True)
    node_type = models.IntegerField()
    collection_timestamp = models.DateField()
    hit_count = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    component_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_details'
        unique_together = (('target_guid', 'collection_timestamp', 'uri', 'node_type', 'node_id', 'key_guid', 'parent_key_guid', 'app_id', 'vhost'),)


class MgmtE2EDetails1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    parent_key_guid = models.TextField()  # This field type is a guess.
    node_id = models.CharField(max_length=1000)
    node_attribute = models.CharField(max_length=1000, blank=True, null=True)
    node_type = models.IntegerField()
    rollup_timestamp = models.DateField()
    hit_count = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    component_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_details_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'node_type', 'node_id', 'key_guid', 'parent_key_guid', 'app_id', 'vhost'),)


class MgmtE2EDetails1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    parent_key_guid = models.TextField()  # This field type is a guess.
    node_id = models.CharField(max_length=1000)
    node_attribute = models.CharField(max_length=1000, blank=True, null=True)
    node_type = models.IntegerField()
    rollup_timestamp = models.DateField()
    hit_count = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    component_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_details_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'node_type', 'node_id', 'key_guid', 'parent_key_guid', 'app_id', 'vhost'),)


class MgmtE2EJdbc(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    collection_timestamp = models.DateField()
    used_conn_count = models.IntegerField(blank=True, null=True)
    conn_cache_hit = models.IntegerField(blank=True, null=True)
    conn_cache_miss = models.IntegerField(blank=True, null=True)
    stmt_create_time = models.IntegerField(blank=True, null=True)
    stmt_cache_hit = models.IntegerField(blank=True, null=True)
    stmt_cache_miss = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_jdbc'
        unique_together = (('target_guid', 'collection_timestamp', 'uri', 'key_guid', 'vhost', 'app_id'),)


class MgmtE2EJdbc1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    rollup_timestamp = models.DateField()
    used_conn_count = models.IntegerField(blank=True, null=True)
    conn_cache_hit = models.IntegerField(blank=True, null=True)
    conn_cache_miss = models.IntegerField(blank=True, null=True)
    stmt_create_time = models.IntegerField(blank=True, null=True)
    stmt_cache_hit = models.IntegerField(blank=True, null=True)
    stmt_cache_miss = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_jdbc_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'key_guid', 'vhost', 'app_id'),)


class MgmtE2EJdbc1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    rollup_timestamp = models.DateField()
    used_conn_count = models.IntegerField(blank=True, null=True)
    conn_cache_hit = models.IntegerField(blank=True, null=True)
    conn_cache_miss = models.IntegerField(blank=True, null=True)
    stmt_create_time = models.IntegerField(blank=True, null=True)
    stmt_cache_hit = models.IntegerField(blank=True, null=True)
    stmt_cache_miss = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_jdbc_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'key_guid', 'vhost', 'app_id'),)


class MgmtE2ESql(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    collection_timestamp = models.DateField()
    exec_count = models.IntegerField(blank=True, null=True)
    exec_time = models.IntegerField(blank=True, null=True)
    fetch_count = models.IntegerField(blank=True, null=True)
    fetch_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_sql'
        unique_together = (('target_guid', 'collection_timestamp', 'uri', 'key_guid', 'vhost', 'app_id'),)


class MgmtE2ESql1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    rollup_timestamp = models.DateField()
    exec_count = models.IntegerField(blank=True, null=True)
    exec_time = models.IntegerField(blank=True, null=True)
    fetch_count = models.IntegerField(blank=True, null=True)
    fetch_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_sql_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'key_guid', 'vhost', 'app_id'),)


class MgmtE2ESql1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    app_id = models.CharField(max_length=128)
    uri = models.CharField(max_length=2000)
    key_guid = models.TextField()  # This field type is a guess.
    rollup_timestamp = models.DateField()
    exec_count = models.IntegerField(blank=True, null=True)
    exec_time = models.IntegerField(blank=True, null=True)
    fetch_count = models.IntegerField(blank=True, null=True)
    fetch_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_sql_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'key_guid', 'vhost', 'app_id'),)


class MgmtE2ESqlConn(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    conn_guid = models.TextField(primary_key=True)  # This field type is a guess.
    conn_schema = models.CharField(max_length=64)
    conn_string = models.CharField(max_length=4000)
    ttl_ref = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_sql_conn'
        unique_together = (('conn_guid', 'target_guid'),)


class MgmtE2ESqlStmt(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    stmt_guid = models.TextField(primary_key=True)  # This field type is a guess.
    stmt_text = models.CharField(max_length=4000)
    part_no = models.IntegerField()
    ttl_ref = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_sql_stmt'
        unique_together = (('stmt_guid', 'part_no', 'target_guid'),)


class MgmtE2ESummary(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    uri = models.CharField(max_length=2000)
    collection_timestamp = models.DateField()
    hit_count = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    max_time = models.IntegerField(blank=True, null=True)
    min_time = models.IntegerField(blank=True, null=True)
    servlet_count = models.IntegerField(blank=True, null=True)
    servlet_time = models.IntegerField(blank=True, null=True)
    jsp_count = models.IntegerField(blank=True, null=True)
    jsp_time = models.IntegerField(blank=True, null=True)
    ejb_count = models.IntegerField(blank=True, null=True)
    ejb_time = models.IntegerField(blank=True, null=True)
    jdbc_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_summary'
        unique_together = (('target_guid', 'collection_timestamp', 'uri', 'vhost'),)


class MgmtE2ESummary1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    uri = models.CharField(max_length=2000)
    rollup_timestamp = models.DateField()
    hit_count = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    max_time = models.IntegerField(blank=True, null=True)
    min_time = models.IntegerField(blank=True, null=True)
    servlet_count = models.IntegerField(blank=True, null=True)
    servlet_time = models.IntegerField(blank=True, null=True)
    jsp_count = models.IntegerField(blank=True, null=True)
    jsp_time = models.IntegerField(blank=True, null=True)
    ejb_count = models.IntegerField(blank=True, null=True)
    ejb_time = models.IntegerField(blank=True, null=True)
    jdbc_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_summary_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'vhost'),)


class MgmtE2ESummary1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    vhost = models.CharField(max_length=256)
    uri = models.CharField(max_length=2000)
    rollup_timestamp = models.DateField()
    hit_count = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    max_time = models.IntegerField(blank=True, null=True)
    min_time = models.IntegerField(blank=True, null=True)
    servlet_count = models.IntegerField(blank=True, null=True)
    servlet_time = models.IntegerField(blank=True, null=True)
    jsp_count = models.IntegerField(blank=True, null=True)
    jsp_time = models.IntegerField(blank=True, null=True)
    ejb_count = models.IntegerField(blank=True, null=True)
    ejb_time = models.IntegerField(blank=True, null=True)
    jdbc_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_e2e_summary_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'uri', 'vhost'),)


class MgmtEcmAruMap(models.Model):
    aru_id = models.IntegerField(primary_key=True)
    display_string = models.CharField(max_length=64)
    em_name = models.CharField(max_length=64)
    em_bitlength = models.CharField(max_length=8)
    category = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_aru_map'
        unique_together = (('aru_id', 'category'),)


class MgmtEcmClusterNodeInfo(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    node_name = models.CharField(max_length=256)
    cluster_name = models.CharField(max_length=256, blank=True, null=True)
    cluster_home = models.CharField(max_length=500, blank=True, null=True)
    node_list = models.CharField(max_length=4000, blank=True, null=True)
    node_status = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_cluster_node_info'
        unique_together = (('ecm_snapshot', 'node_name'),)


class MgmtEcmCsa(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    net_latency_in_ms = models.FloatField(blank=True, null=True)
    net_bandwidth_in_kbitps = models.FloatField(blank=True, null=True)
    net_effective_ip = models.CharField(max_length=20, blank=True, null=True)
    net_ip = models.CharField(max_length=20, blank=True, null=True)
    net_subnet = models.CharField(max_length=20, blank=True, null=True)
    browser_type = models.CharField(max_length=100, blank=True, null=True)
    browser_version = models.CharField(max_length=20, blank=True, null=True)
    browser_jvm_vendor = models.CharField(max_length=100, blank=True, null=True)
    browser_jvm_version = models.CharField(max_length=20, blank=True, null=True)
    browser_proxy_server = models.CharField(max_length=4000, blank=True, null=True)
    browser_proxy_exceptions = models.CharField(max_length=4000, blank=True, null=True)
    browser_cache_size_in_mb = models.FloatField(blank=True, null=True)
    browser_cache_update_frq = models.CharField(max_length=200, blank=True, null=True)
    browser_http1_1_support = models.CharField(max_length=1, blank=True, null=True)
    referring_url_header = models.CharField(max_length=4000, blank=True, null=True)
    referring_url_params = models.CharField(max_length=4000, blank=True, null=True)
    csa_url_header = models.CharField(max_length=4000, blank=True, null=True)
    csa_url_params = models.CharField(max_length=4000, blank=True, null=True)
    destination_url_header = models.CharField(max_length=4000, blank=True, null=True)
    destination_url_params = models.CharField(max_length=4000, blank=True, null=True)
    connection_type = models.FloatField(blank=True, null=True)
    is_windows_admin = models.CharField(max_length=1, blank=True, null=True)
    windows_domain = models.CharField(max_length=100, blank=True, null=True)
    auto_config_url = models.CharField(max_length=4000, blank=True, null=True)
    browser_proxy_enabled = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa'


class MgmtEcmCsaAppidTargetMap(models.Model):
    appid = models.CharField(max_length=128, blank=True, null=True)
    target_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_appid_target_map'
        unique_together = (('appid', 'target_guid'),)


class MgmtEcmCsaCookies(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING)
    name = models.CharField(max_length=4000, blank=True, null=True)
    value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_cookies'


class MgmtEcmCsaCustom(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING)
    type = models.CharField(max_length=512, blank=True, null=True)
    name = models.CharField(max_length=512)
    type_ui = models.CharField(max_length=4000, blank=True, null=True)
    name_ui = models.CharField(max_length=4000, blank=True, null=True)
    value = models.CharField(max_length=4000, blank=True, null=True)
    display_ui = models.CharField(max_length=1, blank=True, null=True)
    history_tracking = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_custom'
        unique_together = (('ecm_snapshot', 'type', 'name'),)


class MgmtEcmCsaFailed(models.Model):
    id = models.TextField()  # This field type is a guess.
    timestamp = models.DateField(blank=True, null=True)
    timezone_delta = models.FloatField(blank=True, null=True)
    saved_timestamp = models.DateField()
    effective_ip = models.CharField(max_length=20, blank=True, null=True)
    appid = models.CharField(max_length=128, blank=True, null=True)
    referring_url_header = models.CharField(max_length=4000, blank=True, null=True)
    referring_url_params = models.CharField(max_length=4000, blank=True, null=True)
    csa_url_header = models.CharField(max_length=4000, blank=True, null=True)
    csa_url_params = models.CharField(max_length=4000, blank=True, null=True)
    destination_url_header = models.CharField(max_length=4000, blank=True, null=True)
    destination_url_params = models.CharField(max_length=4000, blank=True, null=True)
    browser_type = models.CharField(max_length=100, blank=True, null=True)
    browser_version = models.CharField(max_length=20, blank=True, null=True)
    browser_jvm_vendor = models.CharField(max_length=100, blank=True, null=True)
    browser_jvm_version = models.CharField(max_length=20, blank=True, null=True)
    os_arch = models.CharField(max_length=100, blank=True, null=True)
    os_name = models.CharField(max_length=100, blank=True, null=True)
    http_request_user_agent = models.CharField(max_length=100, blank=True, null=True)
    error_code = models.CharField(max_length=1, blank=True, null=True)
    error_text = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_failed'


class MgmtEcmCsaGeneralInfo(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    applet_version = models.CharField(max_length=20, blank=True, null=True)
    custom_class = models.CharField(max_length=1000, blank=True, null=True)
    custom_class_version = models.CharField(max_length=1000, blank=True, null=True)
    target_id_method = models.CharField(max_length=100)
    os_user_name = models.CharField(max_length=500)
    boot_disk_volume_serial_num = models.CharField(max_length=100)
    hostname = models.CharField(max_length=128)
    domain = models.CharField(max_length=500)
    appid = models.CharField(max_length=128)
    target_key1 = models.CharField(max_length=4000, blank=True, null=True)
    target_key2 = models.CharField(max_length=4000, blank=True, null=True)
    target_key3 = models.CharField(max_length=4000, blank=True, null=True)
    proxy_target_name = models.CharField(max_length=256, blank=True, null=True)
    proxy_target_display_name = models.CharField(max_length=256, blank=True, null=True)
    proxy_target_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    worst_rule_status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_general_info'


class MgmtEcmCsaOutOfBox(models.Model):
    status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_out_of_box'


class MgmtEcmCsaRules(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)
    moreinfo = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_rules'
        unique_together = (('ecm_snapshot', 'name'),)


class MgmtEcmCsaSnapshotInfo(models.Model):
    ecm_snapshot = models.ForeignKey('MgmtEcmGenSnapshot', models.DO_NOTHING, primary_key=True)
    display_target_name = models.CharField(max_length=256, blank=True, null=True)
    snapshot_type = models.CharField(max_length=64, blank=True, null=True)
    start_timestamp = models.DateField(blank=True, null=True)
    elapsed_time = models.BigIntegerField()
    status = models.CharField(max_length=1, blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_csa_snapshot_info'


class MgmtEcmGenSnapshot(models.Model):
    snapshot_guid = models.TextField(primary_key=True)  # This field type is a guess.
    snapshot_type = models.CharField(max_length=64)
    start_timestamp = models.DateField()
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_name = models.CharField(max_length=256)
    target_type = models.CharField(max_length=64)
    display_target_name = models.CharField(max_length=256)
    display_target_type = models.CharField(max_length=128)
    elapsed_time = models.BigIntegerField()
    description = models.CharField(max_length=4000, blank=True, null=True)
    is_current = models.CharField(max_length=1)
    message = models.CharField(max_length=4000, blank=True, null=True)
    status = models.CharField(max_length=1)
    creator = models.CharField(max_length=256, blank=True, null=True)
    saved_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_gen_snapshot'


class MgmtEcmHostConfigsToDel(models.Model):
    snapshot_guid = models.TextField(primary_key=True)  # This field type is a guess.
    ts = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_host_configs_to_del'


class MgmtEcmHostpatchComplHist(models.Model):
    group_guid = models.ForeignKey('MgmtEcmHostpatchGroups', models.DO_NOTHING, db_column='group_guid', primary_key=True)
    total_hosts = models.IntegerField()
    compl_hosts = models.IntegerField()
    checked_on = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hostpatch_compl_hist'
        unique_together = (('group_guid', 'checked_on'),)


class MgmtEcmHostpatchGroupRepos(models.Model):
    group_guid = models.ForeignKey('MgmtEcmHostpatchGroups', models.DO_NOTHING, db_column='group_guid')
    repos_guid = models.ForeignKey('MgmtEcmHostpatchRepos', models.DO_NOTHING, db_column='repos_guid')
    group_repos_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hostpatch_group_repos'


class MgmtEcmHostpatchGroups(models.Model):
    group_guid = models.TextField(primary_key=True)  # This field type is a guess.
    maturity_level = models.CharField(max_length=32, blank=True, null=True)
    need_reboot_pkgs = models.CharField(max_length=256, blank=True, null=True)
    mark_rogue_pkgs = models.BooleanField()
    ignored_unknown_pkgs = models.CharField(max_length=256, blank=True, null=True)
    mark_higher_ver_pkg_rogue = models.BooleanField()
    strict_ver_check_pkgs = models.CharField(max_length=256, blank=True, null=True)
    updater_job_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    collector_job_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    creds_type = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hostpatch_groups'


class MgmtEcmHostpatchHostCompl(models.Model):
    host_guid = models.ForeignKey('MgmtEcmHostpatchHosts', models.DO_NOTHING, db_column='host_guid', primary_key=True)
    pkg_name = models.CharField(max_length=256)
    pkg_verspec = models.CharField(max_length=64)
    is_rogue = models.BooleanField()
    is_out_of_date = models.BooleanField()
    needs_reboot = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hostpatch_host_compl'
        unique_together = (('host_guid', 'pkg_name', 'pkg_verspec'),)


class MgmtEcmHostpatchHosts(models.Model):
    host_guid = models.TextField(primary_key=True)  # This field type is a guess.
    group_guid = models.ForeignKey(MgmtEcmHostpatchGroups, models.DO_NOTHING, db_column='group_guid')
    out_of_date_pkgs = models.IntegerField()
    rogue_pkgs = models.IntegerField()
    need_reboot_pkgs = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hostpatch_hosts'


class MgmtEcmHostpatchRepos(models.Model):
    repos_guid = models.TextField(primary_key=True)  # This field type is a guess.
    repos_url = models.CharField(unique=True, max_length=256)
    refresher_job_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hostpatch_repos'


class MgmtEcmHostpatchReposPkgs(models.Model):
    repos_guid = models.ForeignKey(MgmtEcmHostpatchRepos, models.DO_NOTHING, db_column='repos_guid')
    pkg_name = models.CharField(max_length=256)
    pkg_version = models.CharField(max_length=64)
    pkg_release = models.CharField(max_length=32, blank=True, null=True)
    pkg_epoch = models.CharField(max_length=32, blank=True, null=True)
    pkg_arch = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hostpatch_repos_pkgs'
        unique_together = (('repos_guid', 'pkg_name', 'pkg_version', 'pkg_release', 'pkg_epoch', 'pkg_arch'),)


class MgmtEcmHw(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    hostname = models.CharField(max_length=128, blank=True, null=True)
    domain = models.CharField(max_length=500, blank=True, null=True)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    system_config = models.CharField(max_length=4000, blank=True, null=True)
    machine_architecture = models.CharField(max_length=500, blank=True, null=True)
    clock_freq_in_mhz = models.FloatField(blank=True, null=True)
    memory_size_in_mb = models.FloatField(blank=True, null=True)
    avail_memory_size_in_mb = models.FloatField(blank=True, null=True)
    local_disk_space_in_gb = models.FloatField(blank=True, null=True)
    avail_local_disk_space_in_gb = models.FloatField(blank=True, null=True)
    cpu_count = models.IntegerField(blank=True, null=True)
    cpu_board_count = models.IntegerField(blank=True, null=True)
    iocard_count = models.IntegerField(blank=True, null=True)
    fan_count = models.IntegerField(blank=True, null=True)
    power_supply_count = models.IntegerField(blank=True, null=True)
    boot_disk_volume_serial_num = models.CharField(max_length=100, blank=True, null=True)
    system_bios = models.CharField(max_length=100, blank=True, null=True)
    system_serial_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hw'


class MgmtEcmHwCpu(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    freq_in_mhz = models.FloatField(blank=True, null=True)
    ecache_in_mb = models.FloatField(blank=True, null=True)
    impl = models.CharField(max_length=500, blank=True, null=True)
    revision = models.CharField(max_length=2000, blank=True, null=True)
    mask = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hw_cpu'


class MgmtEcmHwIocard(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128)
    freq_in_mhz = models.FloatField(blank=True, null=True)
    bus = models.CharField(max_length=500, blank=True, null=True)
    revision = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hw_iocard'


class MgmtEcmHwNic(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    flags = models.CharField(max_length=1024, blank=True, null=True)
    max_transfer_unit = models.FloatField(blank=True, null=True)
    inet_address = models.CharField(max_length=20, blank=True, null=True)
    mask = models.CharField(max_length=20, blank=True, null=True)
    broadcast_address = models.CharField(max_length=20, blank=True, null=True)
    mac_address = models.CharField(max_length=20, blank=True, null=True)
    hostname_aliases = models.CharField(max_length=4000, blank=True, null=True)
    default_gateway = models.CharField(max_length=20, blank=True, null=True)
    dhcp_enabled = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_hw_nic'


class MgmtEcmLoadedFiles(models.Model):
    file_contents_guid = models.ForeignKey('MgmtEcmSnapshot', models.DO_NOTHING, db_column='file_contents_guid', primary_key=True)
    filename = models.CharField(max_length=1024)
    load_timestamp = models.DateField()
    session_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_loaded_files'


class MgmtEcmMdAllTblColumns(models.Model):
    metadata_id = models.TextField()  # This field type is a guess.
    target_type = models.CharField(max_length=64)
    snapshot_type = models.CharField(max_length=64)
    table_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    ui_name = models.CharField(max_length=256)
    type = models.CharField(max_length=1)
    type_format = models.CharField(max_length=100, blank=True, null=True)
    ui_on = models.CharField(max_length=1)
    compare_on = models.CharField(max_length=1)
    compare_ui_on = models.CharField(max_length=1)
    history_on = models.CharField(max_length=1)
    history_ui_on = models.CharField(max_length=1)
    is_key = models.CharField(max_length=1)
    is_context = models.CharField(max_length=1)
    is_summary = models.CharField(max_length=1)
    is_child_link = models.CharField(max_length=1)
    link_column_name = models.CharField(max_length=30, blank=True, null=True)
    col_order = models.FloatField(blank=True, null=True)
    source_table_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_md_all_tbl_columns'


class MgmtEcmMdHistTbls(models.Model):
    metadata = models.ForeignKey('self', models.DO_NOTHING, primary_key=True)
    target_type = models.CharField(max_length=64)
    snapshot_type = models.CharField(max_length=64)
    name = models.CharField(max_length=30)
    num_hist_ui_keys = models.IntegerField()
    hist_ui_key1 = models.CharField(max_length=30, blank=True, null=True)
    hist_ui_key2 = models.CharField(max_length=30, blank=True, null=True)
    hist_ui_key3 = models.CharField(max_length=30, blank=True, null=True)
    hist_ui_key4 = models.CharField(max_length=30, blank=True, null=True)
    hist_ui_key5 = models.CharField(max_length=30, blank=True, null=True)
    hist_ui_key6 = models.CharField(max_length=30, blank=True, null=True)
    ui_name = models.CharField(max_length=256)
    ui_on = models.CharField(max_length=1)
    compare_on = models.CharField(max_length=1)
    compare_ui_on = models.CharField(max_length=1)
    history_on = models.CharField(max_length=1)
    history_ui_on = models.CharField(max_length=1)
    parent_table_name = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_table_name', blank=True, null=True)
    full_table_path = models.CharField(max_length=1000)
    is_single_row = models.CharField(max_length=1)
    tbl_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_md_hist_tbls'
        unique_together = (('metadata', 'name'),)


class MgmtEcmOs(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    base_version = models.CharField(max_length=100, blank=True, null=True)
    update_level = models.CharField(max_length=100, blank=True, null=True)
    distributor_version = models.CharField(max_length=100, blank=True, null=True)
    max_swap_space_in_mb = models.FloatField(blank=True, null=True)
    address_length_in_bits = models.CharField(max_length=20, blank=True, null=True)
    max_process_virtual_memory = models.FloatField(blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    timezone_delta = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_os'


class MgmtEcmOsComponent(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING)
    name = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    installation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_os_component'


class MgmtEcmOsFilesystem(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING)
    resource_name = models.CharField(max_length=128)
    mount_location = models.CharField(max_length=1024)
    type = models.CharField(max_length=100, blank=True, null=True)
    disk_space_in_gb = models.FloatField(blank=True, null=True)
    avail_disk_space_in_gb = models.FloatField(blank=True, null=True)
    local_drive = models.CharField(max_length=1, blank=True, null=True)
    mount_options = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_os_filesystem'


class MgmtEcmOsProperty(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    source = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_os_property'
        unique_together = (('ecm_snapshot', 'source', 'name'),)


class MgmtEcmOsRegisteredSw(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING)
    id = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=128)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    installation_date = models.DateField(blank=True, null=True)
    installed_location = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    vendor_sw_specific_info = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_os_registered_sw'


class MgmtEcmOsRegisteredSwComp(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING)
    id = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    installation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_os_registered_sw_comp'


class MgmtEcmPatchCache(models.Model):
    aru_id = models.FloatField(primary_key=True)
    status = models.CharField(max_length=31)
    type = models.CharField(max_length=31)
    bug_no = models.FloatField()
    product_id = models.FloatField()
    platform_id = models.FloatField()
    language_id = models.FloatField()
    release = models.CharField(max_length=31)
    abstract = models.CharField(max_length=1000, blank=True, null=True)
    patch_date = models.DateField()
    readme_url = models.CharField(max_length=2000)
    patch_url = models.CharField(max_length=2000)
    comments = models.CharField(max_length=2000, blank=True, null=True)
    file_size = models.FloatField(blank=True, null=True)
    manually_posted = models.CharField(max_length=1)
    last_referenced = models.DateField()
    file_contents = models.BinaryField(blank=True, null=True)
    automated = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_patch_cache'


class MgmtEcmResources(models.Model):
    resource_type = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32)
    default_text = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_resources'
        unique_together = (('resource_type', 'name'),)


class MgmtEcmSavedhostconfig(models.Model):
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    creator = models.CharField(max_length=256, blank=True, null=True)
    hostconfig_contents_guid = models.ForeignKey('MgmtEcmSnapshot', models.DO_NOTHING, db_column='hostconfig_contents_guid', primary_key=True)
    filename = models.CharField(max_length=1024, blank=True, null=True)
    load_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_savedhostconfig'


class MgmtEcmSnapComponentInfo(models.Model):
    snapshot_guid = models.ForeignKey('MgmtEcmSnapshot', models.DO_NOTHING, db_column='snapshot_guid', primary_key=True)
    component_name = models.CharField(max_length=64)
    collection_status = models.CharField(max_length=32)
    collection_message = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_snap_component_info'
        unique_together = (('snapshot_guid', 'component_name'),)


class MgmtEcmSnapshot(models.Model):
    snapshot_guid = models.TextField(primary_key=True)  # This field type is a guess.
    snapshot_type = models.CharField(max_length=64)
    start_timestamp = models.DateField()
    target_name = models.CharField(max_length=256)
    target_type = models.CharField(max_length=64)
    display_target_name = models.CharField(max_length=256)
    display_target_type = models.CharField(max_length=128)
    elapsed_time = models.BigIntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    is_current = models.CharField(max_length=1)
    snapshot_type_version = models.CharField(max_length=16)
    collection_error_stream = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_snapshot'


class MgmtEcmSnapshotMdColumns(models.Model):
    metadata = models.ForeignKey('self', models.DO_NOTHING, primary_key=True)
    table_name = models.ForeignKey('self', models.DO_NOTHING, db_column='table_name')
    name = models.CharField(max_length=30)
    ui_name = models.CharField(max_length=256)
    type = models.CharField(max_length=1)
    type_format = models.CharField(max_length=100, blank=True, null=True)
    ui_on = models.CharField(max_length=1)
    compare_on = models.CharField(max_length=1)
    compare_ui_on = models.CharField(max_length=1)
    history_on = models.CharField(max_length=1)
    history_ui_on = models.CharField(max_length=1)
    is_key = models.CharField(max_length=1)
    is_context = models.CharField(max_length=1)
    is_summary = models.CharField(max_length=1)
    is_child_link = models.CharField(max_length=1)
    link_column_name = models.ForeignKey('self', models.DO_NOTHING, db_column='link_column_name', blank=True, null=True)
    col_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_snapshot_md_columns'
        unique_together = (('metadata', 'table_name', 'name'),)


class MgmtEcmSnapshotMdTables(models.Model):
    metadata = models.ForeignKey('self', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=30)
    ui_name = models.CharField(max_length=256)
    ui_on = models.CharField(max_length=1)
    compare_on = models.CharField(max_length=1)
    compare_ui_on = models.CharField(max_length=1)
    history_on = models.CharField(max_length=1)
    history_ui_on = models.CharField(max_length=1)
    parent_table_name = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_table_name', blank=True, null=True)
    full_table_path = models.CharField(max_length=1000)
    is_single_row = models.CharField(max_length=1)
    tbl_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_snapshot_md_tables'
        unique_together = (('metadata', 'name'),)


class MgmtEcmSnapshotMetadata(models.Model):
    snapshot_type = models.CharField(max_length=64)
    target_type = models.CharField(primary_key=True, max_length=64)
    kind = models.CharField(max_length=1)
    metadata_id = models.TextField()  # This field type is a guess.
    ui_name = models.CharField(max_length=256)
    ui_on = models.CharField(max_length=1)
    compare_on = models.CharField(max_length=1)
    compare_ui_on = models.CharField(max_length=1)
    history_on = models.CharField(max_length=1)
    history_ui_on = models.CharField(max_length=1)
    link_table_name = models.CharField(max_length=30, blank=True, null=True)
    after_load_proc_name = models.CharField(max_length=200, blank=True, null=True)
    after_import_proc_name = models.CharField(max_length=200, blank=True, null=True)
    metadata_version = models.CharField(max_length=16, blank=True, null=True)
    view_url = models.CharField(max_length=4000, blank=True, null=True)
    compare_url = models.CharField(max_length=4000, blank=True, null=True)
    history_url = models.CharField(max_length=4000, blank=True, null=True)
    same_target_compare = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_snapshot_metadata'
        unique_together = (('kind', 'metadata_id'), ('target_type', 'snapshot_type', 'kind'),)


class MgmtEcmUlnChAdv(models.Model):
    channel_guid = models.ForeignKey('MgmtEcmUlnChannels', models.DO_NOTHING, db_column='channel_guid')
    advisory_id = models.CharField(max_length=256)
    summary = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_uln_ch_adv'
        unique_together = (('channel_guid', 'advisory_id'),)


class MgmtEcmUlnChannelPkgs(models.Model):
    channel_guid = models.ForeignKey('MgmtEcmUlnChannels', models.DO_NOTHING, db_column='channel_guid')
    pkg_name = models.CharField(max_length=256)
    pkg_version = models.CharField(max_length=64)
    pkg_release = models.CharField(max_length=32, blank=True, null=True)
    pkg_epoch = models.CharField(max_length=32, blank=True, null=True)
    pkg_arch = models.CharField(max_length=32)
    advisory_id = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_uln_channel_pkgs'
        unique_together = (('pkg_name', 'pkg_release', 'pkg_version', 'pkg_epoch', 'pkg_arch', 'advisory_id'),)


class MgmtEcmUlnChannels(models.Model):
    channel_guid = models.TextField(primary_key=True)  # This field type is a guess.
    channel_name = models.CharField(unique=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_uln_channels'


class MgmtEcmUlnSsChannels(models.Model):
    stage_server_guid = models.ForeignKey('MgmtEcmUlnStageServers', models.DO_NOTHING, db_column='stage_server_guid')
    channel_guid = models.ForeignKey(MgmtEcmUlnChannels, models.DO_NOTHING, db_column='channel_guid')

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_uln_ss_channels'
        unique_together = (('stage_server_guid', 'channel_guid'),)


class MgmtEcmUlnStageServers(models.Model):
    stage_server_guid = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_ecm_uln_stage_servers'


class MgmtEmdPing(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    status = models.FloatField(blank=True, null=True)
    last_heartbeat_ts = models.DateField(blank=True, null=True)
    last_heartbeat_utc = models.DateField(blank=True, null=True)
    clean_heartbeat_utc = models.DateField()
    status_sync_utc = models.DateField()
    emd_uptime_utc = models.DateField()
    unrch_start_ts = models.DateField(blank=True, null=True)
    max_inactive_time = models.FloatField(blank=True, null=True)
    down_reason_code = models.FloatField(blank=True, null=True)
    down_reason_msg = models.CharField(max_length=1024, blank=True, null=True)
    heartbeat_recorder_url = models.CharField(max_length=256, blank=True, null=True)
    ping_job_name = models.CharField(max_length=64, blank=True, null=True)
    job_submit_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emd_ping'


class MgmtEmdPingCheck(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    last_checked_utc = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emd_ping_check'


class MgmtEmxCellCConfig(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    realmname = models.CharField(max_length=200, blank=True, null=True)
    id = models.CharField(max_length=200, blank=True, null=True)
    makemodel = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    bmctype = models.CharField(max_length=200, blank=True, null=True)
    ipblock = models.CharField(max_length=200, blank=True, null=True)
    fancount = models.FloatField(blank=True, null=True)
    powercount = models.FloatField(blank=True, null=True)
    metrichistorydays = models.FloatField(blank=True, null=True)
    snmpsubscriber = models.CharField(max_length=200, blank=True, null=True)
    smtpserver = models.CharField(max_length=200, blank=True, null=True)
    smtpport = models.CharField(max_length=200, blank=True, null=True)
    ipaddress1 = models.CharField(max_length=200, blank=True, null=True)
    ipaddress2 = models.CharField(max_length=200, blank=True, null=True)
    ipaddress3 = models.CharField(max_length=200, blank=True, null=True)
    ipaddress4 = models.CharField(max_length=200, blank=True, null=True)
    kernelversion = models.CharField(max_length=200, blank=True, null=True)
    ossversion = models.CharField(max_length=200, blank=True, null=True)
    interconnectcount = models.FloatField(blank=True, null=True)
    cpucount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emx_cell_c_config'


class MgmtEmxCellCdConfig(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=200)
    cellname = models.CharField(max_length=200)
    realmname = models.CharField(max_length=200)
    status = models.CharField(max_length=200, blank=True, null=True)
    cdsize = models.CharField(max_length=200, blank=True, null=True)
    lun = models.CharField(max_length=200, blank=True, null=True)
    errorcount = models.FloatField(blank=True, null=True)
    freespace = models.FloatField(blank=True, null=True)
    devicepartition = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emx_cell_cd_config'
        unique_together = (('ecm_snapshot', 'name', 'cellname', 'realmname'),)


class MgmtEmxCellGdConfig(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=200)
    cellname = models.CharField(max_length=200)
    realmname = models.CharField(max_length=200)
    status = models.CharField(max_length=200, blank=True, null=True)
    gdsize = models.FloatField(blank=True, null=True)
    creationtime = models.CharField(max_length=200, blank=True, null=True)
    celldisk = models.CharField(max_length=200)
    offset = models.FloatField(blank=True, null=True)
    errorcount = models.FloatField(blank=True, null=True)
    availableto = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emx_cell_gd_config'
        unique_together = (('ecm_snapshot', 'name', 'cellname', 'realmname', 'celldisk'),)


class MgmtEmxCellIormConfig(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=200)
    cellname = models.CharField(max_length=200)
    realmname = models.CharField(max_length=200)
    status = models.CharField(max_length=200, blank=True, null=True)
    latency = models.CharField(max_length=200, blank=True, null=True)
    directivetype = models.CharField(max_length=200)
    dbcatname = models.CharField(max_length=200)
    level1 = models.CharField(max_length=200, blank=True, null=True)
    level2 = models.CharField(max_length=200, blank=True, null=True)
    level3 = models.CharField(max_length=200, blank=True, null=True)
    level4 = models.CharField(max_length=200, blank=True, null=True)
    level5 = models.CharField(max_length=200, blank=True, null=True)
    level6 = models.CharField(max_length=200, blank=True, null=True)
    level7 = models.CharField(max_length=200, blank=True, null=True)
    level8 = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emx_cell_iorm_config'
        unique_together = (('ecm_snapshot', 'name', 'cellname', 'realmname', 'directivetype', 'dbcatname'),)


class MgmtEmxCellLConfig(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=200)
    cellname = models.CharField(max_length=200)
    realmname = models.CharField(max_length=200)
    status = models.CharField(max_length=200, blank=True, null=True)
    id = models.CharField(max_length=200, blank=True, null=True)
    celldisk = models.CharField(max_length=200, blank=True, null=True)
    errorcount = models.FloatField(blank=True, null=True)
    raidlevel = models.CharField(max_length=200, blank=True, null=True)
    devicename = models.CharField(max_length=200, blank=True, null=True)
    lunsize = models.FloatField(blank=True, null=True)
    lunuid = models.CharField(max_length=200, blank=True, null=True)
    lunautocreate = models.CharField(max_length=200, blank=True, null=True)
    physicaldisks = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emx_cell_l_config'
        unique_together = (('ecm_snapshot', 'name', 'cellname', 'realmname'),)


class MgmtEmxCellPdConfig(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=200)
    cellname = models.CharField(max_length=200)
    realmname = models.CharField(max_length=200)
    status = models.CharField(max_length=200, blank=True, null=True)
    id = models.CharField(max_length=200, blank=True, null=True)
    makemodel = models.CharField(max_length=200, blank=True, null=True)
    luns = models.CharField(max_length=1000, blank=True, null=True)
    errorcount = models.CharField(max_length=200, blank=True, null=True)
    ctrlfirmware = models.CharField(max_length=200, blank=True, null=True)
    ctrlhwversion = models.CharField(max_length=200, blank=True, null=True)
    physinterface = models.CharField(max_length=200, blank=True, null=True)
    physfirmware = models.CharField(max_length=200, blank=True, null=True)
    physsize = models.CharField(max_length=200, blank=True, null=True)
    physserial = models.CharField(max_length=200, blank=True, null=True)
    physusetype = models.CharField(max_length=200, blank=True, null=True)
    physport = models.CharField(max_length=200, blank=True, null=True)
    physinserttime = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_emx_cell_pd_config'
        unique_together = (('ecm_snapshot', 'name', 'cellname', 'realmname'),)


class MgmtEnterpriseCredentials(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    credential_set_name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=256)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_enterprise_credentials'
        unique_together = (('target_type', 'credential_set_name', 'user_name'),)


class MgmtErrorMaster(models.Model):
    error_start = models.FloatField(primary_key=True)
    error_end = models.FloatField()
    is_recoverable = models.NullBooleanField()
    module = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_error_master'
        unique_together = (('error_start', 'error_end'),)


class MgmtEsaReport(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    principal = models.CharField(max_length=512)
    object_name = models.CharField(max_length=512)
    report_name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mgmt_esa_report'
        unique_together = (('ecm_snapshot', 'principal', 'object_name', 'report_name'),)


class MgmtFailedConfigActivities(models.Model):
    txn_id = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    param_name = models.CharField(max_length=64)
    param_value = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_failed_config_activities'
        unique_together = (('target_guid', 'txn_id', 'param_name'),)


class MgmtFailoverCallbacks(models.Model):
    callback_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_failover_callbacks'


class MgmtFailoverTable(models.Model):
    failover_id = models.FloatField(primary_key=True)
    last_time_stamp = models.DateField(blank=True, null=True)
    host_url = models.CharField(max_length=256, blank=True, null=True)
    heartbeat_interval = models.IntegerField(blank=True, null=True)
    last_time_stamp_utc = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_failover_table'


class MgmtFbpPatchingGuids(models.Model):
    procedure_guid = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_fbp_patching_guids'


class MgmtFeaturePatches(models.Model):
    patch_id = models.FloatField(primary_key=True)
    family_id = models.FloatField(blank=True, null=True)
    product_id = models.FloatField()
    release_id = models.FloatField()
    platform_id = models.FloatField()
    language_id = models.FloatField()
    patch_type = models.CharField(max_length=32, blank=True, null=True)
    created_on = models.DateField(blank=True, null=True)
    patch_desc = models.CharField(max_length=256, blank=True, null=True)
    patch_features = models.CharField(max_length=256, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_feature_patches'
        unique_together = (('patch_id', 'product_id', 'release_id', 'platform_id', 'language_id'),)


class MgmtFeaturesMapping(models.Model):
    feature_name = models.CharField(primary_key=True, max_length=64)
    product_id = models.FloatField()
    release_id = models.FloatField()
    platform_id = models.FloatField()
    product_feature = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_features_mapping'
        unique_together = (('feature_name', 'product_id', 'release_id', 'platform_id'),)


class MgmtFlatRoleGrants(models.Model):
    role_grantee = models.CharField(primary_key=True, max_length=256)
    role_name = models.ForeignKey('MgmtRoles', models.DO_NOTHING, db_column='role_name')

    class Meta:
        managed = False
        db_table = 'mgmt_flat_role_grants'
        unique_together = (('role_grantee', 'role_name'),)


class MgmtFlatTargetAssoc(models.Model):
    source_target_guid = models.TextField()  # This field type is a guess.
    assoc_target_guid = models.TextField()  # This field type is a guess.
    is_membership = models.NullBooleanField()
    is_connected = models.NullBooleanField()
    membership_count = models.IntegerField(blank=True, null=True)
    ref_count = models.IntegerField(blank=True, null=True)
    prop_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_flat_target_assoc'


class MgmtGensvcAvailBeacons(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    beacon_target_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_avail_beacons'
        unique_together = (('target_guid', 'beacon_target_guid'),)


class MgmtGensvcAvailConfig(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    avail_enabled = models.BooleanField()
    eval_logic = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_avail_config'


class MgmtGensvcAvailEvents(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    test_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    beacon_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    event_code = models.IntegerField()
    event_description = models.CharField(max_length=2000, blank=True, null=True)
    event_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_avail_events'


class MgmtGensvcAvailJob(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    test_guid = models.TextField()  # This field type is a guess.
    next_run = models.DateField()
    in_error = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_avail_job'
        unique_together = (('target_guid', 'test_guid'),)


class MgmtGensvcAvailTests(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    test_guid = models.TextField()  # This field type is a guess.
    test_name = models.CharField(max_length=64)
    test_type = models.CharField(max_length=64)
    metric_guid = models.TextField()  # This field type is a guess.
    avail_test = models.NullBooleanField()
    monit_status = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_avail_tests'
        unique_together = (('target_guid', 'test_guid'),)


class MgmtGensvcJobsDetails(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    operation_guid = models.TextField()  # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_owner = models.CharField(max_length=256, blank=True, null=True)
    execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution_status = models.FloatField(blank=True, null=True)
    submission_timestamp = models.DateField()
    last_updated_timestamp = models.DateField(blank=True, null=True)
    error_message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_jobs_details'
        unique_together = (('target_guid', 'operation_guid'),)


class MgmtGensvcTestAvail(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    test_guid = models.TextField()  # This field type is a guess.
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_status = models.FloatField()
    start_collection_timestamp = models.DateField()
    end_collection_timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_test_avail'
        unique_together = (('target_guid', 'test_guid', 'start_collection_timestamp', 'current_status'),)


class MgmtGensvcTestAvailMarker(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    test_guid = models.TextField()  # This field type is a guess.
    marker_timestamp = models.DateField()
    marker_avail_status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_test_avail_marker'
        unique_together = (('target_guid', 'test_guid'),)


class MgmtGensvcTestCurAvail(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    test_guid = models.TextField()  # This field type is a guess.
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_status = models.FloatField()
    start_collection_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_test_cur_avail'
        unique_together = (('target_guid', 'test_guid'),)


class MgmtGensvcTmplVars(models.Model):
    template_guid = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=512)
    default_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_tmpl_vars'
        unique_together = (('template_guid', 'name'),)


class MgmtGensvcUpdbcnJob(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    operation_guid = models.TextField()  # This field type is a guess.
    template_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    beacon_target_guid = models.TextField()  # This field type is a guess.
    beacon_name = models.CharField(max_length=256, blank=True, null=True)
    action_description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_updbcn_job'
        unique_together = (('target_guid', 'operation_guid', 'beacon_target_guid'),)


class MgmtGensvcUpdbcnJobTests(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    operation_guid = models.TextField()  # This field type is a guess.
    test_guid = models.TextField()  # This field type is a guess.
    test_name = models.CharField(max_length=128, blank=True, null=True)
    test_type = models.CharField(max_length=128, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_gensvc_updbcn_job_tests'
        unique_together = (('target_guid', 'operation_guid', 'test_guid'),)


class MgmtGroupChart(models.Model):
    comp_chart_guid = models.TextField()  # This field type is a guess.
    comp_target_guid = models.TextField()  # This field type is a guess.
    chart_type = models.BooleanField()
    member_metric_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    display_order = models.FloatField(blank=True, null=True)
    targets_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_group_chart'


class MgmtGroupChartSeltargets(models.Model):
    comp_chart_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_group_chart_seltargets'


class MgmtGroupCustomColumns(models.Model):
    composite_target_guid = models.TextField()  # This field type is a guess.
    column_type = models.IntegerField(blank=True, null=True)
    member_metric_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    property_name = models.CharField(max_length=64, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    abbreviation = models.CharField(max_length=64, blank=True, null=True)
    display_order = models.FloatField(blank=True, null=True)
    view_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_group_custom_columns'


class MgmtGroupDefaultChart(models.Model):
    comp_target_type = models.CharField(primary_key=True, max_length=64)
    chart_type = models.BooleanField()
    member_target_type = models.CharField(max_length=64)
    member_metric_name = models.CharField(max_length=64)
    member_metric_column = models.CharField(max_length=64)
    targets_count = models.IntegerField(blank=True, null=True)
    min_column = models.NullBooleanField()
    max_column = models.NullBooleanField()
    avg_column = models.NullBooleanField()
    sum_column = models.NullBooleanField()
    stdev_column = models.NullBooleanField()
    display_order = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_group_default_chart'
        unique_together = (('comp_target_type', 'chart_type', 'member_target_type', 'member_metric_name', 'member_metric_column'),)


class MgmtGroupSummaryChartDef(models.Model):
    comp_chart_guid = models.TextField()  # This field type is a guess.
    comp_target_guid = models.TextField()  # This field type is a guess.
    comp_metric_guid = models.TextField()  # This field type is a guess.
    min_column = models.NullBooleanField()
    max_column = models.NullBooleanField()
    avg_column = models.NullBooleanField()
    sum_column = models.NullBooleanField()
    stdev_column = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_group_summary_chart_def'


class MgmtHaBackup(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=23, blank=True, null=True)
    session_key = models.FloatField(blank=True, null=True)
    session_recid = models.FloatField(blank=True, null=True)
    session_stamp = models.FloatField(blank=True, null=True)
    command_id = models.CharField(max_length=33, blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    time_taken_display = models.CharField(max_length=4000, blank=True, null=True)
    input_type = models.CharField(max_length=13, blank=True, null=True)
    output_device_type = models.CharField(max_length=17, blank=True, null=True)
    input_bytes_display = models.CharField(max_length=4000, blank=True, null=True)
    output_bytes_display = models.CharField(max_length=4000, blank=True, null=True)
    output_bytes_per_sec_display = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_backup'


class MgmtHaClsIntrConn(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    ic_name = models.CharField(max_length=50)
    ic_node = models.CharField(max_length=100)
    ic_subnet = models.CharField(max_length=16, blank=True, null=True)
    ic_ip = models.CharField(max_length=16, blank=True, null=True)
    ic_public = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_cls_intr_conn'
        unique_together = (('ecm_snapshot', 'ic_name', 'ic_node'),)


class MgmtHaDgTargetSummary(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField(blank=True, null=True)
    source_type = models.CharField(max_length=2, blank=True, null=True)
    row_type = models.CharField(max_length=2, blank=True, null=True)
    using_broker = models.CharField(max_length=4, blank=True, null=True)
    active_stby = models.CharField(max_length=4, blank=True, null=True)
    db_unique_name = models.CharField(max_length=64, blank=True, null=True)
    db_id = models.FloatField(blank=True, null=True)
    prmy_db_unique_name = models.CharField(max_length=64, blank=True, null=True)
    prmy_db_id = models.FloatField(blank=True, null=True)
    role = models.CharField(max_length=64, blank=True, null=True)
    stby_list = models.CharField(max_length=1024, blank=True, null=True)
    protection_mode = models.CharField(max_length=256, blank=True, null=True)
    fsfo_status = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=1024, blank=True, null=True)
    transport_lag = models.FloatField(blank=True, null=True)
    apply_lag = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_dg_target_summary'


class MgmtHaFilesEcm(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=64)
    totalsize = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_files_ecm'
        unique_together = (('ecm_snapshot', 'name'),)


class MgmtHaInfoEcm(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    dbid = models.FloatField(blank=True, null=True)
    log_mode = models.CharField(max_length=12, blank=True, null=True)
    force_logging = models.CharField(max_length=3, blank=True, null=True)
    database_role = models.CharField(max_length=16, blank=True, null=True)
    flashback_on = models.CharField(max_length=18, blank=True, null=True)
    supplemental_logging = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_info_ecm'


class MgmtHaInitParamsEcm(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_init_params_ecm'
        unique_together = (('ecm_snapshot', 'name'),)


class MgmtHaMttr(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField(blank=True, null=True)
    estimated_mttr = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_mttr'


class MgmtHaRacIntrConn(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    ic_name = models.CharField(max_length=50)
    ic_ip = models.CharField(max_length=16)
    ic_public = models.CharField(max_length=10, blank=True, null=True)
    ic_source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_rac_intr_conn'
        unique_together = (('ecm_snapshot', 'ic_name', 'ic_ip'),)


class MgmtHaRmanConfigEcm(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=65)
    value = models.CharField(max_length=1025, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ha_rman_config_ecm'
        unique_together = (('ecm_snapshot', 'name'),)


class MgmtHcCpuDetails(models.Model):
    snapshot_guid = models.ForeignKey('MgmtHcSystemSummary', models.DO_NOTHING, db_column='snapshot_guid')
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    freq_in_mhz = models.FloatField(blank=True, null=True)
    ecache_in_mb = models.FloatField(blank=True, null=True)
    impl = models.CharField(max_length=500, blank=True, null=True)
    revision = models.CharField(max_length=2000, blank=True, null=True)
    mask = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_cpu_details'


class MgmtHcFsMountDetails(models.Model):
    snapshot_guid = models.ForeignKey('MgmtHcOsSummary', models.DO_NOTHING, db_column='snapshot_guid')
    resource_name = models.CharField(max_length=128)
    mount_location = models.CharField(max_length=1024)
    type = models.CharField(max_length=100, blank=True, null=True)
    mount_options = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_fs_mount_details'


class MgmtHcHardwareMaster(models.Model):
    snapshot_guid = models.ForeignKey('MgmtHcSystemSummary', models.DO_NOTHING, db_column='snapshot_guid', primary_key=True)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    system_config = models.CharField(max_length=4000, blank=True, null=True)
    machine_architecture = models.CharField(max_length=500, blank=True, null=True)
    clock_freq_in_mhz = models.FloatField(blank=True, null=True)
    memory_size_in_mb = models.FloatField(blank=True, null=True)
    local_disk_space_in_gb = models.FloatField(blank=True, null=True)
    cpu_count = models.FloatField(blank=True, null=True)
    cpu_board_count = models.FloatField(blank=True, null=True)
    iocard_count = models.FloatField(blank=True, null=True)
    fan_count = models.FloatField(blank=True, null=True)
    power_supply_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_hardware_master'


class MgmtHcIocardDetails(models.Model):
    snapshot_guid = models.ForeignKey('MgmtHcSystemSummary', models.DO_NOTHING, db_column='snapshot_guid')
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128)
    freq_in_mhz = models.FloatField(blank=True, null=True)
    bus = models.CharField(max_length=500, blank=True, null=True)
    revision = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_iocard_details'


class MgmtHcNicDetails(models.Model):
    snapshot_guid = models.ForeignKey('MgmtHcSystemSummary', models.DO_NOTHING, db_column='snapshot_guid')
    name = models.CharField(max_length=128, blank=True, null=True)
    flags = models.CharField(max_length=1024, blank=True, null=True)
    max_transfer_unit = models.FloatField(blank=True, null=True)
    inet_address = models.CharField(max_length=20, blank=True, null=True)
    mask = models.CharField(max_length=20, blank=True, null=True)
    broadcast_address = models.CharField(max_length=20, blank=True, null=True)
    mac_address = models.CharField(max_length=20, blank=True, null=True)
    hostname_aliases = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_nic_details'


class MgmtHcOsComponents(models.Model):
    snapshot_guid = models.ForeignKey('MgmtHcOsSummary', models.DO_NOTHING, db_column='snapshot_guid')
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    installation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_os_components'


class MgmtHcOsProperties(models.Model):
    snapshot_guid = models.ForeignKey('MgmtHcOsSummary', models.DO_NOTHING, db_column='snapshot_guid', primary_key=True)
    type = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_os_properties'
        unique_together = (('snapshot_guid', 'type', 'name'),)


class MgmtHcOsSummary(models.Model):
    snapshot_guid = models.ForeignKey(MgmtEcmSnapshot, models.DO_NOTHING, db_column='snapshot_guid', primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    base_version = models.CharField(max_length=100, blank=True, null=True)
    update_level = models.CharField(max_length=100, blank=True, null=True)
    distributor_version = models.CharField(max_length=100, blank=True, null=True)
    max_swap_space_in_mb = models.FloatField(blank=True, null=True)
    address_length_in_bits = models.CharField(max_length=20, blank=True, null=True)
    patches = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_hc_os_summary'


class MgmtHcSystemSummary(models.Model):
    snapshot_guid = models.ForeignKey(MgmtEcmSnapshot, models.DO_NOTHING, db_column='snapshot_guid', primary_key=True)
    hostname = models.CharField(max_length=128)
    domain = models.CharField(max_length=500, blank=True, null=True)
    cc_name = models.CharField(max_length=128, blank=True, null=True)
    cc_partner_info = models.CharField(max_length=2000, blank=True, null=True)
    cc_software_version = models.CharField(max_length=100, blank=True, null=True)
    cc_software_build_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_system_summary'


class MgmtHcVendorSwComponents(models.Model):
    vendor_software_guid = models.ForeignKey('MgmtHcVendorSwSummary', models.DO_NOTHING, db_column='vendor_software_guid')
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    installation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_vendor_sw_components'


class MgmtHcVendorSwSummary(models.Model):
    vendor_software_guid = models.TextField(primary_key=True)  # This field type is a guess.
    snapshot_guid = models.ForeignKey(MgmtEcmSnapshot, models.DO_NOTHING, db_column='snapshot_guid')
    name = models.CharField(max_length=128)
    vendor_name = models.CharField(max_length=128, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    installation_date = models.DateField(blank=True, null=True)
    installed_location = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    vendor_software_specific_info = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_hc_vendor_sw_summary'


class MgmtHostCredentials(models.Model):
    host_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_type = models.CharField(max_length=64)
    credential_set_name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=256)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_host_credentials'
        unique_together = (('host_guid', 'target_type', 'credential_set_name', 'user_name'),)


class MgmtHttpSessionCallbacks(models.Model):
    object_type = models.CharField(primary_key=True, max_length=32)
    callback_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_http_session_callbacks'
        unique_together = (('object_type', 'callback_name'),)


class MgmtHttpSessionObjects(models.Model):
    session_id = models.CharField(primary_key=True, max_length=256)
    oms_failover_id = models.FloatField(blank=True, null=True)
    object_type = models.CharField(max_length=32)
    object_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_http_session_objects'
        unique_together = (('session_id', 'object_type', 'object_guid'),)


class MgmtIndexSizes(models.Model):
    index_name = models.CharField(max_length=30)
    table_name = models.CharField(max_length=30)
    collection_timestamp = models.DateField(primary_key=True)
    allocated_size = models.FloatField(blank=True, null=True)
    space_used = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_index_sizes'
        unique_together = (('collection_timestamp', 'index_name', 'table_name'),)


class MgmtInvComponent(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    version = models.CharField(max_length=64)
    container_guid = models.ForeignKey('MgmtInvContainer', models.DO_NOTHING, db_column='container_guid')
    component_guid = models.TextField()  # This field type is a guess.
    description = models.CharField(max_length=1024, blank=True, null=True)
    external_name = models.CharField(max_length=128)
    languages = models.CharField(max_length=1024, blank=True, null=True)
    installed_location = models.CharField(max_length=1024, blank=True, null=True)
    installer_version = models.CharField(max_length=64, blank=True, null=True)
    min_deinstaller_version = models.CharField(max_length=64, blank=True, null=True)
    is_top_level = models.CharField(max_length=1)
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_component'
        unique_together = (('name', 'version', 'container_guid'),)


class MgmtInvComponentPatch(models.Model):
    component_guid = models.ForeignKey(MgmtInvComponent, models.DO_NOTHING, db_column='component_guid', primary_key=True)
    patch_guid = models.ForeignKey('MgmtInvPatch', models.DO_NOTHING, db_column='patch_guid')

    class Meta:
        managed = False
        db_table = 'mgmt_inv_component_patch'
        unique_together = (('component_guid', 'patch_guid'),)


class MgmtInvContainer(models.Model):
    container_type = models.CharField(max_length=64)
    container_name = models.CharField(max_length=64)
    snapshot_guid = models.ForeignKey(MgmtEcmSnapshot, models.DO_NOTHING, db_column='snapshot_guid')
    container_guid = models.TextField(primary_key=True)  # This field type is a guess.
    container_location = models.CharField(max_length=128)
    oui_platform = models.IntegerField(blank=True, null=True)
    is_clonable = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_container'
        unique_together = (('snapshot_guid', 'container_location'),)


class MgmtInvContainerProperty(models.Model):
    container_guid = models.ForeignKey(MgmtInvContainer, models.DO_NOTHING, db_column='container_guid', primary_key=True)
    property_name = models.CharField(max_length=64)
    property_value = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_container_property'
        unique_together = (('container_guid', 'property_name'),)


class MgmtInvDependencyRule(models.Model):
    dependee_guid = models.ForeignKey(MgmtInvComponent, models.DO_NOTHING, db_column='dependee_guid', primary_key=True)
    referencer_guid = models.ForeignKey(MgmtInvComponent, models.DO_NOTHING, db_column='referencer_guid')
    dependency_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_dependency_rule'
        unique_together = (('dependee_guid', 'referencer_guid'),)


class MgmtInvFile(models.Model):
    file_name = models.CharField(max_length=1024)
    container_guid = models.ForeignKey(MgmtInvContainer, models.DO_NOTHING, db_column='container_guid', primary_key=True)
    parent_file_name = models.CharField(max_length=1024, blank=True, null=True)
    last_patch_guid = models.ForeignKey('MgmtInvPatch', models.DO_NOTHING, db_column='last_patch_guid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_file'
        unique_together = (('container_guid', 'file_name'),)


class MgmtInvPatch(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    container_guid = models.ForeignKey(MgmtInvContainer, models.DO_NOTHING, db_column='container_guid')
    patch_guid = models.TextField(unique=True)  # This field type is a guess.
    timestamp = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    is_rollbackable = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_patch'
        unique_together = (('id', 'container_guid'),)


class MgmtInvPatchFixedBug(models.Model):
    patch_guid = models.ForeignKey(MgmtInvPatch, models.DO_NOTHING, db_column='patch_guid', primary_key=True)
    bug_number = models.CharField(max_length=10)
    component_guid = models.ForeignKey(MgmtInvComponent, models.DO_NOTHING, db_column='component_guid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_patch_fixed_bug'
        unique_together = (('patch_guid', 'bug_number'),)


class MgmtInvPatchedFile(models.Model):
    file_name = models.CharField(max_length=1024)
    patch_guid = models.ForeignKey(MgmtInvPatch, models.DO_NOTHING, db_column='patch_guid', primary_key=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_patched_file'
        unique_together = (('patch_guid', 'file_name'),)


class MgmtInvPatchedFileComp(models.Model):
    component_guid = models.ForeignKey(MgmtInvComponent, models.DO_NOTHING, db_column='component_guid', primary_key=True)
    file_name = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_patched_file_comp'
        unique_together = (('component_guid', 'file_name'),)


class MgmtInvPatchset(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    version = models.CharField(max_length=64)
    container_guid = models.ForeignKey(MgmtInvContainer, models.DO_NOTHING, db_column='container_guid')
    patchset_guid = models.TextField(unique=True)  # This field type is a guess.
    description = models.CharField(max_length=1024, blank=True, null=True)
    external_name = models.CharField(max_length=128)
    installer_version = models.CharField(max_length=64, blank=True, null=True)
    min_deinstaller_version = models.CharField(max_length=64, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_patchset'
        unique_together = (('name', 'version', 'container_guid'),)


class MgmtInvSummary(models.Model):
    snapshot_guid = models.ForeignKey(MgmtEcmSnapshot, models.DO_NOTHING, db_column='snapshot_guid')
    comp_external_name = models.CharField(max_length=128)
    comp_version = models.CharField(max_length=64)
    container_location = models.CharField(max_length=128)
    container_guid = models.TextField()  # This field type is a guess.
    is_patched = models.BooleanField()
    map_target_type = models.CharField(max_length=64)
    map_property_name = models.CharField(max_length=64, blank=True, null=True)
    map_property_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_summary'


class MgmtInvVersionedPatch(models.Model):
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=64)
    component_guid = models.ForeignKey(MgmtInvComponent, models.DO_NOTHING, db_column='component_guid', primary_key=True)
    patchset_guid = models.ForeignKey(MgmtInvPatchset, models.DO_NOTHING, db_column='patchset_guid', blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    external_name = models.CharField(max_length=128)
    languages = models.CharField(max_length=1024, blank=True, null=True)
    installed_location = models.CharField(max_length=1024, blank=True, null=True)
    installer_version = models.CharField(max_length=64, blank=True, null=True)
    min_deinstaller_version = models.CharField(max_length=64, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_inv_versioned_patch'


class MgmtIpElemDefaultParams(models.Model):
    element_name_nlsid = models.CharField(primary_key=True, max_length=256)
    element_type_nlsid = models.CharField(max_length=100)
    param = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_elem_default_params'
        unique_together = (('element_name_nlsid', 'element_type_nlsid', 'param'),)


class MgmtIpElemParamClasses(models.Model):
    element_name_nlsid = models.CharField(primary_key=True, max_length=256)
    element_type_nlsid = models.CharField(max_length=100)
    element_param_class = models.CharField(max_length=1000)
    display_order = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_ip_elem_param_classes'
        unique_together = (('element_name_nlsid', 'element_type_nlsid', 'element_param_class', 'display_order'),)


class MgmtIpElemTargetTypes(models.Model):
    element_type_nlsid = models.CharField(primary_key=True, max_length=100)
    target_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_elem_target_types'
        unique_together = (('element_type_nlsid', 'target_type'),)


class MgmtIpEmailReport(models.Model):
    report_guid = models.TextField()  # This field type is a guess.
    email_enabled = models.NullBooleanField()
    email_subject = models.CharField(max_length=300, blank=True, null=True)
    email_sender = models.CharField(max_length=100)
    email_recipients = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_email_report'


class MgmtIpPurgePolicy(models.Model):
    purge_policy_guid = models.TextField()  # This field type is a guess.
    report_guid = models.TextField()  # This field type is a guess.
    keep_num_versions = models.IntegerField(blank=True, null=True)
    retention_interval = models.IntegerField(blank=True, null=True)
    num_intervals = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_purge_policy'


class MgmtIpReportDef(models.Model):
    report_guid = models.TextField(primary_key=True)  # This field type is a guess.
    schedule_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    schedule_enabled = models.NullBooleanField()
    store_enabled = models.NullBooleanField()
    purge_policy_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    title_nlsid = models.CharField(max_length=100)
    description_nlsid = models.CharField(max_length=500, blank=True, null=True)
    owner = models.CharField(max_length=256)
    category_nlsid = models.CharField(max_length=100)
    sub_category_nlsid = models.CharField(max_length=100)
    last_published_utc = models.DateField(blank=True, null=True)
    last_edit_time_utc = models.DateField(blank=True, null=True)
    last_edit_by = models.CharField(max_length=256, blank=True, null=True)
    is_jit_target = models.NullBooleanField()
    is_jit_multi_target = models.NullBooleanField()
    add_toc = models.NullBooleanField()
    publish_to_public = models.NullBooleanField()
    system_report = models.NullBooleanField()
    custom_report_bean_class = models.CharField(max_length=500, blank=True, null=True)
    internal_only = models.FloatField(blank=True, null=True)
    pack_name = models.CharField(max_length=64, blank=True, null=True)
    style = models.CharField(max_length=64, blank=True, null=True)
    show_navigation = models.NullBooleanField()
    product_name = models.CharField(max_length=100, blank=True, null=True)
    component_name = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    generate_context = models.NullBooleanField()
    help_topic_id = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_report_def'
        unique_together = (('title_nlsid', 'owner', 'system_report'),)


class MgmtIpReportDefElements(models.Model):
    report_guid = models.TextField(primary_key=True)  # This field type is a guess.
    element_guid = models.TextField()  # This field type is a guess.
    image_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    element_name_nlsid = models.CharField(max_length=256, blank=True, null=True)
    element_type_nlsid = models.CharField(max_length=100, blank=True, null=True)
    header_nlsid = models.CharField(max_length=200, blank=True, null=True)
    element_order = models.FloatField(blank=True, null=True)
    element_row = models.FloatField(blank=True, null=True)
    suppress_render = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_report_def_elements'
        unique_together = (('report_guid', 'element_guid'),)


class MgmtIpReportDefJitTypes(models.Model):
    report_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_report_def_jit_types'


class MgmtIpReportElemDef(models.Model):
    element_name_nlsid = models.CharField(primary_key=True, max_length=256)
    element_type_nlsid = models.CharField(max_length=100)
    description_nlsid = models.CharField(max_length=256, blank=True, null=True)
    element_class = models.CharField(max_length=1000, blank=True, null=True)
    internal_only = models.FloatField(blank=True, null=True)
    pack_name = models.CharField(max_length=64, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    component_name = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_report_elem_def'
        unique_together = (('element_name_nlsid', 'element_type_nlsid'),)


class MgmtIpReportElemImage(models.Model):
    report_guid = models.TextField(primary_key=True)  # This field type is a guess.
    element_guid = models.TextField()  # This field type is a guess.
    image_guid = models.TextField()  # This field type is a guess.
    image_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_report_elem_image'
        unique_together = (('report_guid', 'element_guid', 'image_guid'),)


class MgmtIpReportElemParams(models.Model):
    report_guid = models.TextField(primary_key=True)  # This field type is a guess.
    element_guid = models.TextField()  # This field type is a guess.
    param = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_report_elem_params'
        unique_together = (('report_guid', 'element_guid', 'param'),)


class MgmtIpReportElemTargets(models.Model):
    report_guid = models.TextField(primary_key=True)  # This field type is a guess.
    element_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    target_name = models.CharField(max_length=256)
    target_type = models.CharField(max_length=64)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_report_elem_targets'
        unique_together = (('report_guid', 'element_guid', 'target_guid'),)


class MgmtIpSqlStatements(models.Model):
    product_name = models.CharField(max_length=100, blank=True, null=True)
    component_name = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(primary_key=True, max_length=256)
    sql_statement = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_sql_statements'


class MgmtIpStoredReport(models.Model):
    report_guid = models.TextField(primary_key=True)  # This field type is a guess.
    element_guid = models.TextField()  # This field type is a guess.
    generated_date_utc = models.DateField()
    version_guid = models.TextField()  # This field type is a guess.
    status = models.CharField(max_length=4000, blank=True, null=True)
    element_object = models.BinaryField(blank=True, null=True)
    generated_oms_tz = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_ip_stored_report'
        unique_together = (('report_guid', 'element_guid', 'version_guid'),)


class MgmtJob(models.Model):
    job_id = models.TextField(primary_key=True)  # This field type is a guess.
    job_name = models.CharField(max_length=64)
    job_owner = models.CharField(max_length=256)
    job_description = models.CharField(max_length=4000, blank=True, null=True)
    job_type = models.CharField(max_length=32)
    job_type_major_version = models.FloatField(blank=True, null=True)
    nested = models.NullBooleanField()
    nested_job_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_library = models.NullBooleanField()
    parent_job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    schedule_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution_timeout = models.FloatField(blank=True, null=True)
    max_target_list_index = models.FloatField(blank=True, null=True)
    system_job = models.NullBooleanField()
    target_type = models.CharField(max_length=64, blank=True, null=True)
    job_status = models.IntegerField(blank=True, null=True)
    expired = models.NullBooleanField()
    is_corrective_action = models.NullBooleanField()
    restartable = models.NullBooleanField()
    broken = models.NullBooleanField()
    broken_reason = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job'


class MgmtJobAssocParams(models.Model):
    source = models.ForeignKey('MgmtJobParamSource', models.DO_NOTHING, primary_key=True)
    target_names_param = models.CharField(max_length=64)
    target_types_param = models.CharField(max_length=64)
    assoc_name = models.CharField(max_length=64)
    src_target_name = models.CharField(max_length=256)
    src_target_type = models.CharField(max_length=64)
    assoc_target_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_assoc_params'


class MgmtJobBlackoutAssoc(models.Model):
    execution = models.ForeignKey('MgmtJobExecSummary', models.DO_NOTHING, primary_key=True)
    blackout_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_blackout_assoc'
        unique_together = (('execution', 'blackout_guid'),)


class MgmtJobCallbacks(models.Model):
    job_type = models.ForeignKey('MgmtJobTypeInfo', models.DO_NOTHING, primary_key=True)
    callback_type = models.IntegerField()
    callback_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'mgmt_job_callbacks'
        unique_together = (('job_type', 'callback_type', 'callback_name'),)


class MgmtJobCommand(models.Model):
    command_name = models.CharField(primary_key=True, max_length=32)
    command_class = models.CharField(max_length=512, blank=True, null=True)
    command_type = models.NullBooleanField()
    is_trustable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_command'


class MgmtJobCommandBlockProcs(models.Model):
    proc_name = models.CharField(primary_key=True, max_length=256)
    param_types = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_command_block_procs'


class MgmtJobCredParams(models.Model):
    source = models.ForeignKey('MgmtJobParamSource', models.DO_NOTHING, primary_key=True)
    credential_set_name = models.CharField(max_length=256, blank=True, null=True)
    credential_set_target_type = models.CharField(max_length=256, blank=True, null=True)
    base_cred_type_name = models.CharField(max_length=256, blank=True, null=True)
    base_cred_type_target_type = models.CharField(max_length=256, blank=True, null=True)
    base_cred_type_columns = models.TextField(blank=True, null=True)  # This field type is a guess.
    credential_columns = models.TextField(blank=True, null=True)  # This field type is a guess.
    credential_columns_param = models.CharField(max_length=64, blank=True, null=True)
    target_names = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_types = models.TextField(blank=True, null=True)  # This field type is a guess.
    container_paths = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_names_param = models.CharField(max_length=64, blank=True, null=True)
    target_types_param = models.CharField(max_length=64, blank=True, null=True)
    container_paths_param = models.CharField(max_length=64, blank=True, null=True)
    set_override = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_cred_params'


class MgmtJobCredentials(models.Model):
    job_id = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    target_type = models.CharField(max_length=64)
    container_location = models.CharField(max_length=256)
    credential_set_name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=256)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_credentials'
        unique_together = (('job_id', 'target_guid', 'container_location', 'target_type', 'credential_set_name', 'user_name'),)


class MgmtJobDisplayErrorCodes(models.Model):
    job_type = models.ForeignKey('MgmtJobTypeInfo', models.DO_NOTHING, primary_key=True)
    id = models.CharField(max_length=64)
    nlsid = models.CharField(max_length=64, blank=True, null=True)
    default_value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_display_error_codes'
        unique_together = (('job_type', 'id'),)


class MgmtJobEmdStatusQueue(models.Model):
    emd_url = models.CharField(max_length=1024, blank=True, null=True)
    event_type = models.BigIntegerField(blank=True, null=True)
    occur_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_emd_status_queue'


class MgmtJobEvent(models.Model):
    event_name = models.CharField(primary_key=True, max_length=32)
    event_callback = models.CharField(max_length=96, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_event'


class MgmtJobExecCredInfo(models.Model):
    job_id = models.TextField(primary_key=True)  # This field type is a guess.
    execution_id = models.TextField()  # This field type is a guess.
    task_name = models.CharField(max_length=64)
    target_guid = models.TextField()  # This field type is a guess.
    container_location = models.CharField(max_length=256)
    credential_set_name = models.CharField(max_length=32)
    credentials_set = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_exec_cred_info'
        unique_together = (('job_id', 'execution_id', 'task_name', 'target_guid', 'container_location', 'credential_set_name'),)


class MgmtJobExecEventParams(models.Model):
    execution_id = models.TextField(primary_key=True)  # This field type is a guess.
    param_name = models.CharField(max_length=64)
    param_value = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mgmt_job_exec_event_params'
        unique_together = (('execution_id', 'param_name', 'param_value'),)


class MgmtJobExecLocks(models.Model):
    execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    lock_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    lock_mode = models.NullBooleanField()
    lock_status = models.NullBooleanField()
    lock_request_time = models.DateField(blank=True, null=True)
    lock_acquired_time = models.DateField(blank=True, null=True)
    lock_index = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_exec_locks'


class MgmtJobExecSummary(models.Model):
    job_id = models.TextField()  # This field type is a guess.
    job_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution_id = models.TextField(primary_key=True)  # This field type is a guess.
    source_execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_list_index = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    status_code = models.BigIntegerField(blank=True, null=True)
    status_code_category = models.NullBooleanField()
    status_bucket = models.BigIntegerField(blank=True, null=True)
    status_detail = models.BigIntegerField(blank=True, null=True)
    scheduled_time = models.DateField(blank=True, null=True)
    expected_start_time = models.DateField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    suspend_event = models.CharField(max_length=32, blank=True, null=True)
    suspend_time = models.DateField(blank=True, null=True)
    suspend_timeout = models.IntegerField(blank=True, null=True)
    queue_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    queue_index = models.FloatField(blank=True, null=True)
    triggering_severity = models.TextField(blank=True, null=True)  # This field type is a guess.
    deleted_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_exec_summary'


class MgmtJobExecplan(models.Model):
    job_type = models.ForeignKey('MgmtJobTypeInfo', models.DO_NOTHING, primary_key=True)
    step_name = models.CharField(max_length=64)
    step_type = models.IntegerField()
    nested_job_type = models.CharField(max_length=32, blank=True, null=True)
    nested_job_target_type = models.CharField(max_length=64, blank=True, null=True)
    incoming_edge_type = models.NullBooleanField()
    origin_step_name = models.CharField(max_length=64, blank=True, null=True)
    origin_step_type = models.IntegerField(blank=True, null=True)
    switch_var_name = models.CharField(max_length=64, blank=True, null=True)
    switch_var_index = models.CharField(max_length=96, blank=True, null=True)
    switch_case_val = models.CharField(max_length=4000, blank=True, null=True)
    iterate_param = models.CharField(max_length=64, blank=True, null=True)
    iterate_param_filter = models.CharField(max_length=4000, blank=True, null=True)
    num_children = models.BigIntegerField(blank=True, null=True)
    stepset_name = models.CharField(max_length=64, blank=True, null=True)
    stepset_status = models.CharField(max_length=512, blank=True, null=True)
    command_name = models.CharField(max_length=32, blank=True, null=True)
    restart_mode = models.NullBooleanField()
    all_params = models.NullBooleanField()
    all_targets = models.NullBooleanField()
    halt_on_failure = models.NullBooleanField()
    step_nlsid = models.CharField(max_length=64, blank=True, null=True)
    step_default = models.CharField(max_length=256, blank=True, null=True)
    flattened_targets = models.NullBooleanField()
    trusted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_execplan'
        unique_together = (('job_type', 'step_name', 'step_type'),)


class MgmtJobExecution(models.Model):
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    step_id = models.BigIntegerField(primary_key=True)
    source_step_id = models.BigIntegerField(blank=True, null=True)
    original_step_id = models.BigIntegerField(blank=True, null=True)
    restart_mode = models.BigIntegerField(blank=True, null=True)
    step_name = models.CharField(max_length=64, blank=True, null=True)
    step_type = models.IntegerField(blank=True, null=True)
    command_type = models.NullBooleanField()
    iterate_param = models.CharField(max_length=64, blank=True, null=True)
    iterate_param_index = models.IntegerField(blank=True, null=True)
    parent_step_id = models.BigIntegerField(blank=True, null=True)
    step_status = models.IntegerField(blank=True, null=True)
    step_status_code = models.IntegerField(blank=True, null=True)
    step_status_code_category = models.NullBooleanField()
    num_children = models.BigIntegerField(blank=True, null=True)
    num_children_completed = models.BigIntegerField(blank=True, null=True)
    output_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    error_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    dispatcher_id = models.BigIntegerField(blank=True, null=True)
    emd_url = models.CharField(max_length=1024, blank=True, null=True)
    oms_name = models.CharField(max_length=256, blank=True, null=True)
    async_error_received = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_execution'


class MgmtJobExtTargets(models.Model):
    job_id = models.TextField(primary_key=True)  # This field type is a guess.
    execution_id = models.TextField()  # This field type is a guess.
    target_list_index = models.BigIntegerField()
    target_guid = models.TextField()  # This field type is a guess.
    reference_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_ext_targets'
        unique_together = (('job_id', 'execution_id', 'target_list_index', 'target_guid'),)


class MgmtJobFlatTargets(models.Model):
    job = models.ForeignKey(MgmtJob, models.DO_NOTHING, primary_key=True)
    target_guid = models.TextField()  # This field type is a guess.
    target_list_index = models.IntegerField(blank=True, null=True)
    active = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_flat_targets'
        unique_together = (('job', 'target_guid'),)


class MgmtJobHistory(models.Model):
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    step_id = models.BigIntegerField(primary_key=True)
    source_step_id = models.BigIntegerField(blank=True, null=True)
    original_step_id = models.BigIntegerField(blank=True, null=True)
    restart_mode = models.BigIntegerField(blank=True, null=True)
    step_name = models.CharField(max_length=64, blank=True, null=True)
    step_type = models.IntegerField(blank=True, null=True)
    command_type = models.NullBooleanField()
    iterate_param = models.CharField(max_length=64, blank=True, null=True)
    iterate_param_index = models.IntegerField(blank=True, null=True)
    parent_step_id = models.BigIntegerField(blank=True, null=True)
    step_status = models.IntegerField(blank=True, null=True)
    step_status_code = models.IntegerField(blank=True, null=True)
    step_status_code_category = models.NullBooleanField()
    num_children = models.BigIntegerField(blank=True, null=True)
    num_children_completed = models.BigIntegerField(blank=True, null=True)
    output_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    error_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    dispatcher_id = models.BigIntegerField(blank=True, null=True)
    oms_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_history'


class MgmtJobLargeParams(models.Model):
    param_id = models.TextField(primary_key=True)  # This field type is a guess.
    reference_count = models.BigIntegerField(blank=True, null=True)
    param_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_large_params'


class MgmtJobLockInfo(models.Model):
    lock_guid = models.TextField(primary_key=True)  # This field type is a guess.
    job_type = models.ForeignKey('MgmtJobTypeInfo', models.DO_NOTHING)
    lock_index = models.IntegerField(blank=True, null=True)
    lock_name = models.CharField(max_length=32, blank=True, null=True)
    lock_type = models.IntegerField(blank=True, null=True)
    lock_mode = models.NullBooleanField()
    target_names_param = models.CharField(max_length=64, blank=True, null=True)
    target_types_param = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_lock_info'
        unique_together = (('lock_guid', 'job_type'),)


class MgmtJobLockTargets(models.Model):
    lock_guid = models.ForeignKey(MgmtJobLockInfo, models.DO_NOTHING, db_column='lock_guid', blank=True, null=True)
    job_type = models.ForeignKey(MgmtJobLockInfo, models.DO_NOTHING, blank=True, null=True)
    target_name = models.CharField(max_length=256, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)
    target_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_lock_targets'


class MgmtJobNotifyStates(models.Model):
    job = models.ForeignKey(MgmtJob, models.DO_NOTHING, primary_key=True)
    notify_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_notify_states'
        unique_together = (('job', 'notify_state'),)


class MgmtJobOutput(models.Model):
    output_id = models.TextField(primary_key=True)  # This field type is a guess.
    reference_count = models.BigIntegerField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_output'


class MgmtJobParamSource(models.Model):
    source_id = models.TextField(primary_key=True)  # This field type is a guess.
    job_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    apply_at_submission = models.NullBooleanField()
    apply_on_retry = models.NullBooleanField()
    step_name = models.CharField(max_length=64, blank=True, null=True)
    step_type = models.IntegerField(blank=True, null=True)
    source_type = models.CharField(max_length=32, blank=True, null=True)
    source_index = models.IntegerField(blank=True, null=True)
    source_data = models.CharField(max_length=4000, blank=True, null=True)
    override_user = models.NullBooleanField()
    required = models.NullBooleanField()
    encrypted = models.NullBooleanField()
    parameter_names = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_param_source'


class MgmtJobParameter(models.Model):
    job_id = models.TextField(primary_key=True)  # This field type is a guess.
    execution_id = models.TextField()  # This field type is a guess.
    parameter_name = models.CharField(max_length=64)
    parameter_type = models.NullBooleanField()
    encrypted = models.NullBooleanField()
    scalar_value = models.CharField(max_length=4000, blank=True, null=True)
    vector_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    large_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at_submit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_parameter'
        unique_together = (('job_id', 'execution_id', 'parameter_name'),)


class MgmtJobPropParams(models.Model):
    source = models.ForeignKey(MgmtJobParamSource, models.DO_NOTHING, primary_key=True)
    property_names = models.TextField(blank=True, null=True)  # This field type is a guess.
    property_names_param = models.CharField(max_length=64, blank=True, null=True)
    target_names = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_types = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_names_param = models.CharField(max_length=64, blank=True, null=True)
    target_types_param = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_prop_params'


class MgmtJobPurgeCriteria(models.Model):
    policy_name = models.ForeignKey('MgmtJobPurgePolicies', models.DO_NOTHING, db_column='policy_name', blank=True, null=True)
    criterion_index = models.IntegerField(blank=True, null=True)
    criterion_type = models.NullBooleanField()
    negated = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_purge_criteria'


class MgmtJobPurgePolicies(models.Model):
    policy_name = models.CharField(primary_key=True, max_length=32)
    time_frame = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_purge_policies'


class MgmtJobPurgeTargets(models.Model):
    policy_name = models.ForeignKey(MgmtJobPurgePolicies, models.DO_NOTHING, db_column='policy_name', blank=True, null=True)
    criterion_index = models.IntegerField(blank=True, null=True)
    purge_tguid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_purge_targets'


class MgmtJobPurgeValues(models.Model):
    policy_name = models.ForeignKey(MgmtJobPurgePolicies, models.DO_NOTHING, db_column='policy_name', blank=True, null=True)
    criterion_index = models.IntegerField(blank=True, null=True)
    purge_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_purge_values'


class MgmtJobQueues(models.Model):
    queue_name = models.CharField(max_length=128, blank=True, null=True)
    queue_id = models.TextField(primary_key=True)  # This field type is a guess.
    schedule_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    schedule_duration = models.IntegerField(blank=True, null=True)
    enabled = models.NullBooleanField()
    active = models.NullBooleanField()
    max_queue_index = models.FloatField(blank=True, null=True)
    concurrency_factor = models.IntegerField(blank=True, null=True)
    num_scheduled_executions = models.IntegerField(blank=True, null=True)
    num_executions = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_queues'


class MgmtJobSchedule(models.Model):
    schedule_id = models.TextField(primary_key=True)  # This field type is a guess.
    frequency_code = models.IntegerField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    start_grace_period = models.FloatField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    execution_hours = models.IntegerField(blank=True, null=True)
    execution_minutes = models.IntegerField(blank=True, null=True)
    interval = models.FloatField(blank=True, null=True)
    months = models.TextField(blank=True, null=True)  # This field type is a guess.
    days = models.TextField(blank=True, null=True)  # This field type is a guess.
    timezone_info = models.NullBooleanField()
    timezone_target_index = models.FloatField(blank=True, null=True)
    timezone_offset = models.FloatField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_schedule'


class MgmtJobSecInfo(models.Model):
    job_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    apply_at_submission = models.NullBooleanField()
    privilege_name = models.CharField(max_length=32, blank=True, null=True)
    privilege_type = models.NullBooleanField()
    target_names = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_types = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_names_param = models.CharField(max_length=64, blank=True, null=True)
    target_types_param = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_sec_info'


class MgmtJobSingleTargetTypes(models.Model):
    job_type = models.ForeignKey('MgmtJobTypeInfo', models.DO_NOTHING, primary_key=True)
    single_target_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_job_single_target_types'
        unique_together = (('job_type', 'single_target_type'),)


class MgmtJobSqlParams(models.Model):
    source = models.ForeignKey(MgmtJobParamSource, models.DO_NOTHING, primary_key=True)
    vector_params = models.TextField(blank=True, null=True)  # This field type is a guess.
    out_proc = models.NullBooleanField()
    out_param_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_sql_params'


class MgmtJobStateChanges(models.Model):
    state_change_guid = models.TextField(primary_key=True)  # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution = models.ForeignKey(MgmtJobExecSummary, models.DO_NOTHING, blank=True, null=True)
    step_id = models.BigIntegerField(blank=True, null=True)
    logged = models.DateTimeField(blank=True, null=True)
    occurred = models.DateField(blank=True, null=True)
    newstate = models.IntegerField(blank=True, null=True)
    status_bucket = models.IntegerField(blank=True, null=True)
    type = models.FloatField(blank=True, null=True)
    violation_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_state_changes'


class MgmtJobStepCommandLog(models.Model):
    step_id = models.FloatField(blank=True, null=True)
    command_block_id = models.FloatField(primary_key=True)
    command_block_text_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    command_block_status = models.IntegerField(blank=True, null=True)
    command_block_error = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_step_command_log'


class MgmtJobStepParams(models.Model):
    job_type_id = models.TextField(primary_key=True)  # This field type is a guess.
    step_name = models.CharField(max_length=64)
    param_name = models.CharField(max_length=64)
    parameter_type = models.NullBooleanField()
    encrypted = models.NullBooleanField()
    scalar_value = models.CharField(max_length=4000, blank=True, null=True)
    vector_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    large_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    value_of = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_step_params'
        unique_together = (('job_type_id', 'step_name', 'param_name'),)


class MgmtJobStepTargets(models.Model):
    step = models.ForeignKey(MgmtJobHistory, models.DO_NOTHING, blank=True, null=True)
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_step_targets'


class MgmtJobSubstParams(models.Model):
    source = models.ForeignKey(MgmtJobParamSource, models.DO_NOTHING, primary_key=True)
    source_params = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_subst_params'


class MgmtJobTarget(models.Model):
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_list_index = models.BigIntegerField(blank=True, null=True)
    target_guid = models.TextField()  # This field type is a guess.
    target_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_target'


class MgmtJobTypeDisplayInfo(models.Model):
    job_type = models.ForeignKey('MgmtJobTypeInfo', models.DO_NOTHING, blank=True, null=True)
    show_param = models.NullBooleanField()
    nls_bundle = models.CharField(max_length=4000, blank=True, null=True)
    use_default_create_ui = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_display_info'


class MgmtJobTypeDisplayParam(models.Model):
    job_type = models.ForeignKey('MgmtJobTypeInfo', models.DO_NOTHING, blank=True, null=True)
    param_order = models.IntegerField(blank=True, null=True)
    param_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_display_param'


class MgmtJobTypeInfo(models.Model):
    job_type_id = models.TextField(primary_key=True)  # This field type is a guess.
    job_type = models.CharField(max_length=32, blank=True, null=True)
    job_type_description = models.CharField(max_length=256, blank=True, null=True)
    job_type_owner = models.CharField(max_length=256, blank=True, null=True)
    job_type_category = models.NullBooleanField()
    last_modified_by = models.CharField(max_length=256, blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    all_target_types = models.NullBooleanField()
    version = models.CharField(max_length=20, blank=True, null=True)
    major_version = models.FloatField(blank=True, null=True)
    minor_version1 = models.FloatField(blank=True, null=True)
    minor_version2 = models.FloatField(blank=True, null=True)
    agent_bound = models.NullBooleanField()
    lock_action = models.NullBooleanField()
    single_target = models.NullBooleanField()
    default_target_type = models.CharField(max_length=64, blank=True, null=True)
    suspendable = models.NullBooleanField()
    editable = models.NullBooleanField()
    suspend_on_nocreds = models.NullBooleanField()
    restartable = models.NullBooleanField()
    job_type_nlsid = models.CharField(max_length=64, blank=True, null=True)
    job_type_default = models.CharField(max_length=256, blank=True, null=True)
    create_text_nlsid = models.CharField(max_length=64, blank=True, null=True)
    create_text_default = models.CharField(max_length=256, blank=True, null=True)
    delete_text_nlsid = models.CharField(max_length=64, blank=True, null=True)
    delete_text_default = models.CharField(max_length=256, blank=True, null=True)
    trusted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_info'


class MgmtJobTypeMaxVersions(models.Model):
    job_type = models.CharField(primary_key=True, max_length=32)
    job_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    major_version = models.FloatField()
    minor_version1 = models.FloatField(blank=True, null=True)
    minor_version2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_max_versions'
        unique_together = (('job_type', 'major_version'),)


class MgmtJobTypeParamDropdowns(models.Model):
    job_type = models.ForeignKey(MgmtJobTypeInfo, models.DO_NOTHING, blank=True, null=True)
    parameter_name = models.CharField(max_length=64, blank=True, null=True)
    is_default = models.NullBooleanField()
    option_value = models.CharField(max_length=32, blank=True, null=True)
    option_text_nlsid = models.CharField(max_length=64, blank=True, null=True)
    option_text_default = models.CharField(max_length=256, blank=True, null=True)
    param_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_param_dropdowns'


class MgmtJobTypeParamDsplyInfo(models.Model):
    job_type = models.ForeignKey(MgmtJobTypeInfo, models.DO_NOTHING, primary_key=True)
    parameter_name = models.CharField(max_length=64)
    show_in_create = models.NullBooleanField()
    show_in_results = models.NullBooleanField()
    label_nlsid = models.CharField(max_length=64, blank=True, null=True)
    label_default = models.CharField(max_length=256, blank=True, null=True)
    hint_nlsid = models.CharField(max_length=64, blank=True, null=True)
    hint_default = models.CharField(max_length=256, blank=True, null=True)
    display_mode = models.IntegerField(blank=True, null=True)
    num_lines = models.IntegerField(blank=True, null=True)
    default_text = models.CharField(max_length=4000, blank=True, null=True)
    default_nlsid = models.CharField(max_length=64, blank=True, null=True)
    param_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_param_dsply_info'
        unique_together = (('job_type', 'parameter_name'),)


class MgmtJobTypeParamUriInfo(models.Model):
    job_type = models.ForeignKey(MgmtJobTypeInfo, models.DO_NOTHING, primary_key=True)
    uri = models.CharField(max_length=2000, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=2000, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    help_topic = models.CharField(max_length=2000, blank=True, null=True)
    task_help_topic = models.CharField(max_length=2000, blank=True, null=True)
    show_target_properties = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_param_uri_info'


class MgmtJobTypeUriInfo(models.Model):
    job_type = models.ForeignKey(MgmtJobTypeInfo, models.DO_NOTHING, blank=True, null=True)
    uri_use = models.IntegerField(blank=True, null=True)
    uri = models.CharField(max_length=4000, blank=True, null=True)
    is_jsp = models.NullBooleanField()
    class_field = models.CharField(db_column='class', max_length=4000, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'mgmt_job_type_uri_info'


class MgmtJobUserParams(models.Model):
    source = models.ForeignKey(MgmtJobParamSource, models.DO_NOTHING, primary_key=True)
    target_name_params = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_type_params = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_job_user_params'


class MgmtJobValueParams(models.Model):
    source = models.ForeignKey(MgmtJobParamSource, models.DO_NOTHING, primary_key=True)
    param_values = models.TextField(blank=True, null=True)  # This field type is a guess.
    action = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_job_value_params'


class MgmtLastSyncLoadDetails(models.Model):
    emd_url = models.CharField(primary_key=True, max_length=1024)
    load_type = models.CharField(max_length=32, blank=True, null=True)
    load_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_last_sync_load_details'


class MgmtLastViolation(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    policy_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    collection_timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_last_violation'
        unique_together = (('target_guid', 'policy_guid', 'key_value'),)


class MgmtLicensableTargetTypes(models.Model):
    pack_target_type = models.CharField(primary_key=True, max_length=64)
    target_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_licensable_target_types'
        unique_together = (('pack_target_type', 'target_type'),)


class MgmtLicenseConfirmation(models.Model):
    target_guid = models.ForeignKey('MgmtTargets', models.DO_NOTHING, db_column='target_guid', primary_key=True)
    confirmation = models.CharField(max_length=1, blank=True, null=True)
    confirmed_by = models.CharField(max_length=256, blank=True, null=True)
    confirmed_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_license_confirmation'


class MgmtLicenseDefinitions(models.Model):
    pack_label = models.CharField(primary_key=True, max_length=64)
    target_type = models.CharField(max_length=64)
    pack_display_label = models.CharField(max_length=128, blank=True, null=True)
    pack_label_nlsid = models.CharField(max_length=64, blank=True, null=True)
    pack_description = models.CharField(max_length=4000, blank=True, null=True)
    pack_description_nlsid = models.CharField(max_length=64, blank=True, null=True)
    pack_abbr = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'mgmt_license_definitions'
        unique_together = (('pack_label', 'target_type'), ('pack_abbr', 'target_type'),)


class MgmtLicensedTargets(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    pack_name = models.CharField(max_length=64)
    from_target_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_licensed_targets'
        unique_together = (('target_guid', 'pack_name', 'from_target_guid'),)


class MgmtLicenses(models.Model):
    username = models.CharField(max_length=256)
    timestamp = models.DateField(blank=True, null=True)
    i_agree = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_licenses'


class MgmtLoaderDesignators(models.Model):
    designator = models.CharField(primary_key=True, max_length=2)
    oms_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_loader_designators'


class MgmtLoaderQtable(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.CharField(max_length=30, blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.CharField(max_length=30, blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.BinaryField(blank=True, null=True)
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_loader_qtable'


class MgmtLoginAssistants(models.Model):
    login_asst_name = models.CharField(primary_key=True, max_length=64)
    login_index = models.IntegerField(blank=True, null=True)
    login_asst_classname = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_login_assistants'


class MgmtLongText(models.Model):
    digest = models.TextField(primary_key=True)  # This field type is a guess.
    prefix = models.CharField(max_length=4000)
    entire = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_long_text'


class MgmtManagementPlugins(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    mp_version = models.CharField(max_length=64)
    mp_guid = models.TextField(unique=True)  # This field type is a guess.
    import_date = models.DateField(blank=True, null=True)
    hwm_status = models.BigIntegerField(blank=True, null=True)
    functional_description = models.CharField(max_length=4000, blank=True, null=True)
    requirements_description = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_management_plugins'
        unique_together = (('target_type', 'mp_version'),)


class MgmtMasterAgent(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    agent_guid = models.TextField()  # This field type is a guess.
    start_timestamp = models.DateField()
    end_timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_master_agent'
        unique_together = (('target_guid', 'agent_guid', 'start_timestamp'),)


class MgmtMasterChangedCallback(models.Model):
    target_name = models.CharField(primary_key=True, max_length=256)
    target_type = models.CharField(max_length=64)
    callback_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_master_changed_callback'
        unique_together = (('target_name', 'target_type', 'callback_name'),)


class MgmtMessages(models.Model):
    message_id = models.CharField(primary_key=True, max_length=256)
    subsystem = models.CharField(max_length=64)
    language_code = models.CharField(max_length=2)
    country_code = models.CharField(max_length=2)
    message = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_messages'
        unique_together = (('message_id', 'subsystem', 'language_code', 'country_code'),)


class MgmtMetadataSets(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=8)
    table_name = models.CharField(max_length=32)
    load_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metadata_sets'
        unique_together = (('target_type', 'type_meta_ver', 'table_name'),)


class MgmtMetricCollectionsRep(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_metric_collections_rep'
        unique_together = (('target_guid', 'metric_guid', 'coll_name'),)


class MgmtMetricDependency(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    rs_metric = models.NullBooleanField()
    eval_order = models.IntegerField(blank=True, null=True)
    eval_func = models.CharField(max_length=256, blank=True, null=True)
    event_metric = models.FloatField(blank=True, null=True)
    disabled = models.FloatField(blank=True, null=True)
    members_ready = models.FloatField(blank=True, null=True)
    can_calculate = models.FloatField(blank=True, null=True)
    start_timestamp = models.DateField(blank=True, null=True)
    force_calculate = models.FloatField(blank=True, null=True)
    error_msg = models.CharField(max_length=4000, blank=True, null=True)
    min_dep_interval = models.FloatField(blank=True, null=True)
    opt_code = models.FloatField(blank=True, null=True)
    repo_metric_only = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_metric_dependency'
        unique_together = (('target_guid', 'metric_guid', 'key_value'),)


class MgmtMetricDependencyDef(models.Model):
    target_type = models.CharField(max_length=256)
    type_meta_ver = models.CharField(max_length=8)
    metric_guid = models.TextField(primary_key=True)  # This field type is a guess.
    dep_target_type = models.CharField(max_length=256)
    dep_metric_guid = models.TextField()  # This field type is a guess.
    opt_code = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metric_dependency_def'
        unique_together = (('metric_guid', 'type_meta_ver', 'dep_target_type', 'dep_metric_guid'),)


class MgmtMetricDependencyDetails(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    dep_target_guid = models.TextField()  # This field type is a guess.
    dep_metric_guid = models.TextField()  # This field type is a guess.
    edep_target_guid = models.TextField()  # This field type is a guess.
    edep_metric_guid = models.TextField()  # This field type is a guess.
    dep_key_value = models.CharField(max_length=256)
    start_timestamp = models.DateField(blank=True, null=True)
    dep_coll_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metric_dependency_details'
        unique_together = (('target_guid', 'metric_guid', 'key_value', 'dep_target_guid', 'dep_metric_guid', 'dep_key_value'),)


class MgmtMetricErrors(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    agent_guid = models.TextField()  # This field type is a guess.
    collection_timestamp = models.DateField()
    metric_error_message = models.CharField(max_length=4000, blank=True, null=True)
    metric_error_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_metric_errors'
        unique_together = (('target_guid', 'metric_guid', 'coll_name', 'agent_guid', 'collection_timestamp'),)


class MgmtMetricVersions(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    metric_name = models.CharField(max_length=64)
    start_type_meta_ver = models.CharField(max_length=8, blank=True, null=True)
    end_type_meta_ver = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metric_versions'
        unique_together = (('target_type', 'metric_name'),)


class MgmtMetrics(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=8)
    category_prop_1 = models.CharField(max_length=64)
    category_prop_2 = models.CharField(max_length=64)
    category_prop_3 = models.CharField(max_length=64)
    category_prop_4 = models.CharField(max_length=64)
    category_prop_5 = models.CharField(max_length=64)
    metric_name = models.CharField(max_length=64)
    metric_type = models.FloatField(blank=True, null=True)
    usage_type = models.FloatField(blank=True, null=True)
    metric_guid = models.TextField()  # This field type is a guess.
    metric_column = models.CharField(max_length=64)
    column_label = models.CharField(max_length=64, blank=True, null=True)
    column_label_nlsid = models.CharField(max_length=64, blank=True, null=True)
    metric_label = models.CharField(max_length=64, blank=True, null=True)
    metric_label_nlsid = models.CharField(max_length=64, blank=True, null=True)
    key_column = models.CharField(max_length=512, blank=True, null=True)
    key_order = models.FloatField(blank=True, null=True)
    num_keys = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    description_nlsid = models.CharField(max_length=64, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)
    unit_nlsid = models.CharField(max_length=64, blank=True, null=True)
    short_name = models.CharField(max_length=40, blank=True, null=True)
    short_name_nlsid = models.CharField(max_length=64, blank=True, null=True)
    is_for_summary = models.FloatField(blank=True, null=True)
    keys_from_mult_colls = models.FloatField(blank=True, null=True)
    statefull = models.FloatField(blank=True, null=True)
    is_repository = models.NullBooleanField()
    author = models.CharField(max_length=256, blank=True, null=True)
    source_type = models.NullBooleanField()
    source = models.CharField(max_length=4000, blank=True, null=True)
    load_timestamp = models.DateField(blank=True, null=True)
    is_transposed = models.NullBooleanField()
    is_test_metric = models.NullBooleanField()
    has_push = models.NullBooleanField()
    has_pull = models.NullBooleanField()
    remote = models.NullBooleanField()
    repo_timing_enabled = models.NullBooleanField()
    non_thresholded_alerts = models.NullBooleanField()
    keyonly_thresholds = models.NullBooleanField()
    is_long_running = models.NullBooleanField()
    is_renderable = models.NullBooleanField()
    eval_func = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metrics'
        unique_together = (('target_type', 'metric_name', 'metric_column', 'type_meta_ver', 'category_prop_1', 'category_prop_2', 'category_prop_3', 'category_prop_4', 'category_prop_5'),)


class MgmtMetrics1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    rollup_timestamp = models.DateField()
    sample_count = models.FloatField(blank=True, null=True)
    value_average = models.FloatField(blank=True, null=True)
    value_minimum = models.FloatField(blank=True, null=True)
    value_maximum = models.FloatField(blank=True, null=True)
    value_sdev = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metrics_1day'
        unique_together = (('target_guid', 'metric_guid', 'key_value', 'rollup_timestamp'),)


class MgmtMetrics1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    rollup_timestamp = models.DateField()
    sample_count = models.FloatField(blank=True, null=True)
    value_average = models.FloatField(blank=True, null=True)
    value_minimum = models.FloatField(blank=True, null=True)
    value_maximum = models.FloatField(blank=True, null=True)
    value_sdev = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metrics_1hour'
        unique_together = (('target_guid', 'metric_guid', 'key_value', 'rollup_timestamp'),)


class MgmtMetricsCompositeKeys(models.Model):
    composite_key = models.TextField()  # This field type is a guess.
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    key_part1_value = models.CharField(max_length=256, blank=True, null=True)
    key_part2_value = models.CharField(max_length=256, blank=True, null=True)
    key_part3_value = models.CharField(max_length=256, blank=True, null=True)
    key_part4_value = models.CharField(max_length=256, blank=True, null=True)
    key_part5_value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metrics_composite_keys'
        unique_together = (('target_guid', 'composite_key'),)


class MgmtMetricsExt(models.Model):
    metric_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_type = models.CharField(max_length=64)
    meta_ver = models.CharField(max_length=8)
    category_prop_1 = models.CharField(max_length=64)
    category_prop_2 = models.CharField(max_length=64)
    category_prop_3 = models.CharField(max_length=64)
    category_prop_4 = models.CharField(max_length=64)
    category_prop_5 = models.CharField(max_length=64)
    alertable = models.CharField(max_length=1, blank=True, null=True)
    thresholdable = models.CharField(max_length=1, blank=True, null=True)
    keyonly_thresholds = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metrics_ext'
        unique_together = (('metric_guid', 'target_type', 'meta_ver', 'category_prop_1', 'category_prop_2', 'category_prop_3', 'category_prop_4', 'category_prop_5'),)


class MgmtMetricsRaw(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    collection_timestamp = models.DateField()
    value = models.FloatField(blank=True, null=True)
    string_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_metrics_raw'
        unique_together = (('target_guid', 'metric_guid', 'key_value', 'collection_timestamp'),)


class MgmtMntrSetCopies(models.Model):
    mntr_set_copy_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    copy_req_guid = models.TextField()  # This field type is a guess.
    created_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mntr_set_copies'


class MgmtMpContributorFile(models.Model):
    mp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    contributor_file_id = models.CharField(max_length=128)
    file_contents = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_contributor_file'
        unique_together = (('mp_guid', 'contributor_file_id'),)


class MgmtMpContributors(models.Model):
    mp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    contributor_file_id = models.CharField(max_length=128)
    contributor_name = models.CharField(max_length=128, blank=True, null=True)
    contributor_role = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_contributors'
        unique_together = (('mp_guid', 'contributor_file_id', 'contributor_role'),)


class MgmtMpDeploymentErrors(models.Model):
    mp_guid = models.TextField()  # This field type is a guess.
    agent = models.CharField(max_length=128)
    severity = models.BigIntegerField(blank=True, null=True)
    msg_bundle = models.CharField(max_length=128)
    msg_id = models.CharField(max_length=128)
    msg_guid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_deployment_errors'


class MgmtMpDeployments(models.Model):
    mp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    agent = models.CharField(max_length=128)
    deploy_date = models.DateField()
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_deployments'
        unique_together = (('mp_guid', 'agent'),)


class MgmtMpFileProps(models.Model):
    mp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    file_id = models.FloatField()
    prop_name = models.CharField(max_length=128)
    prop_value = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_file_props'
        unique_together = (('mp_guid', 'file_id', 'prop_name'),)


class MgmtMpFiles(models.Model):
    mp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    file_id = models.FloatField()
    file_name = models.CharField(max_length=256, blank=True, null=True)
    file_type = models.CharField(max_length=64, blank=True, null=True)
    file_contents = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_files'
        unique_together = (('mp_guid', 'file_id'),)


class MgmtMpGroupMembers(models.Model):
    group_name = models.CharField(primary_key=True, max_length=64)
    target_type = models.CharField(max_length=64)
    mp_version = models.CharField(max_length=64, blank=True, null=True)
    deployment_order = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_mp_group_members'
        unique_together = (('group_name', 'target_type', 'deployment_order'),)


class MgmtMpGroups(models.Model):
    group_name = models.CharField(primary_key=True, max_length=64)
    description = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_groups'


class MgmtMpHomepageReports(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    report_title = models.CharField(max_length=100)
    report_owner = models.CharField(max_length=256)
    report_order = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_homepage_reports'
        unique_together = (('target_type', 'report_title', 'report_owner'),)


class MgmtMpMechanisms(models.Model):
    mp_guid = models.TextField()  # This field type is a guess.
    mechanism_id = models.FloatField()
    mechanism_type = models.CharField(max_length=128)
    prop_name = models.CharField(max_length=128)
    prop_value = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_mechanisms'


class MgmtMpNlsSubstitutions(models.Model):
    msg_guid = models.BigIntegerField(primary_key=True)
    sub_index = models.BigIntegerField()
    substitution = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_nls_substitutions'
        unique_together = (('msg_guid', 'sub_index'),)


class MgmtMpProps(models.Model):
    mp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    prop_name = models.CharField(max_length=128)
    prop_value = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_mp_props'
        unique_together = (('mp_guid', 'prop_name'),)


class MgmtNestedJobCredInfo(models.Model):
    job_type = models.ForeignKey(MgmtJobTypeInfo, models.DO_NOTHING, primary_key=True)
    nested_job_name = models.CharField(max_length=64)
    target_name = models.CharField(max_length=256)
    target_type = models.CharField(max_length=64)
    container_location = models.CharField(max_length=256)
    credential_set_name = models.CharField(max_length=32)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_nested_job_cred_info'
        unique_together = (('job_type', 'nested_job_name', 'target_name', 'target_type', 'container_location', 'credential_set_name'),)


class MgmtNestedJobTargets(models.Model):
    job_type_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    step_name = models.CharField(max_length=64, blank=True, null=True)
    step_type = models.IntegerField(blank=True, null=True)
    target_name = models.CharField(max_length=256, blank=True, null=True)
    target_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_nested_job_targets'


class MgmtNetEvents(models.Model):
    net_event_guid = models.TextField(primary_key=True)  # This field type is a guess.
    ip_address = models.CharField(max_length=64)
    collection_time = models.DateField()
    message = models.CharField(max_length=4000, blank=True, null=True)
    message_nlsid = models.CharField(max_length=64, blank=True, null=True)
    message_params = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_net_events'


class MgmtNotificationLog(models.Model):
    source_obj_type = models.IntegerField()
    source_obj_guid = models.TextField()  # This field type is a guess.
    timestamp = models.DateField(blank=True, null=True)
    delivered = models.CharField(max_length=1, blank=True, null=True)
    message = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_notification_log'


class MgmtNotifyDevSchedules(models.Model):
    schedule_owner = models.ForeignKey('MgmtNotifyProfiles', models.DO_NOTHING, db_column='schedule_owner', primary_key=True)
    schedule_name = models.CharField(max_length=64)
    device_name = models.ForeignKey('MgmtNotifyDevices', models.DO_NOTHING, db_column='device_name')
    device_owner = models.ForeignKey('MgmtNotifyDevices', models.DO_NOTHING, db_column='device_owner')
    schedule = models.CharField(max_length=1344)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_dev_schedules'
        unique_together = (('schedule_owner', 'schedule_name', 'device_name', 'device_owner'),)


class MgmtNotifyDeviceParams(models.Model):
    device_name = models.ForeignKey('MgmtNotifyDevices', models.DO_NOTHING, db_column='device_name')
    profile_name = models.ForeignKey('MgmtNotifyDevices', models.DO_NOTHING, db_column='profile_name')
    parameter = models.CharField(max_length=256)
    position = models.FloatField()
    abbreviated = models.FloatField()
    timestamp_format = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_device_params'


class MgmtNotifyDevices(models.Model):
    device_name = models.CharField(primary_key=True, max_length=132)
    device_description = models.CharField(max_length=256, blank=True, null=True)
    profile_name = models.ForeignKey('MgmtNotifyProfiles', models.DO_NOTHING, db_column='profile_name')
    type = models.IntegerField()
    email_address = models.CharField(max_length=128, blank=True, null=True)
    subject_prefix = models.CharField(max_length=32, blank=True, null=True)
    program = models.CharField(max_length=512, blank=True, null=True)
    snmp_host = models.CharField(max_length=128, blank=True, null=True)
    snmp_port = models.FloatField(blank=True, null=True)
    snmp_community = models.CharField(max_length=128, blank=True, null=True)
    status = models.BooleanField()
    contact_timestamp = models.DateField()
    status_message = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_devices'
        unique_together = (('device_name', 'profile_name'),)


class MgmtNotifyEmailGateway(models.Model):
    mail_host = models.CharField(primary_key=True, max_length=128)
    email_address = models.CharField(max_length=256)
    email_name = models.CharField(max_length=64)
    smtp_user = models.CharField(max_length=256, blank=True, null=True)
    smtp_pwd = models.CharField(max_length=256, blank=True, null=True)
    smtp_port = models.FloatField(blank=True, null=True)
    precedence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_email_gateway'


class MgmtNotifyFormatHandlers(models.Model):
    source_obj_type = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_format_handlers'


class MgmtNotifyInputQtable(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.CharField(max_length=30, blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.CharField(max_length=30, blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.BinaryField(blank=True, null=True)
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_notify_input_qtable'


class MgmtNotifyJobRuleConfigs(models.Model):
    rule_name = models.ForeignKey('MgmtNotifyRules', models.DO_NOTHING, db_column='rule_name')
    owner = models.ForeignKey('MgmtNotifyRules', models.DO_NOTHING, db_column='owner')
    target_type = models.CharField(max_length=64)
    target_name = models.CharField(max_length=256)
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_name = models.CharField(max_length=64)
    job_owner = models.CharField(max_length=256)
    job_type = models.CharField(max_length=32)
    want_job_scheduled = models.NullBooleanField()
    want_job_running = models.NullBooleanField()
    want_job_succeeded = models.NullBooleanField()
    want_job_suspended = models.NullBooleanField()
    want_job_problems = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_notify_job_rule_configs'


class MgmtNotifyNotifyees(models.Model):
    rule_name = models.ForeignKey('MgmtNotifyRules', models.DO_NOTHING, db_column='rule_name', primary_key=True)
    owner = models.ForeignKey('MgmtNotifyRules', models.DO_NOTHING, db_column='owner')
    device_name = models.CharField(max_length=132)
    profile_name = models.ForeignKey('MgmtNotifyProfiles', models.DO_NOTHING, db_column='profile_name')

    class Meta:
        managed = False
        db_table = 'mgmt_notify_notifyees'
        unique_together = (('rule_name', 'owner', 'device_name', 'profile_name'),)


class MgmtNotifyProfiles(models.Model):
    profile_name = models.CharField(primary_key=True, max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    escalation_profile_name = models.ForeignKey('self', models.DO_NOTHING, db_column='escalation_profile_name', blank=True, null=True)
    escalation_interval = models.FloatField(blank=True, null=True)
    notification_ttl = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_profiles'


class MgmtNotifyQtable(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.CharField(max_length=30, blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.CharField(max_length=30, blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_notify_qtable'


class MgmtNotifyQueues(models.Model):
    qname = models.CharField(primary_key=True, max_length=30)
    oms_id = models.FloatField(blank=True, null=True)
    windows = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_queues'


class MgmtNotifyRequeue(models.Model):
    source_guid = models.TextField()  # This field type is a guess.
    source_type = models.FloatField()
    notification_type = models.FloatField()
    device_name = models.ForeignKey(MgmtNotifyDevices, models.DO_NOTHING, db_column='device_name')
    device_owner = models.ForeignKey(MgmtNotifyDevices, models.DO_NOTHING, db_column='device_owner')
    device_type = models.FloatField()
    rule_name = models.CharField(max_length=64)
    rule_owner = models.CharField(max_length=256)
    num_requeues = models.FloatField()
    max_requeues = models.FloatField()
    insertion_timestamp = models.DateField()
    last_timestamp = models.DateField()
    next_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_notify_requeue'


class MgmtNotifyRuleConfigs(models.Model):
    rule_name = models.ForeignKey('MgmtNotifyRules', models.DO_NOTHING, db_column='rule_name')
    owner = models.ForeignKey('MgmtNotifyRules', models.DO_NOTHING, db_column='owner')
    target_type = models.CharField(max_length=64)
    target_name = models.CharField(max_length=256)
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    metric_column = models.CharField(max_length=64)
    key_value = models.CharField(max_length=256)
    key_part_1 = models.CharField(max_length=256)
    key_part_2 = models.CharField(max_length=256)
    key_part_3 = models.CharField(max_length=256)
    key_part_4 = models.CharField(max_length=256)
    key_part_5 = models.CharField(max_length=256)
    want_clears = models.NullBooleanField()
    want_warnings = models.NullBooleanField()
    want_critical_alerts = models.NullBooleanField()
    want_target_up = models.NullBooleanField()
    want_target_down = models.NullBooleanField()
    want_target_unreachable_start = models.NullBooleanField()
    want_target_unreachable_end = models.NullBooleanField()
    want_target_metric_err_start = models.NullBooleanField()
    want_target_metric_err_end = models.NullBooleanField()
    want_target_blackout_start = models.NullBooleanField()
    want_target_blackout_end = models.NullBooleanField()
    want_policy_clears = models.NullBooleanField()
    want_policy_violations = models.NullBooleanField()
    want_warning_job_succeeded = models.NullBooleanField()
    want_warning_job_problems = models.NullBooleanField()
    want_critical_job_succeeded = models.NullBooleanField()
    want_critical_job_problems = models.NullBooleanField()
    want_policy_job_succeeded = models.NullBooleanField()
    want_policy_job_problems = models.NullBooleanField()
    ignore_rca = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_notify_rule_configs'


class MgmtNotifyRules(models.Model):
    rule_name = models.CharField(primary_key=True, max_length=64)
    owner = models.ForeignKey(MgmtNotifyProfiles, models.DO_NOTHING, db_column='owner')
    description = models.CharField(max_length=256, blank=True, null=True)
    public_rule = models.NullBooleanField()
    repeat = models.FloatField(blank=True, null=True)
    rule_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_notify_rules'
        unique_together = (('rule_name', 'owner'),)


class MgmtNotifySchedules(models.Model):
    schedule_owner = models.ForeignKey(MgmtNotifyProfiles, models.DO_NOTHING, db_column='schedule_owner', primary_key=True)
    schedule_name = models.CharField(max_length=64)
    start_date = models.DateField()
    num_weeks = models.FloatField()
    updated_by = models.CharField(max_length=256)
    updated = models.DateField()
    disable_start = models.DateField(blank=True, null=True)
    disable_end = models.DateField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_notify_schedules'
        unique_together = (('schedule_owner', 'schedule_name'),)


class MgmtObAdminClientDb(models.Model):
    ob_target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    ob_client_host = models.CharField(max_length=128, blank=True, null=True)
    ob_admin_target_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_ob_admin_client_db'
        unique_together = (('ob_target_guid', 'ob_admin_target_guid'),)


class MgmtOmsParameters(models.Model):
    host_url = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    value = models.CharField(max_length=256, blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_oms_parameters'


class MgmtOperationsMaster(models.Model):
    op_code = models.IntegerField(primary_key=True)
    operation_description = models.CharField(max_length=4000, blank=True, null=True)
    operation_audit = models.NullBooleanField()
    audit_column_name1 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name2 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name3 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name4 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name5 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name6 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name7 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name8 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name9 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name10 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name11 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name12 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name13 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name14 = models.CharField(max_length=4000, blank=True, null=True)
    audit_column_name15 = models.CharField(max_length=4000, blank=True, null=True)
    audit_clob_name1 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_operations_master'


class MgmtOsmDiskGroupEcm(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    disk_group = models.CharField(max_length=30)
    problem_code = models.IntegerField()
    value1_n = models.IntegerField(blank=True, null=True)
    value2_n = models.IntegerField(blank=True, null=True)
    value3_s = models.CharField(max_length=100, blank=True, null=True)
    value4_s = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_osm_disk_group_ecm'
        unique_together = (('ecm_snapshot', 'disk_group', 'problem_code'),)


class MgmtOuiAruMap(models.Model):
    aru_id = models.IntegerField()
    oui_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_oui_aru_map'


class MgmtPafApplications(models.Model):
    application_guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(unique=True, max_length=128)
    description = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=512)
    resource_bundle = models.CharField(max_length=1000, blank=True, null=True)
    data_guid = models.CharField(max_length=32, blank=True, null=True)
    interviewable = models.CharField(max_length=1, blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_applications'


class MgmtPafCompJobtypeMappings(models.Model):
    mapping_guid = models.CharField(primary_key=True, max_length=32)
    component_subtype = models.CharField(max_length=256)
    jobtype_guid = models.ForeignKey('MgmtPafJobtypes', models.DO_NOTHING, db_column='jobtype_guid')
    last_updated = models.DateField()
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_comp_jobtype_mappings'
        unique_together = (('component_subtype', 'jobtype_guid'),)


class MgmtPafEncryptedStrings(models.Model):
    str_guid = models.CharField(primary_key=True, max_length=32)
    base_guid = models.CharField(max_length=32)
    encrypted = models.CharField(max_length=2000, blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_encrypted_strings'


class MgmtPafInstances(models.Model):
    instance_guid = models.CharField(primary_key=True, max_length=32)
    instance_name = models.CharField(max_length=256)
    procedure_guid = models.ForeignKey('MgmtPafProcedures', models.DO_NOTHING, db_column='procedure_guid')
    data_guid = models.CharField(max_length=32)
    created_by = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    started = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    deleted = models.CharField(max_length=1, blank=True, null=True)
    oms_guid = models.CharField(max_length=32, blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_instances'


class MgmtPafJobtypeParams(models.Model):
    jobtype_guid = models.ForeignKey('MgmtPafJobtypes', models.DO_NOTHING, db_column='jobtype_guid', primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    param_name = models.CharField(max_length=64)
    param_value = models.CharField(max_length=256, blank=True, null=True)
    implicit = models.CharField(max_length=1, blank=True, null=True)
    secret_status = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    param_order = models.BigIntegerField(blank=True, null=True)
    param_group = models.CharField(max_length=32, blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_jobtype_params'
        unique_together = (('jobtype_guid', 'param_name'),)


class MgmtPafJobtypes(models.Model):
    jobtype_guid = models.CharField(primary_key=True, max_length=32)
    jobtype = models.CharField(max_length=256)
    description = models.CharField(max_length=1000, blank=True, null=True)
    last_updated = models.DateField()
    target_list_dependent = models.CharField(max_length=1, blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_jobtypes'


class MgmtPafMsgQtable1(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.CharField(max_length=30, blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.CharField(max_length=30, blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_paf_msg_qtable_1'


class MgmtPafMsgQtable2(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.CharField(max_length=30, blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.CharField(max_length=30, blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_paf_msg_qtable_2'


class MgmtPafNotificationLog(models.Model):
    job_name = models.CharField(max_length=128, blank=True, null=True)
    instance_guid = models.CharField(max_length=32, blank=True, null=True)
    state_guid = models.CharField(max_length=32, blank=True, null=True)
    job_guid = models.CharField(max_length=32, blank=True, null=True)
    oms_guid = models.CharField(max_length=32, blank=True, null=True)
    job_status = models.IntegerField(blank=True, null=True)
    notif_update_time = models.DateField(blank=True, null=True)
    message = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_notification_log'


class MgmtPafOmsStatus(models.Model):
    oms_guid = models.CharField(primary_key=True, max_length=32)
    host_url = models.CharField(unique=True, max_length=256)
    status = models.CharField(max_length=1, blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_oms_status'


class MgmtPafParFiles(models.Model):
    par_guid = models.CharField(primary_key=True, max_length=32)
    filename = models.CharField(max_length=512, blank=True, null=True)
    application_guid = models.CharField(max_length=32, blank=True, null=True)
    file_path = models.CharField(max_length=2000, blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_par_files'


class MgmtPafParamGroups(models.Model):
    jobtype_guid = models.ForeignKey(MgmtPafJobtypes, models.DO_NOTHING, db_column='jobtype_guid')
    group_guid = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2000, blank=True, null=True)
    group_order = models.BigIntegerField(blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_param_groups'


class MgmtPafProcedures(models.Model):
    procedure_guid = models.CharField(primary_key=True, max_length=32)
    base_guid = models.CharField(max_length=32)
    source_guid = models.CharField(max_length=32, blank=True, null=True)
    version = models.CharField(max_length=32)
    application_name = models.CharField(max_length=128)
    name = models.CharField(max_length=4000)
    description = models.CharField(max_length=4000, blank=True, null=True)
    last_updated = models.DateField()
    created_by = models.CharField(max_length=64)
    data_guid = models.CharField(max_length=32)
    is_oracle = models.CharField(max_length=1, blank=True, null=True)
    deleted = models.CharField(max_length=1, blank=True, null=True)
    helpset = models.CharField(max_length=512, blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_procedures'
        unique_together = (('base_guid', 'version'),)


class MgmtPafStates(models.Model):
    state_guid = models.CharField(primary_key=True, max_length=32)
    instance_guid = models.ForeignKey(MgmtPafInstances, models.DO_NOTHING, db_column='instance_guid')
    step_guid = models.CharField(max_length=32)
    parent_state_guid = models.CharField(max_length=32, blank=True, null=True)
    state_type = models.BigIntegerField()
    status = models.BigIntegerField(blank=True, null=True)
    reason_code = models.BigIntegerField(blank=True, null=True)
    reason_rsc_id = models.CharField(max_length=64, blank=True, null=True)
    reason_rsc_args = models.CharField(max_length=1024, blank=True, null=True)
    reason_exception = models.CharField(max_length=1024, blank=True, null=True)
    state_index = models.BigIntegerField(blank=True, null=True)
    started = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    target_name = models.CharField(max_length=128, blank=True, null=True)
    target_type = models.CharField(max_length=128, blank=True, null=True)
    current_state_guid = models.CharField(max_length=32, blank=True, null=True)
    job_id = models.CharField(unique=True, max_length=32, blank=True, null=True)
    exec_id = models.CharField(max_length=32, blank=True, null=True)
    job_status = models.BigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=4000, blank=True, null=True)
    content0 = models.CharField(max_length=2000, blank=True, null=True)
    content1 = models.CharField(max_length=2000, blank=True, null=True)
    content2 = models.CharField(max_length=2000, blank=True, null=True)
    content3 = models.CharField(max_length=2000, blank=True, null=True)
    content4 = models.CharField(max_length=2000, blank=True, null=True)
    content5 = models.CharField(max_length=2000, blank=True, null=True)
    content6 = models.CharField(max_length=2000, blank=True, null=True)
    content7 = models.CharField(max_length=2000, blank=True, null=True)
    job_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_states'


class MgmtPafTextualData(models.Model):
    data_guid = models.CharField(primary_key=True, max_length=32)
    data_size = models.BigIntegerField()
    encoding = models.CharField(max_length=64, blank=True, null=True)
    data0 = models.CharField(max_length=4000, blank=True, null=True)
    data1 = models.CharField(max_length=4000, blank=True, null=True)
    data2 = models.CharField(max_length=4000, blank=True, null=True)
    data3 = models.CharField(max_length=4000, blank=True, null=True)
    data4 = models.CharField(max_length=4000, blank=True, null=True)
    data5 = models.CharField(max_length=4000, blank=True, null=True)
    data6 = models.CharField(max_length=4000, blank=True, null=True)
    data7 = models.CharField(max_length=4000, blank=True, null=True)
    data8 = models.CharField(max_length=4000, blank=True, null=True)
    data9 = models.CharField(max_length=4000, blank=True, null=True)
    data10 = models.CharField(max_length=4000, blank=True, null=True)
    data11 = models.CharField(max_length=4000, blank=True, null=True)
    data12 = models.CharField(max_length=4000, blank=True, null=True)
    data13 = models.CharField(max_length=4000, blank=True, null=True)
    data14 = models.CharField(max_length=4000, blank=True, null=True)
    data15 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_paf_textual_data'


class MgmtParameters(models.Model):
    parameter_name = models.CharField(primary_key=True, max_length=32)
    parameter_value = models.CharField(max_length=256)
    parameter_comment = models.CharField(max_length=256, blank=True, null=True)
    internal_flag = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_parameters'


class MgmtPdpColumnMetadata(models.Model):
    pdp_guid = models.ForeignKey('MgmtPdpMetadata', models.DO_NOTHING, db_column='pdp_guid', primary_key=True)
    pdp_column_name = models.CharField(max_length=64)
    is_required = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_pdp_column_metadata'
        unique_together = (('pdp_guid', 'pdp_column_name'),)


class MgmtPdpHostSetting(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    pdp_type = models.CharField(max_length=256)
    pdp_setting_name = models.CharField(max_length=256)
    pdp_setting_value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_pdp_host_setting'
        unique_together = (('target_guid', 'pdp_type', 'pdp_setting_name'),)


class MgmtPdpMetadata(models.Model):
    pdp_guid = models.TextField(primary_key=True)  # This field type is a guess.
    pdp_name = models.CharField(max_length=64)
    credential_type_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_pdp_metadata'


class MgmtPdpParamMetadata(models.Model):
    pdp_guid = models.ForeignKey(MgmtPdpMetadata, models.DO_NOTHING, db_column='pdp_guid', primary_key=True)
    pdp_param_name = models.CharField(max_length=64)
    description_nlsid = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_pdp_param_metadata'
        unique_together = (('pdp_guid', 'pdp_param_name'),)


class MgmtPdpSettingMetadata(models.Model):
    pdp_guid = models.ForeignKey(MgmtPdpMetadata, models.DO_NOTHING, db_column='pdp_guid', primary_key=True)
    pdp_setting_name = models.CharField(max_length=64)
    is_required = models.NullBooleanField()
    display_name_nlsid = models.CharField(max_length=64, blank=True, null=True)
    display_name = models.CharField(max_length=64, blank=True, null=True)
    hint_nlsid = models.CharField(max_length=64, blank=True, null=True)
    hint = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_pdp_setting_metadata'
        unique_together = (('pdp_guid', 'pdp_setting_name'),)


class MgmtPdpSettingValues(models.Model):
    setting_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    value_name = models.CharField(max_length=64, blank=True, null=True)
    value = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_pdp_setting_values'


class MgmtPdpSettings(models.Model):
    setting_guid = models.TextField()  # This field type is a guess.
    setting_name = models.CharField(primary_key=True, max_length=64)
    pdp_type = models.CharField(max_length=64)
    created_by = models.CharField(max_length=256, blank=True, null=True)
    last_modified = models.DateField(blank=True, null=True)
    is_enabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_pdp_settings'
        unique_together = (('setting_name', 'pdp_type'),)


class MgmtPerformanceNames(models.Model):
    job_name = models.CharField(primary_key=True, max_length=512)
    display_name = models.CharField(max_length=128, blank=True, null=True)
    dbms_jobname = models.CharField(max_length=128, blank=True, null=True)
    is_dbmsjob = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_performance_names'


class MgmtPlanproblemFactors(models.Model):
    target_guid = models.ForeignKey('MgmtSqlEvaluation', models.DO_NOTHING, db_column='target_guid', primary_key=True)
    eval_timestamp = models.ForeignKey('MgmtSqlEvaluation', models.DO_NOTHING, db_column='eval_timestamp')
    address = models.ForeignKey('MgmtSqlEvaluation', models.DO_NOTHING, db_column='address')
    hash_value = models.ForeignKey('MgmtSqlEvaluation', models.DO_NOTHING, db_column='hash_value')
    plan_hash_value = models.ForeignKey('MgmtSqlEvaluation', models.DO_NOTHING, db_column='plan_hash_value')
    id = models.FloatField()
    reason_code = models.ForeignKey('MgmtSqlEvaluation', models.DO_NOTHING, db_column='reason_code')
    attribute = models.CharField(max_length=64)
    importance = models.CharField(max_length=64, blank=True, null=True)
    confidence = models.CharField(max_length=64, blank=True, null=True)
    sql_text = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_planproblem_factors'
        unique_together = (('target_guid', 'eval_timestamp', 'address', 'hash_value', 'plan_hash_value', 'id', 'reason_code', 'attribute'),)


class MgmtPolicies(models.Model):
    policy_guid = models.TextField(primary_key=True)  # This field type is a guess.
    policy_name = models.CharField(max_length=128)
    metric_guid = models.TextField()  # This field type is a guess.
    target_type = models.CharField(max_length=64)
    start_type_meta_ver = models.CharField(max_length=8, blank=True, null=True)
    end_type_meta_ver = models.CharField(max_length=8, blank=True, null=True)
    policy_type = models.NullBooleanField()
    policy_label_nlsid = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    description_nlsid = models.CharField(max_length=64, blank=True, null=True)
    author = models.CharField(max_length=256, blank=True, null=True)
    auto_enable = models.NullBooleanField()
    impact = models.CharField(max_length=500, blank=True, null=True)
    impact_nlsid = models.CharField(max_length=64, blank=True, null=True)
    recommendation = models.CharField(max_length=500, blank=True, null=True)
    recommendation_nlsid = models.CharField(max_length=64, blank=True, null=True)
    violation_level = models.FloatField(blank=True, null=True)
    condition_type = models.NullBooleanField()
    condition = models.CharField(max_length=4000, blank=True, null=True)
    condition_operator = models.FloatField(blank=True, null=True)
    detailed_url_link = models.CharField(max_length=4000, blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)
    message_nlsid = models.CharField(max_length=64, blank=True, null=True)
    clear_message = models.CharField(max_length=4000, blank=True, null=True)
    clear_message_nlsid = models.CharField(max_length=64, blank=True, null=True)
    owner = models.CharField(max_length=256, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=256, blank=True, null=True)
    cs_consider_percentage = models.NullBooleanField()
    repo_timing_enabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_policies'
        unique_together = (('target_type', 'policy_name'),)


class MgmtPolicyAssoc(models.Model):
    object_guid = models.TextField(primary_key=True)  # This field type is a guess.
    policy_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    object_type = models.NullBooleanField()
    policy_type = models.NullBooleanField()
    is_enabled = models.NullBooleanField()
    add_or_delete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_policy_assoc'
        unique_together = (('object_guid', 'policy_guid', 'coll_name'),)


class MgmtPolicyAssocCfg(models.Model):
    object_guid = models.TextField(primary_key=True)  # This field type is a guess.
    policy_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    key_value = models.CharField(max_length=256)
    key_operator = models.FloatField()
    eval_order = models.FloatField(blank=True, null=True)
    is_exception = models.NullBooleanField()
    has_active_baseline = models.NullBooleanField()
    prevent_override = models.NullBooleanField()
    crit_action_job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    warn_action_job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    info_action_job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    fixit_job = models.CharField(max_length=128, blank=True, null=True)
    simultaneous_actions = models.NullBooleanField()
    importance = models.FloatField(blank=True, null=True)
    num_occurrences = models.FloatField(blank=True, null=True)
    is_push = models.NullBooleanField()
    condition_operator = models.FloatField(blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)
    message_nlsid = models.CharField(max_length=64, blank=True, null=True)
    clear_message = models.CharField(max_length=4000, blank=True, null=True)
    clear_message_nlsid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_policy_assoc_cfg'


class MgmtPolicyAssocCfgParams(models.Model):
    object_guid = models.TextField(primary_key=True)  # This field type is a guess.
    policy_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    key_value = models.CharField(max_length=256)
    key_operator = models.FloatField()
    param_name = models.CharField(max_length=64)
    crit_threshold = models.CharField(max_length=256, blank=True, null=True)
    warn_threshold = models.CharField(max_length=256, blank=True, null=True)
    info_threshold = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_policy_assoc_cfg_params'
        unique_together = (('object_guid', 'policy_guid', 'coll_name', 'key_value', 'key_operator', 'param_name'),)


class MgmtPolicyBindVars(models.Model):
    policy_guid = models.TextField(primary_key=True)  # This field type is a guess.
    bind_column_name = models.CharField(max_length=30)
    bind_column_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_policy_bind_vars'
        unique_together = (('policy_guid', 'bind_column_name'),)


class MgmtPolicyParameters(models.Model):
    policy_guid = models.TextField(primary_key=True)  # This field type is a guess.
    param_name = models.CharField(max_length=64)
    param_name_nlsid = models.CharField(max_length=64, blank=True, null=True)
    param_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_policy_parameters'
        unique_together = (('policy_guid', 'param_name'),)


class MgmtPolicyTypeVersions(models.Model):
    policy_guid = models.TextField(primary_key=True)  # This field type is a guess.
    type_meta_ver = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'mgmt_policy_type_versions'
        unique_together = (('policy_guid', 'type_meta_ver'),)


class MgmtPolicyViolCtxtDef(models.Model):
    policy_guid = models.TextField(primary_key=True)  # This field type is a guess.
    column_name = models.CharField(max_length=64)
    metric_guid = models.TextField()  # This field type is a guess.
    column_position = models.FloatField(blank=True, null=True)
    is_hidden = models.NullBooleanField()
    url_link_template = models.CharField(max_length=4000, blank=True, null=True)
    url_link_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_policy_viol_ctxt_def'
        unique_together = (('policy_guid', 'column_name'),)


class MgmtPrivGrants(models.Model):
    grantee = models.CharField(primary_key=True, max_length=256)
    priv_name = models.ForeignKey('MgmtPrivs', models.DO_NOTHING, db_column='priv_name')
    guid = models.TextField()  # This field type is a guess.
    grantee_is_role = models.BooleanField()
    direct_grant = models.BooleanField()
    ref_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_priv_grants'
        unique_together = (('grantee', 'priv_name', 'guid'),)


class MgmtPrivIncludes(models.Model):
    priv_name = models.ForeignKey('MgmtPrivs', models.DO_NOTHING, db_column='priv_name', primary_key=True)
    ipriv_name = models.ForeignKey('MgmtPrivs', models.DO_NOTHING, db_column='ipriv_name')

    class Meta:
        managed = False
        db_table = 'mgmt_priv_includes'
        unique_together = (('priv_name', 'ipriv_name'),)


class MgmtPrivs(models.Model):
    priv_name = models.CharField(primary_key=True, max_length=30)
    priv_type = models.BooleanField()
    creator = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_privs'


class MgmtProvAsnDependencies(models.Model):
    parent_asn_guid = models.TextField()  # This field type is a guess.
    child_asn_guid = models.TextField()  # This field type is a guess.
    dep_on_asn_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_prov_asn_dependencies'


class MgmtProvAsnTargets(models.Model):
    assignment_guid = models.TextField(primary_key=True)  # This field type is a guess.
    prov_tgt_guid = models.TextField()  # This field type is a guess.
    properties = models.BinaryField(blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_asn_targets'
        unique_together = (('assignment_guid', 'prov_tgt_guid'),)


class MgmtProvAssignment(models.Model):
    assignment_guid = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    assignment_type = models.CharField(max_length=30, blank=True, null=True)
    assignment_subtype = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    component_urn = models.CharField(max_length=255, blank=True, null=True)
    network_urn = models.CharField(max_length=255, blank=True, null=True)
    boot_server_urn = models.CharField(max_length=255, blank=True, null=True)
    stage_urn = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    stage_username = models.CharField(max_length=255, blank=True, null=True)
    stage_password = models.CharField(max_length=255, blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)
    target_reset_time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_assignment'


class MgmtProvBootserver(models.Model):
    boot_guid = models.TextField(primary_key=True)  # This field type is a guess.
    boot_host_name = models.CharField(max_length=255, blank=True, null=True)
    boot_config_dir = models.CharField(max_length=255, blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_bootserver'
        unique_together = (('boot_host_name', 'boot_config_dir'),)


class MgmtProvCluster(models.Model):
    cluster_guid = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_cluster_urn = models.CharField(max_length=255, blank=True, null=True)
    purpose = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_cluster'


class MgmtProvClusterNodes(models.Model):
    node_guid = models.TextField(primary_key=True)  # This field type is a guess.
    cluster_guid = models.TextField()  # This field type is a guess.
    status = models.CharField(max_length=30, blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)
    prov_asn_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_prov_cluster_nodes'
        unique_together = (('node_guid', 'cluster_guid'),)


class MgmtProvCollection(models.Model):
    collected_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_collection'


class MgmtProvDefaultImage(models.Model):
    default_guid = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    ip_address_prefix = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_default_image'


class MgmtProvHardware(models.Model):
    hw_guid = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    new_hostname = models.CharField(max_length=255, blank=True, null=True)
    mac_address1 = models.CharField(max_length=30, blank=True, null=True)
    mac_address2 = models.CharField(max_length=30, blank=True, null=True)
    mac_address3 = models.CharField(max_length=30, blank=True, null=True)
    mac_address4 = models.CharField(max_length=30, blank=True, null=True)
    interface_name1 = models.CharField(max_length=128, blank=True, null=True)
    interface_name2 = models.CharField(max_length=128, blank=True, null=True)
    interface_name3 = models.CharField(max_length=128, blank=True, null=True)
    interface_name4 = models.CharField(max_length=128, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    rf_id = models.CharField(max_length=255, blank=True, null=True)
    purpose = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_hardware'


class MgmtProvHistory(models.Model):
    prov_tgt_guid = models.TextField()  # This field type is a guess.
    op_guid = models.TextField()  # This field type is a guess.
    assignment_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    hostname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_history'


class MgmtProvIpRange(models.Model):
    ip_range_guid = models.TextField(primary_key=True)  # This field type is a guess.
    last_modified_time = models.DateTimeField(blank=True, null=True)
    ip_range_first = models.CharField(max_length=255, blank=True, null=True)
    ip_range_last = models.CharField(max_length=255, blank=True, null=True)
    ip_range_count = models.BigIntegerField(blank=True, null=True)
    ip_range_name_pattern = models.CharField(max_length=255, blank=True, null=True)
    ip_range_start_value = models.BigIntegerField(blank=True, null=True)
    ip_range_state = models.CharField(max_length=32, blank=True, null=True)
    net_config_guid = models.ForeignKey('MgmtProvNetConfig', models.DO_NOTHING, db_column='net_config_guid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_ip_range'


class MgmtProvIpReserved(models.Model):
    ip_addr = models.CharField(primary_key=True, max_length=255)
    ip_owner_urn = models.CharField(max_length=255, blank=True, null=True)
    ip_range_guid = models.ForeignKey(MgmtProvIpRange, models.DO_NOTHING, db_column='ip_range_guid', blank=True, null=True)
    hostname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    net_config_guid = models.ForeignKey('MgmtProvNetConfig', models.DO_NOTHING, db_column='net_config_guid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_ip_reserved'


class MgmtProvNetConfig(models.Model):
    net_config_guid = models.TextField(primary_key=True)  # This field type is a guess.
    last_modified_time = models.DateTimeField(blank=True, null=True)
    net_config_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    net_domain_name = models.CharField(max_length=255, blank=True, null=True)
    net_subnet_mask = models.CharField(max_length=255, blank=True, null=True)
    net_gateway_addrs = models.CharField(max_length=512, blank=True, null=True)
    net_dns_addrs = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_net_config'


class MgmtProvOperation(models.Model):
    op_guid = models.TextField(primary_key=True)  # This field type is a guess.
    creation_time = models.DateTimeField(blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)
    fraction_complete = models.FloatField(blank=True, null=True)
    status_msg = models.CharField(max_length=255, blank=True, null=True)
    op_type = models.CharField(max_length=30, blank=True, null=True)
    job_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_operation'


class MgmtProvRpmRep(models.Model):
    rpm_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rpm_name = models.CharField(max_length=255, blank=True, null=True)
    rpm_dir = models.CharField(max_length=255, blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_rpm_rep'
        unique_together = (('rpm_name', 'rpm_dir'),)


class MgmtProvStagedComps(models.Model):
    stage_guid = models.TextField()  # This field type is a guess.
    comp_urn = models.CharField(max_length=255, blank=True, null=True)
    comp_dir = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_staged_comps'
        unique_together = (('comp_urn', 'stage_guid'),)


class MgmtProvStagingDirs(models.Model):
    stage_guid = models.TextField(primary_key=True)  # This field type is a guess.
    stage_server_hostname = models.CharField(max_length=255, blank=True, null=True)
    nfs_exposed_dir = models.CharField(max_length=255, blank=True, null=True)
    base_url = models.CharField(max_length=255, blank=True, null=True)
    size_limit = models.FloatField(blank=True, null=True)
    current_size = models.FloatField(blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_staging_dirs'
        unique_together = (('stage_server_hostname', 'nfs_exposed_dir'),)


class MgmtProvSuiteInstMembers(models.Model):
    member_guid = models.TextField(primary_key=True)  # This field type is a guess.
    suite_inst_guid = models.TextField()  # This field type is a guess.
    member_type = models.CharField(max_length=20, blank=True, null=True)
    member_component_urn = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    last_modified_time = models.DateTimeField(blank=True, null=True)
    prov_asn_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_prov_suite_inst_members'
        unique_together = (('member_guid', 'suite_inst_guid'),)


class MgmtProvSuiteInstance(models.Model):
    suite_inst_guid = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    suite_urn = models.CharField(max_length=255, blank=True, null=True)
    purpose = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_suite_instance'


class MgmtProvTgtStatus(models.Model):
    prov_tgt_guid = models.TextField(primary_key=True)  # This field type is a guess.
    prov_target_type = models.CharField(max_length=30, blank=True, null=True)
    current_asn_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_suc_asn_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    component_urn = models.CharField(max_length=255, blank=True, null=True)
    network_urn = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_prov_tgt_status'


class MgmtPurgePolicy(models.Model):
    policy_name = models.CharField(primary_key=True, max_length=64)
    policy_description = models.CharField(max_length=256, blank=True, null=True)
    policy_type = models.FloatField(blank=True, null=True)
    rollup_proc_name = models.CharField(max_length=128, blank=True, null=True)
    purge_proc_name = models.CharField(max_length=128, blank=True, null=True)
    execution_group_name = models.CharField(max_length=64, blank=True, null=True)
    policy_retention_hours = models.FloatField(blank=True, null=True)
    retention_group_name = models.CharField(max_length=64, blank=True, null=True)
    user_configurable = models.FloatField(blank=True, null=True)
    is_enabled = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_purge_policy'


class MgmtPurgePolicyGroup(models.Model):
    group_name = models.CharField(primary_key=True, max_length=64)
    group_description = models.CharField(max_length=256, blank=True, null=True)
    group_retention_hours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_purge_policy_group'


class MgmtPurgePolicyTargetState(models.Model):
    policy_name = models.CharField(max_length=64)
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    can_rollup_upto_time = models.DateField()
    rolledup_upto_time = models.DateField()
    target_retention_hours = models.FloatField(blank=True, null=True)
    last_apply_time = models.DateField(blank=True, null=True)
    last_apply_status = models.FloatField(blank=True, null=True)
    last_apply_msg = models.CharField(max_length=256, blank=True, null=True)
    last_apply_rows = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_purge_policy_target_state'
        unique_together = (('target_guid', 'policy_name'),)


class MgmtRacServices(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    ecm_data_version = models.FloatField()
    ivid = models.TextField()  # This field type is a guess.
    database_unique_name = models.CharField(max_length=30)
    service_name = models.CharField(max_length=30)
    service_type = models.CharField(max_length=30, blank=True, null=True)
    enabled = models.CharField(max_length=30, blank=True, null=True)
    tafpolicy = models.CharField(max_length=30, blank=True, null=True)
    preferred_instances = models.CharField(max_length=1024, blank=True, null=True)
    available_instances = models.CharField(max_length=1024, blank=True, null=True)
    running_instances = models.CharField(max_length=1024, blank=True, null=True)
    cluster_name = models.CharField(max_length=64, blank=True, null=True)
    server_group = models.CharField(max_length=1024, blank=True, null=True)
    resource_name = models.CharField(max_length=64, blank=True, null=True)
    service_centric_type = models.CharField(max_length=30, blank=True, null=True)
    service_cardinality = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rac_services'
        unique_together = (('ecm_snapshot', 'ecm_data_version', 'database_unique_name', 'service_name'),)


class MgmtRcaEvent(models.Model):
    event_guid = models.TextField(primary_key=True)  # This field type is a guess.
    source_type = models.FloatField()
    source_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    collection_time = models.DateTimeField()
    test_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    event_action = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rca_event'


class MgmtRcaEventAssoc(models.Model):
    event_guid = models.ForeignKey('MgmtRcaRun', models.DO_NOTHING, db_column='event_guid', primary_key=True)
    update = models.ForeignKey('MgmtRcaRun', models.DO_NOTHING)
    symptom_event_guid = models.ForeignKey(MgmtRcaEvent, models.DO_NOTHING, db_column='symptom_event_guid')
    cause_event_guid = models.ForeignKey(MgmtRcaEvent, models.DO_NOTHING, db_column='cause_event_guid')
    is_root_cause = models.FloatField()
    cause_confidence = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rca_event_assoc'
        unique_together = (('event_guid', 'update', 'symptom_event_guid', 'cause_event_guid'),)


class MgmtRcaMetricProps(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    interactive_rca = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_rca_metric_props'


class MgmtRcaMetricTest(models.Model):
    metric_test_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256, blank=True, null=True)
    key_part1_value = models.CharField(max_length=256, blank=True, null=True)
    key_part2_value = models.CharField(max_length=256, blank=True, null=True)
    key_part3_value = models.CharField(max_length=256, blank=True, null=True)
    key_part4_value = models.CharField(max_length=256, blank=True, null=True)
    key_part5_value = models.CharField(max_length=256, blank=True, null=True)
    scope = models.FloatField()
    scope_guid = models.TextField()  # This field type is a guess.
    threshold_source = models.FloatField()
    operator = models.FloatField(blank=True, null=True)
    rca_threshold = models.CharField(max_length=256, blank=True, null=True)
    message_nlsid = models.CharField(max_length=128, blank=True, null=True)
    message_params = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rca_metric_test'


class MgmtRcaRecovery(models.Model):
    source_guid = models.TextField()  # This field type is a guess.
    start_time = models.DateField()
    recovery_type = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_rca_recovery'


class MgmtRcaRun(models.Model):
    event_guid = models.ForeignKey(MgmtRcaEvent, models.DO_NOTHING, db_column='event_guid', primary_key=True)
    update_id = models.FloatField()
    cause_count = models.FloatField(blank=True, null=True)
    exception_count = models.FloatField(blank=True, null=True)
    start_time = models.DateField()
    end_time = models.DateField()
    status = models.FloatField()
    error_text = models.CharField(max_length=256, blank=True, null=True)
    event_hash = models.CharField(max_length=256, blank=True, null=True)
    confidence_actual = models.FloatField(blank=True, null=True)
    confidence_possible = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rca_run'
        unique_together = (('event_guid', 'update_id'),)


class MgmtRcaSummary(models.Model):
    event_guid = models.ForeignKey(MgmtRcaEvent, models.DO_NOTHING, db_column='event_guid', primary_key=True)
    last_update_id = models.FloatField()
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    rca_type = models.FloatField()
    rca_status = models.FloatField()
    last_run_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rca_summary'


class MgmtRcaTargetProps(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    interactive_rca = models.FloatField()
    collect_on_demand = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_rca_target_props'


class MgmtRcaTestResult(models.Model):
    result_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_test_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    collection_timestamp = models.DateField()
    test_value = models.CharField(max_length=256)
    last_coll_timestamp = models.DateField(blank=True, null=True)
    last_test_value = models.CharField(max_length=256, blank=True, null=True)
    result_status = models.BooleanField()
    message = models.CharField(max_length=4000, blank=True, null=True)
    message_nlsid = models.CharField(max_length=64, blank=True, null=True)
    message_params = models.CharField(max_length=4000, blank=True, null=True)
    is_status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_rca_test_result'


class MgmtRcaTrace(models.Model):
    event_guid = models.ForeignKey(MgmtRcaRun, models.DO_NOTHING, db_column='event_guid', primary_key=True)
    update = models.ForeignKey(MgmtRcaRun, models.DO_NOTHING)
    trace_doc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rca_trace'
        unique_together = (('event_guid', 'update'),)


class MgmtRcvcatConfig(models.Model):
    rcvcat_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    rcvcat_version = models.CharField(max_length=15, blank=True, null=True)
    rcvcat_connect_str = models.CharField(max_length=1024, blank=True, null=True)
    rcvcat_username = models.CharField(max_length=128, blank=True, null=True)
    rcvcat_password = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    vpcbase_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    em_user = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rcvcat_config'
        unique_together = (('rcvcat_guid', 'em_user'),)


class MgmtRcvcatRepos(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    use_rcvcat = models.CharField(max_length=4, blank=True, null=True)
    rcvcat_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    em_user = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rcvcat_repos'
        unique_together = (('target_guid', 'em_user'),)


class MgmtRebuildIndexes(models.Model):
    table_name = models.CharField(primary_key=True, max_length=30)
    interval = models.FloatField()
    table_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rebuild_indexes'


class MgmtRoleGrants(models.Model):
    grantee = models.CharField(primary_key=True, max_length=256)
    role_name = models.ForeignKey('MgmtRoles', models.DO_NOTHING, db_column='role_name')
    with_admin = models.BooleanField()
    grantee_is_role = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_role_grants'
        unique_together = (('grantee', 'role_name'),)


class MgmtRoles(models.Model):
    role_name = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_roles'


class MgmtRowsetHandlers(models.Model):
    rowset_name = models.CharField(primary_key=True, max_length=32)
    protocol_version = models.CharField(max_length=16)
    handler_type = models.IntegerField()
    handler_info = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rowset_handlers'
        unique_together = (('rowset_name', 'protocol_version', 'handler_type'),)


class MgmtRtBootstrapTimes(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rollup_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_bootstrap_times'


class MgmtRtCookieData(models.Model):
    raw_index = models.CharField(primary_key=True, max_length=256)
    name = models.CharField(max_length=256)
    value = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_cookie_data'
        unique_together = (('raw_index', 'name', 'value'),)


class MgmtRtDomain1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_domain = models.CharField(max_length=1024)
    visitor_subnet = models.CharField(max_length=15)
    visitor_subnet_num = models.FloatField()
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_domain_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_domain', 'visitor_subnet'),)


class MgmtRtDomain1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_domain = models.CharField(max_length=1024)
    visitor_subnet = models.CharField(max_length=15)
    visitor_subnet_num = models.FloatField()
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_domain_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_domain', 'visitor_subnet'),)


class MgmtRtDomainBootstrap(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_domain = models.CharField(max_length=1024)
    visitor_subnet = models.CharField(max_length=15)
    visitor_subnet_num = models.FloatField()
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_domain_bootstrap'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_domain', 'visitor_subnet'),)


class MgmtRtDomainDist1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_domain = models.CharField(max_length=1024)
    visitor_subnet = models.CharField(max_length=15)
    visitor_subnet_num = models.FloatField()
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_domain_dist_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_domain', 'visitor_subnet', 'num_seconds', 'dist_value_type'),)


class MgmtRtDomainDist1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_domain = models.CharField(max_length=1024)
    visitor_subnet = models.CharField(max_length=15)
    visitor_subnet_num = models.FloatField()
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_domain_dist_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_domain', 'visitor_subnet', 'num_seconds', 'dist_value_type'),)


class MgmtRtDomainDistBootstrap(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_domain = models.CharField(max_length=1024)
    visitor_subnet = models.CharField(max_length=15)
    visitor_subnet_num = models.FloatField()
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_domain_dist_bootstrap'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_domain', 'visitor_subnet', 'num_seconds', 'dist_value_type'),)


class MgmtRtIncompleteLoads(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    page_url = models.CharField(max_length=1024)
    num_incomplete_loads = models.FloatField(blank=True, null=True)
    avg_server_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aggregate_hour_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_incomplete_loads'


class MgmtRtIncompleteLoads1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    page_url = models.CharField(max_length=1024)
    num_incomplete_loads = models.FloatField(blank=True, null=True)
    avg_server_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rollup_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_incomplete_loads_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'page_url'),)


class MgmtRtIncompleteLoads1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    page_url = models.CharField(max_length=1024)
    num_incomplete_loads = models.FloatField(blank=True, null=True)
    avg_server_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rollup_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_incomplete_loads_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'page_url'),)


class MgmtRtIp1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_node = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_ip_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_node'),)


class MgmtRtIp1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_node = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_ip_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_node'),)


class MgmtRtIpBootstrap(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_node = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_ip_bootstrap'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_node'),)


class MgmtRtIpDist1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_node = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_ip_dist_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_node', 'num_seconds', 'dist_value_type'),)


class MgmtRtIpDist1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_node = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_ip_dist_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_node', 'num_seconds', 'dist_value_type'),)


class MgmtRtIpDistBootstrap(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    visitor_node = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_ip_dist_bootstrap'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'visitor_node', 'num_seconds', 'dist_value_type'),)


class MgmtRtMetricsRaw(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    collection_timestamp = models.DateField()
    status = models.FloatField(blank=True, null=True)
    status_description = models.CharField(max_length=128, blank=True, null=True)
    submit_action_timestamp = models.FloatField()
    load_action_timestamp = models.FloatField(blank=True, null=True)
    elapsed_time = models.FloatField(blank=True, null=True)
    url_filename = models.CharField(max_length=1024)
    url_base = models.CharField(max_length=256, blank=True, null=True)
    visitor_node = models.CharField(max_length=1024, blank=True, null=True)
    visitor_domain = models.CharField(max_length=1024, blank=True, null=True)
    visitor_ip = models.CharField(max_length=15)
    visitor_ip_num = models.FloatField(blank=True, null=True)
    server_in_timestamp = models.FloatField(blank=True, null=True)
    server_out_timestamp = models.FloatField(blank=True, null=True)
    server_latency_time = models.FloatField(blank=True, null=True)
    database_time = models.FloatField(blank=True, null=True)
    icx_session_id = models.CharField(max_length=32, blank=True, null=True)
    browser_name = models.CharField(max_length=64, blank=True, null=True)
    browser_version = models.CharField(max_length=16, blank=True, null=True)
    os_name = models.CharField(max_length=64, blank=True, null=True)
    os_version = models.CharField(max_length=25, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    cookie_index = models.CharField(max_length=256, blank=True, null=True)
    cache_rendered = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_metrics_raw'
        unique_together = (('target_guid', 'collection_timestamp', 'url_filename', 'metric_name', 'submit_action_timestamp', 'visitor_ip'),)


class MgmtRtPrMapping(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    page_url = models.CharField(max_length=1024)
    request_url = models.CharField(max_length=1024)
    num_cache_hits = models.FloatField(blank=True, null=True)
    cache_hits_avg_svr_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    num_non_cache_hits = models.FloatField(blank=True, null=True)
    non_cache_hits_avg_svr_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aggregate_hour_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_pr_mapping'


class MgmtRtPrMapping1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    page_url = models.CharField(max_length=1024)
    request_url = models.CharField(max_length=1024)
    num_cache_hits = models.FloatField(blank=True, null=True)
    cache_hits_avg_svr_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    num_non_cache_hits = models.FloatField(blank=True, null=True)
    non_cache_hits_avg_svr_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rollup_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_pr_mapping_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'page_url', 'request_url'),)


class MgmtRtPrMapping1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    page_url = models.CharField(max_length=1024)
    request_url = models.CharField(max_length=1024)
    num_cache_hits = models.FloatField(blank=True, null=True)
    cache_hits_avg_svr_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    num_non_cache_hits = models.FloatField(blank=True, null=True)
    non_cache_hits_avg_svr_time = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rollup_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_pr_mapping_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'page_url', 'request_url'),)


class MgmtRtRegionEntries(models.Model):
    id = models.FloatField(primary_key=True)
    min_ip = models.FloatField()
    max_ip = models.FloatField()
    domain = models.CharField(unique=True, max_length=1024)
    ref_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_region_entries'


class MgmtRtRegionMapping(models.Model):
    id = models.FloatField(primary_key=True)
    region_guid = models.ForeignKey('MgmtRtRegions', models.DO_NOTHING, db_column='region_guid')

    class Meta:
        managed = False
        db_table = 'mgmt_rt_region_mapping'
        unique_together = (('id', 'region_guid'),)


class MgmtRtRegions(models.Model):
    region_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    region_name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_regions'
        unique_together = (('target_guid', 'region_name'),)


class MgmtRtTargetProperties(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    property_name = models.CharField(max_length=64)
    property_value = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_target_properties'
        unique_together = (('target_guid', 'property_name'),)


class MgmtRtUrl1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    url_filename = models.CharField(max_length=1024)
    url_link = models.CharField(max_length=1280)
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_url_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'url_filename', 'url_link'),)


class MgmtRtUrl1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    url_filename = models.CharField(max_length=1024)
    url_link = models.CharField(max_length=1280)
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_url_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'url_filename', 'url_link'),)


class MgmtRtUrlBootstrap(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    url_filename = models.CharField(max_length=1024)
    url_link = models.CharField(max_length=1280)
    rollup_timestamp = models.DateField()
    hits = models.FloatField()
    response_time_average = models.FloatField()
    response_time_minimum = models.FloatField()
    response_time_maximum = models.FloatField()
    response_time_sdev = models.FloatField()
    response_time_variance = models.FloatField()
    server_time_average = models.FloatField()
    server_time_minimum = models.FloatField()
    server_time_maximum = models.FloatField()
    server_time_sdev = models.FloatField()
    server_time_variance = models.FloatField()
    db_time_average = models.FloatField(blank=True, null=True)
    db_time_minimum = models.FloatField(blank=True, null=True)
    db_time_maximum = models.FloatField(blank=True, null=True)
    db_time_sdev = models.FloatField(blank=True, null=True)
    db_time_variance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_url_bootstrap'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'url_filename', 'url_link'),)


class MgmtRtUrlDist1Day(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    url_filename = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_url_dist_1day'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'url_filename', 'num_seconds', 'dist_value_type'),)


class MgmtRtUrlDist1Hour(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    url_filename = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_url_dist_1hour'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'url_filename', 'num_seconds', 'dist_value_type'),)


class MgmtRtUrlDistBootstrap(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    url_filename = models.CharField(max_length=1024)
    rollup_timestamp = models.DateField()
    hits = models.FloatField(blank=True, null=True)
    num_seconds = models.FloatField()
    dist_value_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_rt_url_dist_bootstrap'
        unique_together = (('target_guid', 'rollup_timestamp', 'metric_name', 'url_filename', 'num_seconds', 'dist_value_type'),)


class MgmtRtUrls(models.Model):
    url_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    display_name = models.CharField(max_length=128)
    url_filename = models.CharField(max_length=512)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_rt_urls'
        unique_together = (('target_guid', 'display_name'), ('target_guid', 'url_filename'),)


class MgmtSecInfo(models.Model):
    ipw = models.CharField(max_length=256, blank=True, null=True)
    ca_pki = models.BinaryField(blank=True, null=True)
    ca_pwd = models.CharField(max_length=128, blank=True, null=True)
    ca = models.BinaryField(blank=True, null=True)
    b64_local_ca = models.TextField(blank=True, null=True)
    b64_internet_ca = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_sec_info'


class MgmtSeverityRbk(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rbk_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    collection_timestamp = models.DateField()
    severity_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    severity_code = models.FloatField()
    severity_type = models.FloatField()
    severity_duration = models.FloatField(blank=True, null=True)
    annotated_flag = models.FloatField(blank=True, null=True)
    notification_status = models.FloatField(blank=True, null=True)
    message = models.CharField(max_length=4000, blank=True, null=True)
    message_nlsid = models.CharField(max_length=64, blank=True, null=True)
    message_params = models.CharField(max_length=4000, blank=True, null=True)
    action_message = models.CharField(max_length=4000, blank=True, null=True)
    action_message_nlsid = models.CharField(max_length=64, blank=True, null=True)
    action_message_params = models.CharField(max_length=4000, blank=True, null=True)
    advisory_id = models.CharField(max_length=64, blank=True, null=True)
    load_timestamp = models.DateField(blank=True, null=True)
    user_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_severity_rbk'
        unique_together = (('target_guid', 'rbk_guid', 'metric_guid', 'key_value', 'collection_timestamp', 'severity_code'),)


class MgmtSlMetrics(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mgmt_sl_metrics'
        unique_together = (('target_guid', 'metric_guid', 'key_value'),)


class MgmtSlMetricsHistory(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256, blank=True, null=True)
    load_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_sl_metrics_history'


class MgmtSlRules(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    date_sequence = models.CharField(max_length=7)
    start_time = models.CharField(max_length=4)
    end_time = models.CharField(max_length=4)
    avail_includes = models.FloatField()
    expected_sl = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_sl_rules'


class MgmtSlRulesHistory(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    date_sequence = models.CharField(max_length=7)
    start_time = models.CharField(max_length=4)
    end_time = models.CharField(max_length=4)
    avail_includes = models.FloatField()
    expected_sl = models.FloatField()
    load_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_sl_rules_history'


class MgmtSnapshotMetricMap(models.Model):
    snapshot_target_type = models.CharField(primary_key=True, max_length=64)
    snapshot_name = models.CharField(max_length=64)
    metric_guid = models.TextField()  # This field type is a guess.
    store_metric = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_snapshot_metric_map'
        unique_together = (('snapshot_target_type', 'snapshot_name', 'metric_guid'),)


class MgmtSpaceMetrics(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    collection_timestamp = models.DateField()
    object = models.CharField(max_length=150)
    tablespace = models.CharField(max_length=30, blank=True, null=True)
    segment_type = models.FloatField()
    problem_code = models.IntegerField()
    recommendations = models.IntegerField()
    value1 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_space_metrics'
        unique_together = (('target_guid', 'collection_timestamp', 'object', 'segment_type', 'metric_name', 'problem_code'),)


class MgmtSqlBindVars(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    collection_timestamp = models.DateField()
    load_timestamp = models.DateField(blank=True, null=True)
    digest = models.TextField()  # This field type is a guess.
    application = models.CharField(max_length=256, blank=True, null=True)
    module = models.CharField(max_length=256, blank=True, null=True)
    normalized_digest = models.TextField(blank=True, null=True)  # This field type is a guess.
    sharable_mem = models.FloatField(blank=True, null=True)
    persistent_mem = models.FloatField(blank=True, null=True)
    runtime_mem = models.FloatField(blank=True, null=True)
    loaded_versions = models.FloatField(blank=True, null=True)
    executions = models.FloatField(blank=True, null=True)
    loads = models.FloatField(blank=True, null=True)
    invalidations = models.FloatField(blank=True, null=True)
    parse_calls = models.FloatField(blank=True, null=True)
    parsing_user = models.CharField(max_length=30, blank=True, null=True)
    kept_versions = models.FloatField(blank=True, null=True)
    hash_value = models.FloatField(blank=True, null=True)
    action = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_sql_bind_vars'
        unique_together = (('target_guid', 'collection_timestamp', 'metric_name', 'digest'),)


class MgmtSqlEvaluation(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField()
    eval_timestamp = models.DateField()
    snap_id = models.IntegerField()
    address = models.TextField()  # This field type is a guess.
    hash_value = models.FloatField()
    plan_hash_value = models.FloatField()
    reason_code = models.FloatField()
    derived_metric = models.FloatField(blank=True, null=True)
    severity_code = models.FloatField(blank=True, null=True)
    severity = models.FloatField(blank=True, null=True)
    eval_type = models.FloatField()
    sql_text = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_sql_evaluation'
        unique_together = (('target_guid', 'eval_timestamp', 'reason_code', 'address', 'hash_value', 'plan_hash_value'),)


class MgmtSqlMetricHelper(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField(blank=True, null=True)
    snap_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_sql_metric_helper'


class MgmtSqlPlan(models.Model):
    snap_id = models.IntegerField()
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField()
    address = models.TextField()  # This field type is a guess.
    hash_value = models.FloatField()
    operation = models.CharField(max_length=30, blank=True, null=True)
    options = models.CharField(max_length=30, blank=True, null=True)
    object_node = models.CharField(max_length=128, blank=True, null=True)
    object_owner = models.CharField(max_length=30, blank=True, null=True)
    object_name = models.CharField(max_length=64, blank=True, null=True)
    optimizer = models.CharField(max_length=20, blank=True, null=True)
    id = models.FloatField()
    parent_id = models.FloatField(blank=True, null=True)
    position = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    cardinality = models.FloatField(blank=True, null=True)
    bytes = models.FloatField(blank=True, null=True)
    other_tag = models.CharField(max_length=35, blank=True, null=True)
    partition_start = models.CharField(max_length=5, blank=True, null=True)
    partition_stop = models.CharField(max_length=5, blank=True, null=True)
    partition_id = models.FloatField(blank=True, null=True)
    other = models.CharField(max_length=4000, blank=True, null=True)
    distribution = models.CharField(max_length=30, blank=True, null=True)
    cpu_cost = models.FloatField(blank=True, null=True)
    io_cost = models.FloatField(blank=True, null=True)
    temp_space = models.FloatField(blank=True, null=True)
    plan_hash_value = models.FloatField()
    object_number = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_sql_plan'
        unique_together = (('target_guid', 'snap_id', 'address', 'hash_value', 'plan_hash_value', 'id'),)


class MgmtSqlReuse(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_name = models.CharField(max_length=64)
    collection_timestamp = models.DateField()
    load_timestamp = models.DateField(blank=True, null=True)
    sql_text = models.CharField(max_length=4000, blank=True, null=True)
    application = models.CharField(max_length=256, blank=True, null=True)
    module = models.CharField(max_length=256, blank=True, null=True)
    normalized_sql = models.CharField(max_length=4000, blank=True, null=True)
    sharable_mem = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_sql_reuse'
        unique_together = (('target_guid', 'collection_timestamp'),)


class MgmtSqlSummary(models.Model):
    snap_id = models.IntegerField()
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    collection_timestamp = models.DateField()
    sql_text = models.CharField(max_length=64, blank=True, null=True)
    piece = models.FloatField()
    plan_hash_value = models.FloatField()
    application = models.CharField(max_length=256, blank=True, null=True)
    module = models.CharField(max_length=64, blank=True, null=True)
    sharable_mem = models.FloatField(blank=True, null=True)
    sorts = models.FloatField(blank=True, null=True)
    loaded_versions = models.FloatField(blank=True, null=True)
    executions = models.FloatField(blank=True, null=True)
    loads = models.FloatField(blank=True, null=True)
    invalidations = models.FloatField(blank=True, null=True)
    parse_calls = models.FloatField(blank=True, null=True)
    disk_reads = models.FloatField(blank=True, null=True)
    buffer_gets = models.FloatField(blank=True, null=True)
    rows_processed = models.FloatField(blank=True, null=True)
    command_type = models.FloatField(blank=True, null=True)
    address = models.TextField()  # This field type is a guess.
    hash_value = models.FloatField()
    version_count = models.FloatField(blank=True, null=True)
    cpu_time = models.FloatField(blank=True, null=True)
    elapsed_time = models.FloatField(blank=True, null=True)
    outline_sid = models.FloatField(blank=True, null=True)
    outline_category = models.CharField(max_length=64, blank=True, null=True)
    persistent_mem = models.FloatField(blank=True, null=True)
    runtime_mem = models.FloatField(blank=True, null=True)
    optimizer_mode = models.CharField(max_length=25, blank=True, null=True)
    optimizer_cost = models.FloatField(blank=True, null=True)
    parsing_user = models.CharField(max_length=30, blank=True, null=True)
    parsing_schema = models.CharField(max_length=30, blank=True, null=True)
    action = models.CharField(max_length=64, blank=True, null=True)
    literal_hash_value = models.FloatField(blank=True, null=True)
    first_load_time = models.CharField(max_length=19, blank=True, null=True)
    last_load_time = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_sql_summary'
        unique_together = (('target_guid', 'snap_id', 'address', 'hash_value', 'plan_hash_value', 'piece'),)


class MgmtSqlproblemFactors(models.Model):
    target_guid = models.ForeignKey(MgmtSqlEvaluation, models.DO_NOTHING, db_column='target_guid', primary_key=True)
    eval_timestamp = models.ForeignKey(MgmtSqlEvaluation, models.DO_NOTHING, db_column='eval_timestamp')
    address = models.ForeignKey(MgmtSqlEvaluation, models.DO_NOTHING, db_column='address')
    hash_value = models.ForeignKey(MgmtSqlEvaluation, models.DO_NOTHING, db_column='hash_value')
    plan_hash_value = models.ForeignKey(MgmtSqlEvaluation, models.DO_NOTHING, db_column='plan_hash_value')
    reason_code = models.ForeignKey(MgmtSqlEvaluation, models.DO_NOTHING, db_column='reason_code')
    attribute = models.CharField(max_length=64)
    importance = models.CharField(max_length=64, blank=True, null=True)
    confidence = models.CharField(max_length=64, blank=True, null=True)
    sql_text = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_sqlproblem_factors'
        unique_together = (('target_guid', 'eval_timestamp', 'address', 'hash_value', 'plan_hash_value', 'reason_code', 'attribute'),)


class MgmtStorageReportAlias(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    key_value = models.TextField()  # This field type is a guess.
    value = models.CharField(max_length=256)
    file_type = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_storage_report_alias'
        unique_together = (('ecm_snapshot', 'key_value', 'value'),)


class MgmtStorageReportData(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    key_value = models.TextField()  # This field type is a guess.
    global_unique_id = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=256, blank=True, null=True)
    storage_layer = models.CharField(max_length=32, blank=True, null=True)
    em_query_flag = models.CharField(max_length=64, blank=True, null=True)
    entity_type = models.CharField(max_length=64, blank=True, null=True)
    rawsizeb = models.FloatField(blank=True, null=True)
    sizeb = models.FloatField(blank=True, null=True)
    usedb = models.FloatField(blank=True, null=True)
    freeb = models.FloatField(blank=True, null=True)
    a1 = models.CharField(max_length=256, blank=True, null=True)
    a2 = models.CharField(max_length=256, blank=True, null=True)
    a3 = models.CharField(max_length=256, blank=True, null=True)
    a4 = models.CharField(max_length=256, blank=True, null=True)
    a5 = models.CharField(max_length=256, blank=True, null=True)
    a6 = models.CharField(max_length=256, blank=True, null=True)
    a7 = models.CharField(max_length=256, blank=True, null=True)
    a8 = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_storage_report_data'
        unique_together = (('ecm_snapshot', 'key_value'),)


class MgmtStorageReportIssues(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    type = models.CharField(max_length=32)
    message_counter = models.FloatField()
    message_id = models.CharField(max_length=256, blank=True, null=True)
    message_params = models.CharField(max_length=512, blank=True, null=True)
    action_id = models.CharField(max_length=256, blank=True, null=True)
    action_params = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_storage_report_issues'
        unique_together = (('ecm_snapshot', 'type', 'message_counter'),)


class MgmtStorageReportKeys(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    key_value = models.TextField()  # This field type is a guess.
    parent_key_value = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_storage_report_keys'
        unique_together = (('ecm_snapshot', 'key_value', 'parent_key_value'),)


class MgmtStorageReportUiTargets(models.Model):
    target_type = models.CharField(max_length=64)
    target_name = models.CharField(max_length=256)
    target_guid = models.TextField()  # This field type is a guess.
    ecm_snapshot_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_storage_report_ui_targets'


class MgmtStorageTmpNfsData(models.Model):
    key_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    server_name = models.CharField(max_length=256, blank=True, null=True)
    server_mac_address = models.CharField(max_length=256, blank=True, null=True)
    server_ip_address = models.CharField(max_length=256, blank=True, null=True)
    filesystem = models.CharField(max_length=256, blank=True, null=True)
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_name = models.CharField(max_length=256, blank=True, null=True)
    target_type = models.CharField(max_length=256, blank=True, null=True)
    exported_fs = models.CharField(max_length=256, blank=True, null=True)
    global_unique_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_storage_tmp_nfs_data'


class MgmtSwlibDataDirectories(models.Model):
    path_id = models.TextField(primary_key=True)  # This field type is a guess.
    filepath = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_data_directories'


class MgmtSwlibDirectories(models.Model):
    directory_id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    owner = models.CharField(max_length=64, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_directories'


class MgmtSwlibEntities(models.Model):
    entity_id = models.TextField(primary_key=True)  # This field type is a guess.
    name = models.CharField(max_length=64)
    owner = models.CharField(max_length=64)
    creation_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=64)
    directory = models.ForeignKey(MgmtSwlibDirectories, models.DO_NOTHING, blank=True, null=True)
    vendor = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_entities'


class MgmtSwlibEntityData(models.Model):
    revision = models.ForeignKey('MgmtSwlibEntityRevisions', models.DO_NOTHING, primary_key=True)
    external_key = models.CharField(max_length=256, blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_entity_data'


class MgmtSwlibEntityDocuments(models.Model):
    revision = models.ForeignKey('MgmtSwlibEntityRevisions', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=64)
    reference = models.ForeignKey('MgmtSwlibEntityReferences', models.DO_NOTHING, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_entity_documents'


class MgmtSwlibEntityParameters(models.Model):
    entity = models.ForeignKey(MgmtSwlibEntities, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_entity_parameters'
        unique_together = (('entity', 'name'),)


class MgmtSwlibEntityPlatforms(models.Model):
    entity = models.ForeignKey(MgmtSwlibEntities, models.DO_NOTHING, primary_key=True)
    platform = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_entity_platforms'
        unique_together = (('entity', 'platform'),)


class MgmtSwlibEntityReferences(models.Model):
    reference_id = models.TextField(primary_key=True)  # This field type is a guess.
    source = models.ForeignKey('MgmtSwlibEntityRevisions', models.DO_NOTHING)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64, blank=True, null=True)
    refindex = models.IntegerField(blank=True, null=True)
    target = models.ForeignKey(MgmtSwlibEntities, models.DO_NOTHING, blank=True, null=True)
    target_revision = models.ForeignKey('MgmtSwlibEntityRevisions', models.DO_NOTHING, blank=True, null=True)
    target_production = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_entity_references'


class MgmtSwlibEntityRevisions(models.Model):
    revision_id = models.TextField(primary_key=True)  # This field type is a guess.
    entity = models.ForeignKey(MgmtSwlibEntities, models.DO_NOTHING)
    revision = models.CharField(max_length=16)
    modified_date = models.DateField(blank=True, null=True)
    revision_author = models.CharField(max_length=64, blank=True, null=True)
    maturity_status = models.ForeignKey('MgmtSwlibMaturityStatus', models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    product = models.CharField(max_length=64, blank=True, null=True)
    product_version = models.CharField(max_length=16, blank=True, null=True)
    data_type = models.CharField(max_length=64, blank=True, null=True)
    checksum = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_current = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_entity_revisions'


class MgmtSwlibMaturityStatus(models.Model):
    maturity_status_id = models.IntegerField(primary_key=True)
    maturity_status = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_maturity_status'


class MgmtSwlibRevisionParameters(models.Model):
    revision = models.ForeignKey(MgmtSwlibEntityRevisions, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_swlib_revision_parameters'
        unique_together = (('revision', 'name'),)


class MgmtSystemChanges(models.Model):
    ecm_snapshot = models.ForeignKey(MgmtEcmGenSnapshot, models.DO_NOTHING, primary_key=True)
    system_name = models.CharField(max_length=200)
    system_type = models.CharField(max_length=200)
    member_name = models.CharField(max_length=200)
    member_type = models.CharField(max_length=200)
    modified_by = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_system_changes'
        unique_together = (('ecm_snapshot', 'member_name', 'member_type'),)


class MgmtSystemErrorLog(models.Model):
    module_name = models.ForeignKey(MgmtPerformanceNames, models.DO_NOTHING, db_column='module_name')
    occur_date = models.DateField(blank=True, null=True)
    error_code = models.FloatField(blank=True, null=True)
    log_level = models.CharField(max_length=16, blank=True, null=True)
    error_msg = models.CharField(max_length=2048, blank=True, null=True)
    facility = models.CharField(max_length=6, blank=True, null=True)
    client_data = models.CharField(max_length=128, blank=True, null=True)
    host_url = models.CharField(max_length=256, blank=True, null=True)
    emd_url = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_system_error_log'


class MgmtSystemPerformanceLog(models.Model):
    job_name = models.ForeignKey(MgmtPerformanceNames, models.DO_NOTHING, db_column='job_name')
    time = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=512, blank=True, null=True)
    action = models.CharField(max_length=32, blank=True, null=True)
    is_total = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    value = models.CharField(max_length=128, blank=True, null=True)
    client_data = models.CharField(max_length=128, blank=True, null=True)
    host_url = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_system_performance_log'


class MgmtTableSizes(models.Model):
    table_name = models.CharField(max_length=30)
    collection_timestamp = models.DateField(primary_key=True)
    allocated_size = models.FloatField(blank=True, null=True)
    space_used = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_table_sizes'
        unique_together = (('collection_timestamp', 'table_name'),)


class MgmtTargetAddCallbacks(models.Model):
    callback_name = models.CharField(primary_key=True, max_length=100)
    target_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_target_add_callbacks'
        unique_together = (('callback_name', 'target_type'),)


class MgmtTargetAgentAssoc(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    agent_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_target_agent_assoc'
        unique_together = (('target_guid', 'agent_guid'),)


class MgmtTargetAssoc(models.Model):
    target_type = models.CharField(primary_key=True, max_length=256)
    type_meta_ver = models.CharField(max_length=8)
    association = models.CharField(max_length=64)
    assoc_target_type = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_assoc'
        unique_together = (('target_type', 'type_meta_ver', 'association'),)


class MgmtTargetAssocDefs(models.Model):
    assoc_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    assoc_def_name = models.CharField(primary_key=True, max_length=64)
    name_nlsid = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    description_nlsid = models.CharField(max_length=64, blank=True, null=True)
    source_target_type = models.CharField(max_length=64)
    assoc_target_type = models.CharField(max_length=64)
    scope_target_type = models.CharField(max_length=64)
    cardinality = models.NullBooleanField()
    prop_view_priv = models.NullBooleanField()
    association_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_assoc_defs'
        unique_together = (('assoc_def_name', 'source_target_type', 'scope_target_type'),)


class MgmtTargetAssocError(models.Model):
    source_target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    scope_target_guid = models.TextField()  # This field type is a guess.
    assoc_guid = models.TextField()  # This field type is a guess.
    error_code = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_target_assoc_error'
        unique_together = (('source_target_guid', 'assoc_guid', 'scope_target_guid'),)


class MgmtTargetAssocInstance(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    association = models.CharField(max_length=64)
    assoc_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_target_assoc_instance'
        unique_together = (('target_guid', 'association'),)


class MgmtTargetAssocProp(models.Model):
    assoc_guid = models.TextField()  # This field type is a guess.
    source_target_guid = models.TextField()  # This field type is a guess.
    scope_target_guid = models.TextField()  # This field type is a guess.
    assoc_target_guid = models.TextField()  # This field type is a guess.
    property_name = models.CharField(max_length=64, blank=True, null=True)
    property_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_assoc_prop'


class MgmtTargetAssocPropDefs(models.Model):
    assoc_guid = models.TextField(primary_key=True)  # This field type is a guess.
    property_name = models.CharField(max_length=64)
    property_nlsid = models.CharField(max_length=64, blank=True, null=True)
    property_default = models.CharField(max_length=64, blank=True, null=True)
    is_required = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_target_assoc_prop_defs'
        unique_together = (('assoc_guid', 'property_name'),)


class MgmtTargetAssocStatus(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    assoc_count = models.FloatField(blank=True, null=True)
    last_update_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_assoc_status'


class MgmtTargetAssocs(models.Model):
    assoc_guid = models.TextField()  # This field type is a guess.
    source_target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    assoc_target_guid = models.TextField()  # This field type is a guess.
    scope_target_guid = models.TextField()  # This field type is a guess.
    is_editable = models.NullBooleanField()
    created_by = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_target_assocs'
        unique_together = (('source_target_guid', 'assoc_guid', 'assoc_target_guid', 'scope_target_guid'),)


class MgmtTargetBaselines(models.Model):
    baseline_name = models.CharField(max_length=128)
    baseline_date = models.DateField()
    is_active = models.NullBooleanField()
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_target_baselines'
        unique_together = (('target_guid', 'baseline_name'),)


class MgmtTargetBaselinesData(models.Model):
    baseline_name = models.CharField(max_length=128)
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    value_average = models.FloatField(blank=True, null=True)
    value_minimum = models.FloatField(blank=True, null=True)
    value_maximum = models.FloatField(blank=True, null=True)
    warning_operator = models.FloatField(blank=True, null=True)
    warning_threshold = models.CharField(max_length=256, blank=True, null=True)
    critical_operator = models.FloatField(blank=True, null=True)
    critical_threshold = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_baselines_data'
        unique_together = (('target_guid', 'metric_guid', 'key_value', 'baseline_name'),)


class MgmtTargetCredentials(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    credential_set_name = models.CharField(max_length=32)
    user_name = models.CharField(max_length=256)
    pdp_data = models.CharField(max_length=512, blank=True, null=True)
    credential_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_target_credentials'
        unique_together = (('target_guid', 'credential_set_name', 'user_name'),)


class MgmtTargetDeleteCallbacks(models.Model):
    callback_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mgmt_target_delete_callbacks'


class MgmtTargetDeleteExceptions(models.Model):
    table_name = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'mgmt_target_delete_exceptions'


class MgmtTargetPendingAssocs(models.Model):
    assoc_guid = models.TextField()  # This field type is a guess.
    source_target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    assoc_target_guid = models.TextField()  # This field type is a guess.
    scope_target_guid = models.TextField()  # This field type is a guess.
    is_editable = models.NullBooleanField()
    created_by = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_target_pending_assocs'
        unique_together = (('source_target_guid', 'assoc_guid', 'assoc_target_guid', 'scope_target_guid'),)


class MgmtTargetPropDefs(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=8)
    property_name = models.CharField(max_length=64)
    property_type = models.CharField(max_length=64)
    property_display_name = models.CharField(max_length=64)
    property_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    required_flag = models.NullBooleanField()
    credential_flag = models.NullBooleanField()
    default_value = models.CharField(max_length=1024, blank=True, null=True)
    computed_flag = models.BooleanField()
    read_only_flag = models.BooleanField()
    hidden_flag = models.BooleanField()
    system_flag = models.BooleanField()
    all_versions = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_target_prop_defs'
        unique_together = (('target_type', 'type_meta_ver', 'property_name', 'property_type'),)


class MgmtTargetProperties(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    property_name = models.CharField(max_length=64)
    property_type = models.CharField(max_length=64)
    property_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_properties'
        unique_together = (('target_guid', 'property_name', 'property_type'),)


class MgmtTargetRollupTimes(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    rollup_table_name = models.CharField(max_length=64)
    rollup_timestamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'mgmt_target_rollup_times'
        unique_together = (('target_guid', 'rollup_table_name'),)


class MgmtTargetTempList(models.Model):
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_target_temp_list'


class MgmtTargetTypeComponentMap(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    property_name = models.CharField(max_length=64, blank=True, null=True)
    property_value = models.CharField(max_length=1024, blank=True, null=True)
    component_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'mgmt_target_type_component_map'
        unique_together = (('target_type', 'component_name'),)


class MgmtTargetTypeVersions(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=128)
    type_display_name = models.CharField(max_length=128, blank=True, null=True)
    type_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    type_resource_bundle = models.CharField(max_length=256, blank=True, null=True)
    target_type_ver_guid = models.TextField()  # This field type is a guess.
    created_date = models.DateField(blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_type_versions'
        unique_together = (('target_type', 'type_meta_ver'),)


class MgmtTargetTypes(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    type_display_name = models.CharField(max_length=128, blank=True, null=True)
    type_display_nlsid = models.CharField(max_length=64, blank=True, null=True)
    type_resource_bundle = models.CharField(max_length=256, blank=True, null=True)
    target_type_guid = models.TextField()  # This field type is a guess.
    max_type_meta_ver = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_target_types'


class MgmtTargets(models.Model):
    target_name = models.CharField(max_length=256)
    target_type = models.CharField(primary_key=True, max_length=64)
    type_meta_ver = models.CharField(max_length=8, blank=True, null=True)
    category_prop_1 = models.CharField(max_length=64, blank=True, null=True)
    category_prop_2 = models.CharField(max_length=64, blank=True, null=True)
    category_prop_3 = models.CharField(max_length=64, blank=True, null=True)
    category_prop_4 = models.CharField(max_length=64, blank=True, null=True)
    category_prop_5 = models.CharField(max_length=64, blank=True, null=True)
    target_guid = models.TextField(unique=True)  # This field type is a guess.
    load_timestamp = models.DateField(blank=True, null=True)
    timezone_delta = models.FloatField(blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    display_name = models.CharField(max_length=256, blank=True, null=True)
    owner = models.CharField(max_length=256, blank=True, null=True)
    type_display_name = models.CharField(max_length=128, blank=True, null=True)
    service_type = models.CharField(max_length=64, blank=True, null=True)
    host_name = models.CharField(max_length=256, blank=True, null=True)
    emd_url = models.CharField(max_length=1024, blank=True, null=True)
    last_load_time = models.DateField(blank=True, null=True)
    is_group = models.NullBooleanField()
    broken_reason = models.FloatField(blank=True, null=True)
    broken_str = models.CharField(max_length=512, blank=True, null=True)
    last_rt_load_time = models.DateField(blank=True, null=True)
    last_updated_time = models.DateField(blank=True, null=True)
    monitoring_mode = models.FloatField(blank=True, null=True)
    rep_side_avail = models.FloatField(blank=True, null=True)
    last_e2e_load_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_targets'
        unique_together = (('target_type', 'target_name'),)


class MgmtTargetsDelete(models.Model):
    target_name = models.CharField(max_length=256)
    target_type = models.CharField(max_length=64)
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    emd_url = models.CharField(max_length=1024, blank=True, null=True)
    timezone_region = models.CharField(max_length=64, blank=True, null=True)
    delete_request_time = models.DateField(blank=True, null=True)
    delete_complete_time = models.DateField(blank=True, null=True)
    last_updated_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_targets_delete'


class MgmtTaskQtable(models.Model):
    q_name = models.CharField(max_length=30, blank=True, null=True)
    msgid = models.TextField(primary_key=True)  # This field type is a guess.
    corrid = models.CharField(max_length=128, blank=True, null=True)
    priority = models.FloatField(blank=True, null=True)
    state = models.FloatField(blank=True, null=True)
    delay = models.DateTimeField(blank=True, null=True)
    expiration = models.FloatField(blank=True, null=True)
    time_manager_info = models.DateTimeField(blank=True, null=True)
    local_order_no = models.FloatField(blank=True, null=True)
    chain_no = models.FloatField(blank=True, null=True)
    cscn = models.FloatField(blank=True, null=True)
    dscn = models.FloatField(blank=True, null=True)
    enq_time = models.DateTimeField(blank=True, null=True)
    enq_uid = models.CharField(max_length=30, blank=True, null=True)
    enq_tid = models.CharField(max_length=30, blank=True, null=True)
    deq_time = models.DateTimeField(blank=True, null=True)
    deq_uid = models.CharField(max_length=30, blank=True, null=True)
    deq_tid = models.CharField(max_length=30, blank=True, null=True)
    retry_count = models.FloatField(blank=True, null=True)
    exception_qschema = models.CharField(max_length=30, blank=True, null=True)
    exception_queue = models.CharField(max_length=30, blank=True, null=True)
    step_no = models.FloatField(blank=True, null=True)
    recipient_key = models.FloatField(blank=True, null=True)
    dequeue_msgid = models.TextField(blank=True, null=True)  # This field type is a guess.
    sender_name = models.CharField(max_length=30, blank=True, null=True)
    sender_address = models.CharField(max_length=1024, blank=True, null=True)
    sender_protocol = models.FloatField(blank=True, null=True)
    user_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_prop = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_task_qtable'


class MgmtTaskWorkerCounts(models.Model):
    task_class_list = models.CharField(primary_key=True, max_length=64)
    worker_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_task_worker_counts'


class MgmtTemplateCopies(models.Model):
    template_copy_guid = models.TextField(primary_key=True)  # This field type is a guess.
    template_guid = models.TextField()  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    copy_req_guid = models.TextField()  # This field type is a guess.
    copy_type = models.NullBooleanField()
    created_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_template_copies'


class MgmtTemplates(models.Model):
    template_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_type = models.CharField(max_length=64)
    template_name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, blank=True, null=True)
    is_public = models.NullBooleanField()
    owner = models.CharField(max_length=256, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_updated_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_templates'


class MgmtTest(models.Model):
    test_type = models.CharField(primary_key=True, max_length=64)
    label = models.CharField(max_length=64)
    nlsid = models.CharField(max_length=64)
    resource_bundle = models.CharField(max_length=4000)
    collection_generator = models.CharField(max_length=4000)
    min_beacon_ver = models.CharField(max_length=8)
    test_version = models.CharField(max_length=8)
    deprecated = models.CharField(max_length=1)
    avail_metric = models.CharField(max_length=64)
    avail_metric_column = models.CharField(max_length=64, blank=True, null=True)
    help_id = models.CharField(max_length=256, blank=True, null=True)
    tip_text = models.CharField(max_length=4000, blank=True, null=True)
    tip_text_nlsid = models.CharField(max_length=64, blank=True, null=True)
    validator = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_test'


class MgmtTestDefaultPromotion(models.Model):
    test_type = models.ForeignKey('MgmtTestMcolumns', models.DO_NOTHING, db_column='test_type')
    src_metric_name = models.ForeignKey('MgmtTestMcolumns', models.DO_NOTHING, db_column='src_metric_name')
    src_metric_column = models.ForeignKey('MgmtTestMcolumns', models.DO_NOTHING, db_column='src_metric_column')
    src_metric_key1_value = models.CharField(max_length=64, blank=True, null=True)
    src_metric_key2_value = models.CharField(max_length=64, blank=True, null=True)
    src_metric_key3_value = models.CharField(max_length=64, blank=True, null=True)
    src_metric_key4_value = models.CharField(max_length=64, blank=True, null=True)
    src_metric_key5_value = models.CharField(max_length=64, blank=True, null=True)
    eval_func = models.CharField(max_length=256)
    critical = models.FloatField(blank=True, null=True)
    warning = models.FloatField(blank=True, null=True)
    operator = models.CharField(max_length=16)
    num_occurrences = models.FloatField(blank=True, null=True)
    dest_metric_name = models.CharField(max_length=64)
    dest_metric_column = models.CharField(max_length=64)
    dest_metric_key1_value = models.CharField(max_length=64, blank=True, null=True)
    dest_metric_key2_value = models.CharField(max_length=64, blank=True, null=True)
    dest_metric_key3_value = models.CharField(max_length=64, blank=True, null=True)
    dest_metric_key4_value = models.CharField(max_length=64, blank=True, null=True)
    dest_metric_key5_value = models.CharField(max_length=64, blank=True, null=True)
    default_chart = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_test_default_promotion'
        unique_together = (('test_type', 'dest_metric_name', 'dest_metric_column', 'dest_metric_key1_value', 'dest_metric_key2_value', 'dest_metric_key3_value', 'dest_metric_key4_value', 'dest_metric_key5_value'),)


class MgmtTestDefaultThresholds(models.Model):
    test_type = models.ForeignKey('MgmtTestMcolumns', models.DO_NOTHING, db_column='test_type')
    metric_name = models.ForeignKey('MgmtTestMcolumns', models.DO_NOTHING, db_column='metric_name')
    metric_column = models.ForeignKey('MgmtTestMcolumns', models.DO_NOTHING, db_column='metric_column')
    metric_key1_value = models.CharField(max_length=64, blank=True, null=True)
    metric_key2_value = models.CharField(max_length=64, blank=True, null=True)
    metric_key3_value = models.CharField(max_length=64, blank=True, null=True)
    metric_key4_value = models.CharField(max_length=64, blank=True, null=True)
    metric_key5_value = models.CharField(max_length=64, blank=True, null=True)
    critical = models.FloatField(blank=True, null=True)
    warning = models.FloatField(blank=True, null=True)
    operator = models.CharField(max_length=16)
    num_occurrences = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_test_default_thresholds'
        unique_together = (('test_type', 'metric_name', 'metric_column', 'metric_key1_value', 'metric_key2_value', 'metric_key3_value', 'metric_key4_value', 'metric_key5_value'),)


class MgmtTestMcolumns(models.Model):
    test_type = models.ForeignKey('MgmtTestMetrics', models.DO_NOTHING, db_column='test_type', primary_key=True)
    metric_name = models.ForeignKey('MgmtTestMetrics', models.DO_NOTHING, db_column='metric_name')
    metric_column = models.CharField(max_length=64)
    display_order = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_test_mcolumns'
        unique_together = (('test_type', 'metric_name', 'display_order'), ('test_type', 'metric_name', 'metric_column'),)


class MgmtTestMetricProps(models.Model):
    property_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_type = models.CharField(max_length=64)
    type_meta_ver = models.CharField(max_length=8)
    metric_name = models.CharField(max_length=64)
    property_name = models.CharField(max_length=64)
    scope = models.CharField(max_length=64)
    optional = models.CharField(max_length=1)
    encrypt = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_test_metric_props'
        unique_together = (('property_guid', 'type_meta_ver'),)


class MgmtTestMetrics(models.Model):
    test_type = models.ForeignKey(MgmtTest, models.DO_NOTHING, db_column='test_type', primary_key=True)
    metric_name = models.CharField(max_length=64)
    metric_number = models.FloatField()
    interactive = models.CharField(max_length=1)
    level_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_test_metrics'
        unique_together = (('test_type', 'metric_number'), ('test_type', 'metric_name'),)


class MgmtTestProp(models.Model):
    test_type = models.ForeignKey(MgmtTest, models.DO_NOTHING, db_column='test_type', primary_key=True)
    prop_name = models.CharField(max_length=64)
    group_name = models.CharField(max_length=64, blank=True, null=True)
    display_order = models.FloatField(blank=True, null=True)
    label = models.CharField(max_length=64, blank=True, null=True)
    nlsid = models.CharField(max_length=64, blank=True, null=True)
    property_type = models.FloatField()
    default_numeric_value = models.FloatField(blank=True, null=True)
    default_string_value = models.CharField(max_length=4000, blank=True, null=True)
    max_value = models.FloatField(blank=True, null=True)
    min_value = models.FloatField(blank=True, null=True)
    hidden = models.CharField(max_length=1)
    encrypt = models.CharField(max_length=1)
    password = models.CharField(max_length=1)
    varies_per_beacon = models.CharField(max_length=1)
    tip_text = models.CharField(max_length=4000, blank=True, null=True)
    tip_text_nlsid = models.CharField(max_length=64, blank=True, null=True)
    validator = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_test_prop'
        unique_together = (('test_type', 'prop_name'), ('test_type', 'group_name', 'display_order'),)


class MgmtTestPropChoices(models.Model):
    test_type = models.ForeignKey(MgmtTestProp, models.DO_NOTHING, db_column='test_type', primary_key=True)
    prop_name = models.ForeignKey(MgmtTestProp, models.DO_NOTHING, db_column='prop_name')
    choice_name = models.CharField(max_length=64)
    display_order = models.FloatField()
    label = models.CharField(max_length=64)
    nlsid = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mgmt_test_prop_choices'
        unique_together = (('test_type', 'prop_name', 'choice_name'), ('test_type', 'prop_name', 'display_order'),)


class MgmtTestPropLevel(models.Model):
    test_type = models.ForeignKey(MgmtTestProp, models.DO_NOTHING, db_column='test_type', primary_key=True)
    property = models.ForeignKey(MgmtTestProp, models.DO_NOTHING, db_column='property')
    level_name = models.CharField(max_length=64)
    optional = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'mgmt_test_prop_level'
        unique_together = (('test_type', 'property', 'level_name'),)


class MgmtTestPropQualifiers(models.Model):
    test_type = models.ForeignKey(MgmtTestProp, models.DO_NOTHING, db_column='test_type', primary_key=True)
    property = models.ForeignKey(MgmtTestProp, models.DO_NOTHING, db_column='property')
    qualifier = models.CharField(max_length=64)
    text_value = models.CharField(max_length=4000, blank=True, null=True)
    numeric_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_test_prop_qualifiers'
        unique_together = (('test_type', 'property', 'qualifier'),)


class MgmtTestPropUigroup(models.Model):
    test_type = models.ForeignKey(MgmtTest, models.DO_NOTHING, db_column='test_type', primary_key=True)
    group_name = models.CharField(max_length=64)
    display_order = models.FloatField()
    label = models.CharField(max_length=64)
    nlsid = models.CharField(max_length=64)
    tip_text = models.CharField(max_length=4000, blank=True, null=True)
    tip_text_nlsid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_test_prop_uigroup'
        unique_together = (('test_type', 'display_order'), ('test_type', 'group_name'),)


class MgmtTestQualifiers(models.Model):
    test_type = models.ForeignKey(MgmtTest, models.DO_NOTHING, db_column='test_type', primary_key=True)
    qualifier = models.CharField(max_length=64)
    text_value = models.CharField(max_length=4000, blank=True, null=True)
    numeric_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_test_qualifiers'
        unique_together = (('test_type', 'qualifier'),)


class MgmtTestTargetMap(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    target_meta_ver = models.CharField(max_length=8)
    cat_prop1 = models.CharField(max_length=64)
    cat_prop2 = models.CharField(max_length=64)
    cat_prop3 = models.CharField(max_length=64)
    cat_prop4 = models.CharField(max_length=64)
    cat_prop5 = models.CharField(max_length=64)
    test_type = models.ForeignKey(MgmtTest, models.DO_NOTHING, db_column='test_type')

    class Meta:
        managed = False
        db_table = 'mgmt_test_target_map'
        unique_together = (('target_type', 'target_meta_ver', 'cat_prop1', 'cat_prop2', 'cat_prop3', 'cat_prop4', 'cat_prop5', 'test_type'),)


class MgmtTextIndexStats(models.Model):
    target_guid = models.TextField()  # This field type is a guess.
    collection_timestamp = models.DateField()
    index_name = models.CharField(max_length=400)
    partn_name = models.CharField(max_length=400, blank=True, null=True)
    stat_data = models.CharField(max_length=4000, blank=True, null=True)
    size_data = models.CharField(max_length=4000, blank=True, null=True)
    objects_data = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_text_index_stats'


class MgmtTextindex(models.Model):
    textindex_guid = models.TextField(primary_key=True)  # This field type is a guess.
    target_guid = models.TextField()  # This field type is a guess.
    textindex_name = models.CharField(max_length=200)
    textindex_schema_name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mgmt_textindex'
        unique_together = (('target_guid', 'textindex_name', 'textindex_schema_name'),)


class MgmtTextindexLogsInfo(models.Model):
    textindex_guid = models.ForeignKey(MgmtTextindex, models.DO_NOTHING, db_column='textindex_guid')
    log_directory = models.CharField(max_length=2000, blank=True, null=True)
    log_file = models.CharField(max_length=2000, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    textindex_action_type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_textindex_logs_info'


class MgmtTopoPageBgImage(models.Model):
    topo_page_type = models.CharField(primary_key=True, max_length=64)
    page_instance_id = models.CharField(max_length=128)
    image_name = models.CharField(max_length=128)
    image_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_topo_page_bg_image'
        unique_together = (('topo_page_type', 'page_instance_id'),)


class MgmtTopoPageObjPos(models.Model):
    topo_page_type = models.CharField(primary_key=True, max_length=64)
    page_instance_id = models.CharField(max_length=128)
    node_id = models.CharField(max_length=128)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_topo_page_obj_pos'
        unique_together = (('topo_page_type', 'page_instance_id', 'node_id'),)


class MgmtTopoPagePref(models.Model):
    topo_page_type = models.CharField(primary_key=True, max_length=64)
    page_instance_id = models.CharField(max_length=128)
    preference_name = models.CharField(max_length=128)
    preference_value = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'mgmt_topo_page_pref'
        unique_together = (('topo_page_type', 'page_instance_id', 'preference_name'),)


class MgmtTypeProperties(models.Model):
    target_type = models.CharField(primary_key=True, max_length=64)
    property_name = models.CharField(max_length=64)
    property_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_type_properties'
        unique_together = (('target_type', 'property_name'),)


class MgmtUpdateCollCredsData(models.Model):
    data_set_guid = models.TextField()  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    collection_name = models.CharField(max_length=64, blank=True, null=True)
    credential_set_name = models.CharField(max_length=64)
    credential_column = models.CharField(max_length=32)
    credential_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_coll_creds_data'


class MgmtUpdateCredentialsData(models.Model):
    data_set_guid = models.TextField(primary_key=True)  # This field type is a guess.
    credential_set_name = models.CharField(max_length=64)
    credential_column = models.CharField(max_length=32)
    credential_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_credentials_data'
        unique_together = (('data_set_guid', 'credential_set_name', 'credential_column'),)


class MgmtUpdateOperations(models.Model):
    operation_guid = models.TextField(primary_key=True)  # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    job_owner = models.CharField(max_length=256, blank=True, null=True)
    submission_timestamp = models.DateField()
    last_updated_timestamp = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_operations'


class MgmtUpdateOperationsData(models.Model):
    operation_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_set_guid = models.TextField(primary_key=True)  # This field type is a guess.
    source_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    data_set_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mgmt_update_operations_data'


class MgmtUpdateOperationsDetails(models.Model):
    operation_guid = models.TextField(primary_key=True)  # This field type is a guess.
    destination_target_guid = models.TextField()  # This field type is a guess.
    agent_guid = models.TextField()  # This field type is a guess.
    execution_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    execution_status = models.FloatField(blank=True, null=True)
    last_updated_timestamp = models.DateField(blank=True, null=True)
    error_message = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_operations_details'
        unique_together = (('operation_guid', 'destination_target_guid', 'agent_guid'),)


class MgmtUpdatePdpData(models.Model):
    data_set_guid = models.TextField()  # This field type is a guess.
    setting_name = models.CharField(max_length=64)
    setting_value = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_pdp_data'


class MgmtUpdatePdpDataCopy(models.Model):
    operation_guid = models.TextField()  # This field type is a guess.
    setting_name = models.CharField(max_length=64)
    setting_value = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_pdp_data_copy'


class MgmtUpdatePdpDataMap(models.Model):
    operation_guid = models.TextField()  # This field type is a guess.
    setting_guid = models.TextField()  # This field type is a guess.
    applied_by = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'mgmt_update_pdp_data_map'


class MgmtUpdatePropertiesData(models.Model):
    data_set_guid = models.TextField(primary_key=True)  # This field type is a guess.
    property_name = models.CharField(max_length=64)
    property_type = models.CharField(max_length=64)
    property_value = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_properties_data'
        unique_together = (('data_set_guid', 'property_name', 'property_type'),)


class MgmtUpdateTemplateDataMap(models.Model):
    data_set_guid = models.TextField(primary_key=True)  # This field type is a guess.
    template_copy_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_update_template_data_map'


class MgmtUpdateThresholdsData(models.Model):
    data_set_guid = models.TextField(primary_key=True)  # This field type is a guess.
    metric_guid = models.TextField()  # This field type is a guess.
    coll_name = models.CharField(max_length=64)
    key_value = models.CharField(max_length=256)
    eval_order = models.FloatField(blank=True, null=True)
    num_occurences = models.FloatField(blank=True, null=True)
    fixit_job = models.CharField(max_length=256, blank=True, null=True)
    warning_threshold = models.CharField(max_length=256, blank=True, null=True)
    critical_threshold = models.CharField(max_length=256, blank=True, null=True)
    warning_operator = models.FloatField(blank=True, null=True)
    critical_operator = models.FloatField(blank=True, null=True)
    key_part1_value = models.CharField(max_length=256, blank=True, null=True)
    key_part2_value = models.CharField(max_length=256, blank=True, null=True)
    key_part3_value = models.CharField(max_length=256, blank=True, null=True)
    key_part4_value = models.CharField(max_length=256, blank=True, null=True)
    key_part5_value = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_update_thresholds_data'
        unique_together = (('data_set_guid', 'metric_guid', 'coll_name', 'key_value'),)


class MgmtUrlCache(models.Model):
    url = models.CharField(primary_key=True, max_length=256)
    created_on = models.DateField(blank=True, null=True)
    content_type = models.CharField(max_length=32, blank=True, null=True)
    content_length = models.FloatField(blank=True, null=True)
    content = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_url_cache'


class MgmtUrlProxy(models.Model):
    protocol = models.CharField(primary_key=True, max_length=32)
    host_name = models.CharField(max_length=128)
    port_number = models.FloatField()
    local_host = models.CharField(max_length=128)
    created_on = models.DateField(blank=True, null=True)
    is_default = models.CharField(max_length=32, blank=True, null=True)
    dont_proxy_for = models.CharField(max_length=1024, blank=True, null=True)
    proxy_realm = models.CharField(max_length=256, blank=True, null=True)
    proxy_user = models.CharField(max_length=32, blank=True, null=True)
    proxy_password = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_url_proxy'
        unique_together = (('protocol', 'host_name', 'port_number', 'local_host'),)


class MgmtUserCallbacks(models.Model):
    callback = models.CharField(primary_key=True, max_length=100)
    type = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mgmt_user_callbacks'
        unique_together = (('callback', 'type'),)


class MgmtUserCas(models.Model):
    grantee = models.CharField(primary_key=True, max_length=256)
    job_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_user_cas'
        unique_together = (('grantee', 'job_id'),)


class MgmtUserContext(models.Model):
    client_identifier = models.CharField(primary_key=True, max_length=256)
    attribute = models.FloatField()
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_user_context'
        unique_together = (('client_identifier', 'attribute'),)


class MgmtUserFolders(models.Model):
    user_name = models.CharField(max_length=256)
    folder_name = models.CharField(max_length=256)
    display_order = models.IntegerField(blank=True, null=True)
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_user_folders'


class MgmtUserJobs(models.Model):
    grantee = models.CharField(primary_key=True, max_length=256)
    job_id = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_user_jobs'
        unique_together = (('grantee', 'job_id'),)


class MgmtUserPreferences(models.Model):
    user_name = models.CharField(primary_key=True, max_length=256)
    preference_name = models.CharField(max_length=512)
    preference_value = models.CharField(max_length=4000)
    additional_value = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_user_preferences'
        unique_together = (('user_name', 'preference_name'),)


class MgmtUserReportDefs(models.Model):
    grantee = models.CharField(primary_key=True, max_length=256)
    report_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_user_report_defs'
        unique_together = (('grantee', 'report_guid'),)


class MgmtUserSession(models.Model):
    user_session_id_guid = models.TextField(primary_key=True)  # This field type is a guess.
    user_session_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    em_user = models.CharField(max_length=4000, blank=True, null=True)
    em_user_type = models.CharField(max_length=4000, blank=True, null=True)
    em_user_host_name = models.CharField(max_length=4000, blank=True, null=True)
    oms_host_name = models.CharField(max_length=4000, blank=True, null=True)
    browser_type = models.CharField(max_length=4000, blank=True, null=True)
    login_time = models.DateField(blank=True, null=True)
    logoff_time = models.DateField(blank=True, null=True)
    ip_address = models.CharField(max_length=4000, blank=True, null=True)
    osuser = models.CharField(max_length=4000, blank=True, null=True)
    session_status = models.CharField(max_length=4000, blank=True, null=True)
    session_type = models.CharField(max_length=4000, blank=True, null=True)
    time_zone = models.CharField(max_length=4000, blank=True, null=True)
    ca_name_1 = models.CharField(max_length=256, blank=True, null=True)
    ca_value_1 = models.CharField(max_length=4000, blank=True, null=True)
    ca_name_2 = models.CharField(max_length=256, blank=True, null=True)
    ca_value_2 = models.CharField(max_length=4000, blank=True, null=True)
    ca_name_3 = models.CharField(max_length=256, blank=True, null=True)
    ca_value_3 = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_user_session'


class MgmtUserSubtabColPrefs(models.Model):
    user_name = models.CharField(primary_key=True, max_length=256)
    subtab_name = models.CharField(max_length=64)
    display_order = models.IntegerField()
    column_id_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    column_id = models.CharField(max_length=256, blank=True, null=True)
    column_type = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'mgmt_user_subtab_col_prefs'
        unique_together = (('user_name', 'subtab_name', 'display_order'),)


class MgmtUserTargets(models.Model):
    grantee = models.CharField(primary_key=True, max_length=256)
    target_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_user_targets'
        unique_together = (('grantee', 'target_guid'),)


class MgmtUserTemplates(models.Model):
    grantee = models.CharField(primary_key=True, max_length=256)
    template_guid = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mgmt_user_templates'
        unique_together = (('grantee', 'template_guid'),)


class MgmtVClusterMemberList(models.Model):
    member_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    member_target_type = models.CharField(max_length=255, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_v_cluster_member_list'


class MgmtVClusterRacPolDetail(models.Model):
    composite_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    information_count = models.FloatField(blank=True, null=True)
    warning_count = models.FloatField(blank=True, null=True)
    critical_count = models.FloatField(blank=True, null=True)
    compliance_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_v_cluster_rac_pol_detail'


class MgmtVRacAssocMemberList(models.Model):
    composite_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_type = models.CharField(max_length=255, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_v_rac_assoc_member_list'


class MgmtVRacMemberList(models.Model):
    composite_target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    target_type = models.CharField(max_length=255, blank=True, null=True)
    host_name = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_v_rac_member_list'


class MgmtVersions(models.Model):
    component_name = models.CharField(max_length=32)
    version = models.CharField(max_length=32)
    compat_core_version = models.CharField(max_length=32)
    component_mode = models.CharField(max_length=32, blank=True, null=True)
    status = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_versions'


class MgmtViolationContext(models.Model):
    target_guid = models.TextField(primary_key=True)  # This field type is a guess.
    policy_guid = models.TextField()  # This field type is a guess.
    key_value = models.CharField(max_length=256)
    collection_timestamp = models.DateField()
    column_name = models.CharField(max_length=64)
    column_type = models.FloatField(blank=True, null=True)
    column_value = models.FloatField(blank=True, null=True)
    column_str_value = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgmt_violation_context'
        unique_together = (('target_guid', 'policy_guid', 'key_value', 'collection_timestamp', 'column_name'),)


class Sale(models.Model):
    id = models.BooleanField(primary_key=True)
    time_left = models.IntegerField(blank=True, null=True)
    sold_price = models.IntegerField(blank=True, null=True)
    initial_price = models.IntegerField(blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    done = models.NullBooleanField()
    conclusion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'

class Users(models.Model):
    email = models.CharField(max_length=30, blank=True, null=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=15, blank=True, null=True)
    addresses = models.TextField(blank=True, null=True)  # This field type is a guess.
    phones = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'users'
