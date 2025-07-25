# pylint: disable=pointless-statement
from datetime import datetime, timedelta
from unittest.mock import patch
import pytest
from spark_expectations.core import get_spark_session
from spark_expectations.config.user_config import Constants as user_config
from spark_expectations.core.context import SparkExpectationsContext
from spark_expectations.core.exceptions import SparkExpectationsMiscException
from datetime import datetime, date
import os

spark = get_spark_session()


@patch("spark_expectations.core.context.uuid1")
def test_context_init(mock_uuid):
    # Test that the product_id is set correctly
    mock_uuid.return_value = "hghg-gjgu-jgj"
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    assert context.product_id == "test_product"

    # Test that the run_id is set correctly
    assert context.get_run_id == "test_product_hghg-gjgu-jgj"

    # Test that the run_date is set correctly
    run_date = context.get_run_date
    assert isinstance(datetime.strptime(run_date, "%Y-%m-%d %H:%M:%S"), datetime)


def test_context_properties():
    # Test that the getter properties return the correct values
    context = SparkExpectationsContext(product_id="product1", spark=spark)

    context._run_id = "test_run_id"
    context._run_date = "test_run_date"
    context._dq_stats_table_name = "test_dq_stats_table"
    context._dq_detailed_stats_table_name = "test_dq_stats_table"
    context._final_table_name = "test_final_table"
    context._error_table_name = "test_error_table"

    context._row_dq_rule_type_name = "row_dq_test"
    context._agg_dq_rule_type_name = "agg_dq_test"
    context._source_agg_dq_status = "test_skipped"
    context._row_dq_status = "test_skipped"
    context._final_agg_dq_status = "test_skipped"
    context._dq_run_status = "test_failed"
    context._se_enable_error_table = True
    context._dq_rules_params = {}

    context._dq_project_env_name = "APLAD-5063"
    context._dq_config_file_name = "dq_spark_expectations_config.ini"
    context._dq_config_abs_path = "sparkexpectations/config.ini"
    context._mail_smtp_server = "abc"
    context._mail_smtp_port = 25
    context._mail_smtp_password = "test_password"
    context._smtp_creds_dict = {
        "se.streaming.secret.type": "cerberus",
        "se.streaming.cerberus.url": "https://xyz.com",
        "se.streaming.cerberus.sdb.path": "abc",
        "spark.expectations.notifications.cerberus.smtp.password": "def",
    }
    context._enable_mail = True
    context._enable_smtp_server_auth = True
    context._enable_custom_email_body = True
    context._enable_templated_basic_email_body = True
    context._to_mail = "abc@mail.com, decf@mail.com"
    context._mail_from = "abc@mail.com"
    context._mail_subject = "spark expectations"
    context._email_custom_body = "test email body"
    context._enable_slack = True
    context._slack_webhook_url = "abcedfghi"
    context._enable_teams = True
    context._teams_webhook_url = "abcedfghi"
    context._enable_zoom = True
    context._zoom_webhook_url = "abcedfghi"
    context._zoom_token = "abcedfghi"
    context._table_name = "test_table"
    context._input_count = 100
    context._error_count = 10
    context._output_count = 90
    context._kafka_stats_topic_name = "spark_expectations_stats_topic"
    context._source_agg_dq_result = [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]
    context._final_agg_dq_result = [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]

    context._notification_on_start = True
    context._notification_on_completion = True
    context._enable_agg_dq_detailed_result = True

    context._enable_query_dq_detailed_result = True
    context._notification_on_fail = True
    context._env = "dev"
    context._error_drop_threshold = 100

    context._cerberus_url = "https://xyz"
    context._cerberus_cred_path = "spark-expectations/credentials"
    context._cerberus_token = "xxx"
    # context._kafka_bootstrap_server_url = "https://boostarp/server"
    # context._kafka_secret = "xxxx"
    # context._kafka_token_endpoint_uri = "https://token_uri"
    # context._kafka_client_id = "spark-expectations"

    context._run_id_name = "run_id"
    context._run_date_name = "run_date"
    context._run_date_time_name = "run_date_time"

    context._source_query_dq_status = "Passed"
    context._final_query_dq_status = "Skipped"

    context._debugger_mode = False

    context._supported_df_query_dq = spark.createDataFrame(
        [{"spark_expectations_query_check": "supported_place_holder_dataset_to_run_query_check"}]
    ).collect()

    datetime_now = datetime.now()

    context._source_agg_dq_start_time = datetime_now
    context._final_agg_dq_start_time = datetime_now
    context._source_query_dq_start_time = datetime_now
    context._final_query_dq_start_time = datetime_now
    context._row_dq_start_time = datetime_now
    context._dq_start_time = datetime_now

    context._source_agg_dq_end_time = datetime_now
    context._final_agg_dq_end_time = datetime_now
    context._source_query_dq_end_time = datetime_now
    context._final_query_dq_end_time = datetime_now
    context._row_dq_end_time = datetime_now
    context._dq_end_time = datetime_now

    context._num_row_dq_rules = 1
    context._num_dq_rules = 1
    context._num_agg_dq_rules = {"source_agg_dq": 1, "final_agg_dq": 1}
    context._num_query_dq_rules = {"source_query_dq": 1, "final_query_dq": 1}
    context._summarized_row_dq_res = [
        {"rule": "rule_1", "action_if_failed": "ignore", "failed_row_count": 2},
        {"rule": "rule_2", "action_if_failed": "fail", "failed_row_count": 4},
    ]

    context._kafka_row_dq_res_topic_name = "abc"

    context._se_streaming_stats_dict = {"a": "b", "c": "d"}
    context._se_streaming_stats_topic_name = "test_topic"
    context._stats_dict = [
        {
            "product_id": "test_product_id",
            "table_name": "table1",
        }
    ]

    assert context.get_run_id == "test_run_id"
    assert context.get_run_date == "test_run_date"
    assert context._dq_stats_table_name == "test_dq_stats_table"
    assert context._dq_detailed_stats_table_name == "test_dq_stats_table"
    assert context._final_table_name == "test_final_table"
    assert context._error_table_name == "test_error_table"

    assert context.get_row_dq_rule_type_name == "row_dq_test"
    assert context.get_agg_dq_rule_type_name == "agg_dq_test"
    assert context.get_source_agg_dq_status == "test_skipped"
    assert context.get_row_dq_status == "test_skipped"
    assert context.get_final_agg_dq_status == "test_skipped"
    assert context.get_dq_run_status == "test_failed"
    assert context.get_se_enable_error_table == True

    assert context._dq_project_env_name == "APLAD-5063"
    assert context._dq_config_file_name == "dq_spark_expectations_config.ini"
    assert context._dq_config_abs_path == "sparkexpectations/config.ini"
    assert context._mail_smtp_server == "abc"
    assert context.get_mail_smtp_port == 25
    assert context._mail_smtp_password == "test_password"
    assert context._smtp_creds_dict == {
        "se.streaming.secret.type": "cerberus",
        "se.streaming.cerberus.url": "https://xyz.com",
        "se.streaming.cerberus.sdb.path": "abc",
        "spark.expectations.notifications.cerberus.smtp.password": "def",
    }
    assert context._enable_mail is True
    assert context._enable_smtp_server_auth is True
    assert context._enable_custom_email_body is True
    assert context._enable_templated_basic_email_body is True
    assert context._to_mail == "abc@mail.com, decf@mail.com"
    assert context._mail_from == "abc@mail.com"
    assert context._mail_subject == "spark expectations"
    assert context._email_custom_body == "test email body"
    assert context._enable_slack is True
    assert context._slack_webhook_url == "abcedfghi"
    assert context._enable_teams is True
    assert context._teams_webhook_url == "abcedfghi"
    assert context._enable_zoom is True
    assert context._zoom_webhook_url == "abcedfghi"
    assert context._zoom_token == "abcedfghi"
    assert context._table_name == "test_table"
    assert context._input_count == 100
    assert context._error_count == 10
    assert context._output_count == 90
    assert context._kafka_stats_topic_name == "spark_expectations_stats_topic"
    assert context._source_agg_dq_result == [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]
    assert context._final_agg_dq_result == [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]

    assert context._notification_on_start is True
    assert context._notification_on_completion is True
    assert context._notification_on_fail is True
    assert context._env == "dev"
    assert context._error_drop_threshold == 100

    assert context._cerberus_url == "https://xyz"
    assert context.get_cerberus_url == "https://xyz"
    assert context._cerberus_cred_path == "spark-expectations/credentials"
    assert context.get_cerberus_cred_path == "spark-expectations/credentials"
    assert context._cerberus_token == "xxx"
    assert context.get_cerberus_token == "xxx"
    # assert context._kafka_bootstrap_server_url == "https://boostarp/server"
    # assert context._kafka_secret == "xxxx"
    # assert context._kafka_token_endpoint_uri == "https://token_uri"
    # assert context._kafka_client_id == "spark-expectations"

    assert context._run_id_name == "run_id"
    assert context._run_date_name == "run_date"
    assert context._run_date_time_name == "run_date_time"

    assert (
        context._supported_df_query_dq
        == spark.createDataFrame(
            [{"spark_expectations_query_check": "supported_place_holder_dataset_to_run_query_check"}]
        ).collect()
    )

    assert context._source_agg_dq_start_time == datetime_now
    assert context._final_agg_dq_start_time == datetime_now
    assert context._source_query_dq_start_time == datetime_now
    assert context._final_query_dq_start_time == datetime_now
    assert context._row_dq_start_time == datetime_now
    assert context._dq_start_time == datetime_now

    assert context._source_agg_dq_end_time == datetime_now
    assert context._final_agg_dq_end_time == datetime_now
    assert context._source_query_dq_end_time == datetime_now
    assert context._final_query_dq_end_time == datetime_now
    assert context._row_dq_end_time == datetime_now
    assert context._dq_end_time == datetime_now

    assert context._num_row_dq_rules == 1
    assert context._num_dq_rules == 1
    assert context._num_agg_dq_rules == {"source_agg_dq": 1, "final_agg_dq": 1}
    assert context._num_query_dq_rules == {"source_query_dq": 1, "final_query_dq": 1}
    assert context._summarized_row_dq_res == [
        {"rule": "rule_1", "action_if_failed": "ignore", "failed_row_count": 2},
        {"rule": "rule_2", "action_if_failed": "fail", "failed_row_count": 4},
    ]

    assert context._debugger_mode == False

    assert context._source_query_dq_status == "Passed"
    assert context._final_query_dq_status == "Skipped"
    assert context._kafka_row_dq_res_topic_name == "abc"
    assert context._se_streaming_stats_dict == {"a": "b", "c": "d"}
    assert context._se_streaming_stats_topic_name == "test_topic"
    assert context._stats_dict == [
        {
            "product_id": "test_product_id",
            "table_name": "table1",
        }
    ]


def test_set_dq_stats_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_dq_stats_table_name("dq_stats_table_name")
    assert context._dq_stats_table_name == "dq_stats_table_name"
    assert context.get_dq_stats_table_name == "dq_stats_table_name"


def test_set_final_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_table_name("final_table_name")
    assert context._final_table_name == "final_table_name"
    assert context.get_final_table_name == "final_table_name"


def test_error_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_error_table_name("error_table_name")
    assert context._error_table_name == "error_table_name"
    assert context.get_error_table_name == "error_table_name"


def test_row_dq_rule_type_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._row_dq_rule_type_name = "row_dq1"
    context.get_row_dq_rule_type_name == "row_dq1"


def test_agg_dq_rule_type_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._agg_dq_rule_type_name = "row_dq1"
    context.get_agg_dq_rule_type_name == "row_dq1"


def test_set_source_agg_dq_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_source_agg_dq_status("Passed")
    assert context._source_agg_dq_status == "Passed"
    assert context.get_source_agg_dq_status == "Passed"


def test_set_row_dq_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_row_dq_status("Failed")
    assert context._row_dq_status == "Failed"
    assert context.get_row_dq_status == "Failed"


def test_set_final_agg_dq_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_agg_dq_status("Skipped")
    assert context._final_agg_dq_status == "Skipped"
    assert context.get_final_agg_dq_status == "Skipped"


def test_set_dq_run_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_dq_run_status("Passed")
    assert context._dq_run_status == "Passed"
    assert context.get_dq_run_status == "Passed"


def test_get_source_agg_dq_status_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._source_agg_dq_status = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_source_agg_dq_status' before \n            accessing it",
    ):
        context.get_source_agg_dq_status


def test_get_row_dq_status_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._row_dq_status = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_row_dq_status' before \n            accessing it",
    ):
        context.get_row_dq_status


def test_get_final_agg_dq_status_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._final_agg_dq_status = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_final_agg_dq_status' before \n            accessing it",
    ):
        context.get_final_agg_dq_status


def test_get_dq_run_status_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._dq_run_status = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_dq_run_status' before \n            accessing it",
    ):
        context.get_dq_run_status


def test_get_row_dq_rule_type_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._row_dq_rule_type_name = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_row_dq_rule_type_name' before \n            accessing it",
    ):
        context.get_row_dq_rule_type_name


def test_get_agg_dq_rule_type_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._agg_dq_rule_type_name = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_agg_dq_rule_type_name' before \n            accessing it",
    ):
        context.get_agg_dq_rule_type_name


def test_set_source_query_dq_result():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    value = [{"1": "2"}]
    context.set_source_query_dq_result(value)
    context.get_source_query_dq_result == value


def test_set_final_query_dq_result():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    value = [{"1": "2"}]
    context.set_final_query_dq_result(value)
    context.get_final_query_dq_result == value


def test_get_query_dq_rule_type_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    values = [None, "query_dq"]
    for value in values:
        context._query_dq_rule_type_name = value
        if value is None:
            with pytest.raises(
                SparkExpectationsMiscException,
                match="The spark expectations context is not set completely, please assign "
                "'_query_dq_rule_type_name' before \n            accessing it",
            ):
                context.get_query_dq_rule_type_name
        else:
            context.get_query_dq_rule_type_name == value


def test_get_dq_stats_table_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_dq_stats_table_name' before \n            accessing it",
    ):
        context.get_dq_stats_table_name


def test_get_final_table_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_final_table_name' before \n            accessing it",
    ):
        context.get_final_table_name


def test_get_error_table_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_error_table_name' before \n            accessing it",
    ):
        context.get_error_table_name


def test_get_config_file_path():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._dq_config_abs_path = "spark_expectations/config/file"

    assert context.get_config_file_path == "spark_expectations/config/file"


def test_get_config_file_path_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._dq_config_abs_path = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_dq_config_abs_path' before
            accessing it""",
    ):
        context.get_config_file_path


def test_set_enable_mail():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_enable_mail(True)
    assert context._enable_mail is True
    assert context.get_enable_mail is True


def test_set_enable_smtp_server_auth():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_enable_smtp_server_auth(True)
    assert context._enable_smtp_server_auth is True
    assert context.get_enable_smtp_server_auth is True


def test_set_enable_custom_email_body():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_enable_custom_email_body(True)
    assert context._enable_custom_email_body is True
    assert context.get_enable_custom_email_body is True


def test_set_enable_templated_basic_email_body():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_enable_templated_basic_email_body(True)
    assert context._enable_templated_basic_email_body is True
    assert context.get_enable_templated_basic_email_body is True


def test_set_smtp_server():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_mail_smtp_server("abc")
    assert context._mail_smtp_server == "abc"
    assert context.get_mail_smtp_server == "abc"


def test_set_smtp_port():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_mail_smtp_port(25)
    context.set_mail_smtp_port(context._mail_smtp_port)
    assert context._mail_smtp_port == 25
    assert context.get_mail_smtp_port == 25


def test_set_mail_smtp_password():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_mail_smtp_password("test_password")
    assert context._mail_smtp_password == "test_password"
    assert context.get_mail_smtp_password == "test_password"


def test_set_smtp_creds_dict():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_smtp_creds_dict(
        {
            "se.streaming.secret.type": "cerberus",
            "se.streaming.cerberus.url": "https://xyz.com",
            "se.streaming.cerberus.sdb.path": "abc",
            "spark.expectations.notifications.cerberus.smtp.password": "def",
        }
    )
    assert context._smtp_creds_dict == {
        "se.streaming.secret.type": "cerberus",
        "se.streaming.cerberus.url": "https://xyz.com",
        "se.streaming.cerberus.sdb.path": "abc",
        "spark.expectations.notifications.cerberus.smtp.password": "def",
    }
    assert context.get_smtp_creds_dict == {
        "se.streaming.secret.type": "cerberus",
        "se.streaming.cerberus.url": "https://xyz.com",
        "se.streaming.cerberus.sdb.path": "abc",
        "spark.expectations.notifications.cerberus.smtp.password": "def",
    }


def test_set_to_mail():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_to_mail("abc@mail.com, def@mail.com")
    assert context._to_mail == "abc@mail.com, def@mail.com"
    assert context.get_to_mail == "abc@mail.com, def@mail.com"


def test_set_mail_from():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_mail_from("abc@mail.com")
    assert context._mail_from == "abc@mail.com"
    assert context.get_mail_from == "abc@mail.com"


def test_set_mail_subject():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_mail_subject("spark expectations")
    assert context._mail_subject == "spark expectations"
    assert context.get_mail_subject == "spark expectations"


def test_set_email_custom_body():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_email_custom_body("test email custom body")
    assert context._email_custom_body == "test email custom body"
    assert context.get_email_custom_body == "test email custom body"


def test_get_email_custom_body_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._email_custom_body = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_email_custom_body' before 
            accessing it""",
    ):
        context.get_email_custom_body


def test_set_enable_slack():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_enable_slack(True)
    assert context._enable_slack is True
    assert context.get_enable_slack is True


def test_set_slack_webhook_url():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_slack_webhook_url("abcdefghi")
    assert context._slack_webhook_url == "abcdefghi"
    assert context.get_slack_webhook_url == "abcdefghi"


def test_set_enable_teams():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_enable_teams(True)
    assert context._enable_teams is True
    assert context.get_enable_teams is True


def test_set_teams_webhook_url():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_teams_webhook_url("abcdefghi")
    assert context._teams_webhook_url == "abcdefghi"
    assert context.get_teams_webhook_url == "abcdefghi"


def test_set_enable_zoom():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_enable_zoom(True)
    assert context._enable_zoom is True
    assert context.get_enable_zoom is True


def test_set_zoom_webhook_url():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_zoom_webhook_url("abcdefghi")
    assert context._zoom_webhook_url == "abcdefghi"
    assert context.get_zoom_webhook_url == "abcdefghi"


def test_set_zoom_token():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_zoom_token("abcdefghi")
    assert context._zoom_token == "abcdefghi"
    assert context.get_zoom_token == "abcdefghi"


def test_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_table_name("test_table")
    assert context._table_name == "test_table"
    assert context._table_name == "test_table"
    assert context.get_table_name == "test_table"


def test_set_input_count():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_input_count(100)
    assert context._input_count == 100
    assert context._input_count == 100
    assert context.get_input_count == 100


def test_set_error_count():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_error_count(10)
    assert context._error_count == 10
    assert context.get_error_count == 10


def test_set_output_count():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_output_count(90)
    assert context._output_count == 90
    assert context.get_output_count == 90


# def test_set_kafka_stats_topic_name():
#     context = SparkExpectationsContext(product_id="product1")
#     context.set_kafka_stats_topic_name("spark_expectations_stats_topic")
#     assert context._kafka_stats_topic_name == "spark_expectations_stats_topic"
#     assert context.get_kafka_stats_topic_name == "spark_expectations_stats_topic"


def test_set_kafka_source_agg_dq_result():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_source_agg_dq_result(
        [
            {
                "action_if_failed": "ignore",
                "rule_type": "agg_dq",
                "rule_name": "sum_of_salary_threshold",
                "rule": "sum(salary)>100",
            }
        ]
    )
    assert context._source_agg_dq_result == [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]
    assert context.get_source_agg_dq_result == [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]


def test_set_kafka_final_agg_dq_result():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_agg_dq_result(
        [
            {
                "action_if_failed": "ignore",
                "rule_type": "agg_dq",
                "rule_name": "sum_of_salary_threshold",
                "rule": "sum(salary)>100",
            }
        ]
    )
    assert context._final_agg_dq_result == [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]
    assert context.get_final_agg_dq_result == [
        {
            "action_if_failed": "ignore",
            "rule_type": "agg_dq",
            "rule_name": "sum_of_salary_threshold",
            "rule": "sum(salary)>100",
        }
    ]


def test_get_mail_smtp_server_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._mail_smtp_server = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_mail_smtp_server' before \n            accessing it",
    ):
        context.get_mail_smtp_server


def test_get_mail_smtp_port_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._mail_smtp_port = 0
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_mail_smtp_port' before \n            accessing it",
    ):
        context.get_mail_smtp_port


def test_get_mail_smtp_password_none():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._mail_smtp_password = None
    assert context.get_mail_smtp_password is None


def test_get_to_mail_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._to_mail = False
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_to_mail' before \n            accessing it",
    ):
        context.get_to_mail


def test_get_mail_subject_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._to_mail = False
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_mail_subject' before \n            accessing it",
    ):
        context.get_mail_subject


def test_get_mail_from_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._mail_from = False
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_mail_from' before \n            accessing it",
    ):
        context.get_mail_from


def test_get_slack_webhook_url_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._slack_webhook_url = False
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_slack_webhook_url' before \n            accessing it",
    ):
        context.get_slack_webhook_url


def test_get_teams_webhook_url_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._teams_webhook_url = False
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_teams_webhook_url' before \n            accessing it",
    ):
        context.get_teams_webhook_url


def test_get_zoom_webhook_url_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._zoom_webhook_url = False
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_zoom_webhook_url' before \n            accessing it",
    ):
        context.get_zoom_webhook_url


def test_get_zoom_token():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._zoom_token = False
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_zoom_token' before \n            accessing it",
    ):
        context.get_zoom_token


def test_get_table_name_expection():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._table_name = ""
    with pytest.raises(
        SparkExpectationsMiscException,
        match="The spark expectations context is not set completely, please assign "
        "'_table_name' before \n            accessing it",
    ):
        context.get_table_name


# def test_get_input_count():
#     context = SparkExpectationsContext(product_id="product1")
#     context._input_count = 0
#     with pytest.raises(SparkExpectationsMiscException,
#                        match="The spark expectations context is not set completely, please assign "
#                              "'_input_count' before \n            accessing it"):
#         context.get_input_count


# def test_get_kafka_stats_topic_name_exception():
#     context = SparkExpectationsContext(product_id="product1")
#     context._kafka_stats_topic_name = None
#     with pytest.raises(SparkExpectationsMiscException,
#                        match="The spark expectations context is not set completely, please assign "
#                              "'_kafka_stats_topic_name' before \n            accessing it"):
#         context.get_kafka_stats_topic_name


def test_set_notification_on_start():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_notification_on_start(True)
    assert context._notification_on_start is True
    assert context.get_notification_on_start is True


def test_set_notification_on_completion():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_notification_on_completion(True)
    assert context._notification_on_completion is True
    assert context.get_notification_on_completion is True


def test_set_notification_on_fail():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_notification_on_fail(True)
    assert context._notification_on_fail is True
    assert context.get_notification_on_fail is True


def test_set_env():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._table_name = "dq_spark_staging.test_table"
    context.set_env("staging")
    assert context.get_env == "staging"


def test_get_env():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._env = "dev1"
    assert context.get_env == "dev1"


def test_get_error_percentage():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 100
    context._error_count = 50

    assert context.get_error_percentage == 50.0


def test_get_output_percentage():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 100
    context._output_count = 50

    assert context.get_output_percentage == 50.0


def test_get_success_percentage():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 100
    context._output_count = 50
    context._error_count = 25

    assert context.get_success_percentage == 75.0


def test_get_error_drop_percentage():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 100
    context._output_count = 50
    context._error_count = 25

    assert context.get_error_drop_percentage == 50.0


def test_set_error_threshold():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_error_drop_threshold(100)
    assert context._error_drop_threshold == 100
    assert context.get_error_drop_threshold == 100


def test_get_error_threshold():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._error_drop_threshold = 0
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_error_drop_threshold'  before 
            accessing it""",
    ):
        context.get_error_drop_threshold


def test_get_cerberus_url_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._cerberus_url = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_cerberus_url'  before 
            accessing it""",
    ):
        context.get_cerberus_url


def test_get_cerberus_cred_path_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._cerberus_cred_path = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_cerberus_cred_path'  before 
            accessing it""",
    ):
        context.get_cerberus_cred_path


def test_get_cerberus_token_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._cerberus_token = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_cerberus_token'  before 
            accessing it""",
    ):
        context.get_cerberus_token


# def test_get_kafka_bootstrap_server_url_exception():
#     context = SparkExpectationsContext(product_id="product1")
#     context._kafka_bootstrap_server_url = None
#     with pytest.raises(SparkExpectationsMiscException,
#                        match="""The spark expectations context is not set completely, please assign '_kafka_bootstrap_server_url'  before
#             accessing it"""):
#         context.get_kafka_bootstrap_server_url


# def test_get_kafka_secret_exception():
#     context = SparkExpectationsContext(product_id="product1")
#     context._kafka_secret = None
#     with pytest.raises(SparkExpectationsMiscException,
#                        match="""The spark expectations context is not set completely, please assign '_kafka_secret'  before
#             accessing it"""):
#         context.get_kafka_secret


# def test_get_kafka_token_endpoint_uri_exception():
#     context = SparkExpectationsContext(product_id="product1")
#     context._kafka_token_endpoint_uri = None
#     with pytest.raises(SparkExpectationsMiscException,
#                        match="""The spark expectations context is not set completely, please assign '_kafka_token_endpoint_uri'  before
#             accessing it"""):
#         context.get_kafka_token_endpoint_uri


# def test_get_kafka_client_id_exception():
#     context = SparkExpectationsContext(product_id="product1")
#     context._kafka_client_id = None
#     with pytest.raises(SparkExpectationsMiscException,
#                        match="""The spark expectations context is not set completely, please assign '_kafka_client_id'  before
#             accessing it"""):
#         context.get_kafka_client_id


# def test_set_kafka_bootstrap_server_url():
#     context = SparkExpectationsContext(product_id="product1")
#     context.set_kafka_bootstrap_server_url(kafka_bootstrap_server_url="https://boostarp/server")
#     assert context._kafka_bootstrap_server_url == "https://boostarp/server"
#     assert context.get_kafka_bootstrap_server_url == "https://boostarp/server"


# def test_kafka_secret():
#     context = SparkExpectationsContext(product_id="product1")
#     context.set_kafka_secret(kafka_secret="xxx")
#     assert context._kafka_secret == "xxx"
#     assert context.get_kafka_secret == "xxx"


# def test_kafka_token_endpoint_uri():
#     context = SparkExpectationsContext(product_id="product1")
#     context.set_kafka_token_endpoint_uri(kafka_token_endpoint_uri="https://token_uri")
#     assert context._kafka_token_endpoint_uri == "https://token_uri"
#     assert context.get_kafka_token_endpoint_uri == "https://token_uri"


# def test_set_kafka_client_id():
#     context = SparkExpectationsContext(product_id="product1")
#     context.set_kafka_client_id(kafka_client_id="spark-expectations")
#     assert context._kafka_client_id == "spark-expectations"
#     assert context.get_kafka_client_id == "spark-expectations"


def test_set_source_agg_dq_start_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_source_agg_dq_start_time()
    assert isinstance(context._source_agg_dq_start_time, datetime)


def test_set_source_agg_dq_end_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_source_agg_dq_end_time()
    assert isinstance(context._source_agg_dq_end_time, datetime)


def test_set_final_agg_dq_start_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_agg_dq_start_time()
    assert isinstance(context._final_agg_dq_start_time, datetime)


def test_set_final_agg_dq_end_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_agg_dq_end_time()
    assert isinstance(context._final_agg_dq_end_time, datetime)


def test_set_source_query_dq_start_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_source_query_dq_start_time()
    assert isinstance(context._source_query_dq_start_time, datetime)


def test_set_source_query_dq_end_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_source_query_dq_end_time()
    assert isinstance(context._source_query_dq_end_time, datetime)


def test_set_final_query_dq_start_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_query_dq_start_time()
    assert isinstance(context._final_query_dq_start_time, datetime)


def test_set_final_query_dq_end_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_query_dq_end_time()
    assert isinstance(context._final_query_dq_end_time, datetime)


def test_set_row_dq_start_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_row_dq_start_time()
    assert isinstance(context._row_dq_start_time, datetime)


def test_set_row_dq_end_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_row_dq_end_time()
    assert isinstance(context._row_dq_end_time, datetime)


def test_set_dq_start_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_dq_start_time()
    assert isinstance(context._dq_start_time, datetime)


def test_set_dq_end_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_dq_end_time()
    assert isinstance(context._dq_end_time, datetime)


def test_get_time_diff():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    assert context.get_time_diff(None, None) == 0.0
    now = datetime.now()
    assert context.get_time_diff(now, now + timedelta(seconds=2)) == 2.0


def test_get_source_agg_dq_run_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    now = datetime.now()
    context._source_agg_dq_start_time = now
    context._source_agg_dq_end_time = now + timedelta(seconds=2)
    assert context.get_source_agg_dq_run_time == 2.0


def test_get_final_agg_dq_run_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    now = datetime.now()
    context._final_agg_dq_start_time = now
    context._final_agg_dq_end_time = now + timedelta(seconds=2)
    assert context.get_final_agg_dq_run_time == 2.0


def test_get_source_query_dq_run_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    now = datetime.now()
    context._source_query_dq_start_time = now
    context._source_query_dq_end_time = now + timedelta(seconds=2)
    assert context.get_source_query_dq_run_time == 2.0


def test_get_final_query_dq_run_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    now = datetime.now()
    context._final_query_dq_start_time = now
    context._final_query_dq_end_time = now + timedelta(seconds=2)
    assert context.get_final_query_dq_run_time == 2.0


def test_get_row_dq_run_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    now = datetime.now()
    context._row_dq_start_time = now
    context._row_dq_end_time = now + timedelta(seconds=2)
    assert context.get_row_dq_run_time == 2.0


def test_get_dq_run_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    now = datetime.now()
    context._dq_start_time = now
    context._dq_end_time = now + timedelta(seconds=2)
    assert context.get_dq_run_time == 2.0


def test_get_dbr_version():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    os.environ["DATABRICKS_RUNTIME_VERSION"] = "13"
    assert context.get_dbr_version == 13

    os.environ["DATABRICKS_RUNTIME_VERSION"] = "13.3"
    assert context.get_dbr_version == 13.3

    # Remove the mock to test non-Databricks environment
    del os.environ["DATABRICKS_RUNTIME_VERSION"]
    assert context.get_dbr_version == None


def test_get_run_id_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    values = [None, "test"]
    for value in values:
        context._run_id_name = value
        if not value:
            with pytest.raises(
                SparkExpectationsMiscException,
                match="""The spark expectations context is not set completely, please assign '_run_id_name'  .*""",
            ):
                context.get_run_id_name
        else:
            context.get_run_id_name == value


def test_get_run_date_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    values = [None, "test"]
    for value in values:
        context._run_date_name = value
        if not value:
            with pytest.raises(
                SparkExpectationsMiscException,
                match="""The spark expectations context is not set completely, please assign '_run_date_name'  .*""",
            ):
                context.get_run_date_name
        else:
            context.get_run_date_name == value


def test_get_run_date_time_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    values = [None, "test"]
    for value in values:
        context._run_date_time_name = value
        if not value:
            with pytest.raises(
                SparkExpectationsMiscException,
                match="""The spark expectations context is not set completely, please assign '_run_date_time_name'  .*""",
            ):
                context.get_run_date_time_name
        else:
            context.get_run_date_time_name == value


def test_set_num_row_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_num_row_dq_rules()
    assert context._num_row_dq_rules == 1
    assert context._num_dq_rules == 1


def test_set_num_agg_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_num_agg_dq_rules(True, True)
    assert context.get_num_agg_dq_rules == {
        "num_source_agg_dq_rules": 1,
        "num_final_agg_dq_rules": 1,
        "num_agg_dq_rules": 1,
    }


def test_set_num_query_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_num_query_dq_rules(True, True)
    assert context.get_num_query_dq_rules == {
        "num_source_query_dq_rules": 1,
        "num_final_query_dq_rules": 1,
        "num_query_dq_rules": 1,
    }


def test_get_num_row_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_num_row_dq_rules'  .*""",
    ):
        context._num_row_dq_rules = None
        context.get_num_row_dq_rules

    context._num_row_dq_rules = 0
    context.set_num_row_dq_rules()
    context.get_num_row_dq_rules == 1


def test_get_num_agg_dq_rules_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._num_agg_dq_rules = [1, 2, 3, 4]
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_num_agg_dq_rules'  before 
            accessing it""",
    ):
        context.get_num_agg_dq_rules


def test_get_num_query_dq_rules_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._num_query_dq_rules = [1, 2, 3, 4]
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_num_query_dq_rules'  before 
            accessing it""",
    ):
        context.get_num_query_dq_rules


def test_get_num_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_num_dq_rules'  .*""",
    ):
        context._num_dq_rules = None
        context.get_num_dq_rules

    context.reset_num_dq_rules()
    context.get_num_dq_rules == 0


def test_set_summarized_row_dq_res():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_summarized_row_dq_res(
        [
            {"rule": "rule_1", "action_if_failed": "ignore", "failed_row_count": 2},
            {"rule": "rule_2", "action_if_failed": "fail", "failed_row_count": 4},
        ]
    )

    assert context.get_summarized_row_dq_res == [
        {"rule": "rule_1", "action_if_failed": "ignore", "failed_row_count": 2},
        {"rule": "rule_2", "action_if_failed": "fail", "failed_row_count": 4},
    ]


def test_set_target_and_error_table_writer_config():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_target_and_error_table_writer_config({"format": "bigquery"})

    assert context.get_target_and_error_table_writer_config == {"format": "bigquery"}


def test_set_stats_table_writer_config():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_stats_table_writer_config({"format": "bigquery"})

    assert context.get_stats_table_writer_config == {"format": "bigquery"}


# def test_set_kafka_row_dq_res_topic_name():
#     context = SparkExpectationsContext(product_id="product1")
#     context.set_kafka_row_dq_res_topic_name("abc")
#     assert context.get_kafka_row_dq_res_topic_name == "abc"
#
# def test_get_kafka_row_dq_res_topic_name_exception():
#     context = SparkExpectationsContext(product_id="product1")
#     context._kafka_row_dq_res_topic_name = None
#     with pytest.raises(SparkExpectationsMiscException,
#                        match= """The spark expectations context is not set completely, please assign '_kafka_row_dq_res_topic_name' before
#             accessing it"""):
#         context.get_kafka_row_dq_res_topic_name


def test_set_source_query_dq_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_source_query_dq_status("Passed")
    assert context.get_source_query_dq_status == "Passed"


def test_set_final_query_dq_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_final_query_dq_status("Passed")
    assert context.get_final_query_dq_status == "Passed"


def test_get_source_query_dq_status_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._source_query_dq_status = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_source_query_dq_status' before 
            accessing it""",
    ):
        context.get_source_query_dq_status


def test_get_final_query_dq_status_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._final_query_dq_status = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_final_query_dq_status' before 
            accessing it""",
    ):
        context.get_final_query_dq_status


def test_set_supported_df_query_dq():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._supported_df_query_dq = context.set_supported_df_query_dq()
    assert (
        context.get_supported_df_query_dq.collect()
        == get_spark_session()
        .createDataFrame([{"spark_expectations_query_check": "supported_place_holder_dataset_to_run_query_check"}])
        .collect()
    )


def test_get_supported_df_query_dq():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._supported_df_query_dq = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_supported_df_query_dq'  before 
            accessing it""",
    ):
        context.get_supported_df_query_dq


def test_set_debugger_mode():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_debugger_mode(True)
    assert context._debugger_mode == True


def test_get_debugger_mode():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_debugger_mode(True)
    assert context.get_debugger_mode == True


def test_print_dataframe_with_debugger():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_debugger_mode(True)
    context.print_dataframe_with_debugger(context.set_supported_df_query_dq())


def test_get_error_percentage_negative():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 0
    assert context.get_error_percentage == 0.0


def test_get_error_percentage_negative():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 0
    assert context.get_error_percentage == 0.0


def test_get_output_percentage_negative():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 0
    assert context.get_output_percentage == 0.0


def test_get_success_percentage_negative():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 0
    assert context.get_success_percentage == 0.0


def test_get_error_drop_percentage_negative():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._input_count = 0
    assert context.get_error_drop_percentage == 0.0


def test_reset_num_row_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.reset_num_row_dq_rules()
    assert context._num_row_dq_rules == 0


def test_reset_num_row_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.reset_num_agg_dq_rules()
    assert context._num_agg_dq_rules == {
        "num_agg_dq_rules": 0,
        "num_source_agg_dq_rules": 0,
        "num_final_agg_dq_rules": 0,
    }


def test_reset_num_query_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.reset_num_query_dq_rules()
    assert context._num_query_dq_rules == {
        "num_query_dq_rules": 0,
        "num_source_query_dq_rules": 0,
        "num_final_query_dq_rules": 0,
    }


def test_set_end_time_when_dq_job_fails():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    attributes = ["source_agg", "source_query", "row", "final_agg", "final_query"]
    for attribute in attributes:
        setattr(context, f"_{attribute}_dq_start_time", datetime.now())
        setattr(context, f"_{attribute}_dq_end_time", None)
        context.set_end_time_when_dq_job_fails()
        datetime_actual = getattr(context, f"_{attribute}_dq_end_time")
        datetime_actual.date == date.today()


def test_reset_num_dq_rules():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.reset_num_dq_rules()
    assert context._num_dq_rules == 0


def test_set_se_streaming_stats_dict():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({"a": "b", "c": "d"})

    assert context.get_se_streaming_stats_dict == {"a": "b", "c": "d"}


def get_set_se_streaming_stats_dict():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({"a": "b", "c": "d"})

    assert context.get_se_streaming_stats_dict == context._se_streaming_stats_dict


def test_set_stats_dict():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    data = [("test_product_id", "test_schema.table1", 5)]
    columns = ["product_id", "table_name", "error_count"]
    df = spark.createDataFrame(data, columns)
    context.set_stats_dict(df)

    assert context._stats_dict == [
        {
            "product_id": "test_product_id",
            "table_name": "test_schema.table1",
            "error_count": 5,
        }
    ]

    assert context.get_stats_dict == [
        {
            "product_id": "test_product_id",
            "table_name": "test_schema.table1",
            "error_count": 5,
        }
    ]


def test_get_secret_type():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.secret_type: "a"})

    assert context.get_secret_type == "a"


def test_get_secret_type_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.se_enable_streaming: "a"})

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign 
            'UserConfig.secret_type' before 
            accessing it""",
    ):
        context.get_secret_type


def test_get_server_url_key():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_kafka_server_url: "b", user_config.secret_type: "databricks"})

    assert context.get_server_url_key == "b"

    context.set_se_streaming_stats_dict(
        {
            user_config.dbx_kafka_server_url: "b",
            user_config.cbs_kafka_server_url: "c",
            user_config.secret_type: "cerberus",
        }
    )
    assert context.get_server_url_key == "c"


def test_get_server_url_key_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_kafka_server_url: "b", user_config.secret_type: "cerberus"})

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign
            'UserConfig.cbs_kafka_server_url' before
            accessing it""",
    ):
        context.get_server_url_key


def test_get_token_endpoint_url():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_secret_token_url: "d", user_config.secret_type: "databricks"})

    assert context.get_token_endpoint_url == "d"

    context.set_se_streaming_stats_dict(
        {
            user_config.dbx_secret_token_url: "d",
            user_config.cbs_secret_token_url: "f",
            user_config.secret_type: "cerberus",
        }
    )
    assert context.get_token_endpoint_url == "f"


def test_get_token_endpoint_url_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_secret_token_url: "d", user_config.secret_type: "cerberus"})

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign
            'UserConfig.cbs_secret_token_url' before
            accessing it""",
    ):
        context.get_token_endpoint_url


def test_get_token():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_secret_token: "g", user_config.secret_type: "databricks"})

    assert context.get_token == "g"

    context.set_se_streaming_stats_dict(
        {
            user_config.dbx_secret_token: "g",
            user_config.cbs_secret_token: "h",
            user_config.secret_type: "cerberus",
        }
    )
    assert context.get_token == "h"


def test_get_token_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_secret_token_url: "g", user_config.secret_type: "cerberus"})

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign
            'UserConfig.cbs_secret_token' before
            accessing it""",
    ):
        context.get_token


def test_get_client_id():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_secret_app_name: "i", user_config.secret_type: "databricks"})

    assert context.get_client_id == "i"

    context.set_se_streaming_stats_dict(
        {
            user_config.dbx_secret_app_name: "i",
            user_config.cbs_secret_app_name: "j",
            user_config.secret_type: "cerberus",
        }
    )
    assert context.get_client_id == "j"


def test_get_client_id_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_secret_app_name: "g", user_config.secret_type: "cerberus"})

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign
            'UserConfig.cbs_secret_app_name' before
            accessing it""",
    ):
        context.get_client_id


def test_get_topic_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_topic_name: "k", user_config.secret_type: "databricks"})

    assert context.get_topic_name == "k"

    context.set_se_streaming_stats_dict(
        {
            user_config.dbx_topic_name: "k",
            user_config.cbs_topic_name: "l",
            user_config.secret_type: "cerberus",
        }
    )
    assert context.get_topic_name == "l"


def test_get_topic_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_dict({user_config.dbx_topic_name: "k", user_config.secret_type: "cerberus"})

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign 
            'UserConfig.cbs_topic_name' before 
            accessing it""",
    ):
        context.get_topic_name


def test_set_se_streaming_stats_topic_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_topic_name("test_topic")

    assert context.get_se_streaming_stats_topic_name == "test_topic"


def test_get_se_streaming_stats_topic_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_topic_name("test_topic")

    assert context.get_se_streaming_stats_topic_name == context.get_se_streaming_stats_topic_name


def test_get_se_streaming_stats_topic_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_se_streaming_stats_topic_name("")

    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign 
            '_se_streaming_stats_topic_name' before 
            accessing it""",
    ):
        context.get_se_streaming_stats_topic_name


def test_set_rules_exceeds_threshold():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_rules_exceeds_threshold(
        [
            {
                "rule_name": "rule_1",
                "action_if_failed": "ignore",
                "description": "description1",
                "rule_type": "row_dq",
                "error_drop_threshold": "10",
                "error_drop_percentage": "10.0",
            }
        ]
    )
    assert context.get_rules_exceeds_threshold == [
        {
            "rule_name": "rule_1",
            "action_if_failed": "ignore",
            "description": "description1",
            "rule_type": "row_dq",
            "error_drop_threshold": "10",
            "error_drop_percentage": "10.0",
        }
    ]


def test_get_rules_exceds_threshold():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._rules_error_per = [
        {
            "rule_name": "rule_1",
            "action_if_failed": "ignore",
            "description": "description1",
            "rule_type": "row_dq",
            "error_drop_threshold": "10",
            "error_drop_percentage": "10.0",
        }
    ]

    assert context.get_rules_exceeds_threshold == [
        {
            "rule_name": "rule_1",
            "action_if_failed": "ignore",
            "description": "description1",
            "rule_type": "row_dq",
            "error_drop_threshold": "10",
            "error_drop_percentage": "10.0",
        }
    ]


def test_set_agg_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_agg_dq_detailed_stats_status(True)
    assert context.get_agg_dq_detailed_stats_status is True


def test_get_agg_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    assert context.get_agg_dq_detailed_stats_status is True


def test_set_query_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    assert context.get_query_dq_detailed_stats_status is True


def test_get_query_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    assert context.get_query_dq_detailed_stats_status is False


def test_set_target_agg_dq_detailed_stats():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    target_agg_dq_detailed_stats = [
        ("column1", "rule1"),
        ("column2", "rule2"),
        ("column3", "rule3"),
    ]
    context.set_target_agg_dq_detailed_stats(target_agg_dq_detailed_stats)
    assert context.get_target_agg_dq_detailed_stats == target_agg_dq_detailed_stats


def test_set_target_query_dq_detailed_stats():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    target_query_dq_detailed_stats = [
        ("column1", "rule1"),
        ("column2", "rule2"),
        ("column3", "rule3"),
    ]
    context.set_target_query_dq_detailed_stats(target_query_dq_detailed_stats)
    assert context.get_target_query_dq_detailed_stats == target_query_dq_detailed_stats


def test_set_source_agg_dq_detailed_stats():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    source_agg_dq_detailed_stats = [
        ("column1", "rule1"),
        ("column2", "rule2"),
        ("column3", "rule3"),
    ]
    context.set_source_agg_dq_detailed_stats(source_agg_dq_detailed_stats)
    assert context.get_source_agg_dq_detailed_stats == source_agg_dq_detailed_stats


def test_set_source_query_dq_detailed_stats():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    source_query_dq_detailed_stats = [
        ("column1", "rule1"),
        ("column2", "rule2"),
        ("column3", "rule3"),
    ]
    context.set_source_query_dq_detailed_stats(source_query_dq_detailed_stats)
    assert context.get_source_query_dq_detailed_stats == source_query_dq_detailed_stats


def test_set_detailed_stats_table_writer_config():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    config = {"key": "value"}
    context.set_detailed_stats_table_writer_config(config)
    assert context.get_detailed_stats_table_writer_config() == config


# Add more test cases as needed
def test_set_agg_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_agg_dq_detailed_stats_status(True)
    assert context.get_agg_dq_detailed_stats_status is True


def test_get_agg_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_agg_dq_detailed_stats_status(True)
    assert context.get_agg_dq_detailed_stats_status is True


def test_set_query_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    assert context.get_query_dq_detailed_stats_status is True


def test_get_query_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    assert context.get_query_dq_detailed_stats_status is True


def test_set_agg_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_agg_dq_detailed_stats_status(True)
    assert context.get_agg_dq_detailed_stats_status is True


def test_set_query_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    assert context.get_query_dq_detailed_stats_status is True


def test_set_dq_stats_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_dq_stats_table_name("dq_stats_table_name")
    assert context._dq_stats_table_name == "dq_stats_table_name"
    assert context.get_dq_stats_table_name == "dq_stats_table_name"


def test_set_dq_detailed_stats_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_dq_detailed_stats_table_name("dq_stats_table_name")

    context._enable_agg_dq_detailed_result = True
    context._enable_query_dq_detailed_result = True

    assert context.get_agg_dq_detailed_stats_status is True
    assert context.get_query_dq_detailed_stats_status is True

    assert context._dq_detailed_stats_table_name == "dq_stats_table_name"
    assert context.get_dq_detailed_stats_table_name == "dq_stats_table_name"


def test_set_detailed_stats_table_writer_config():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    config = {"setting1": "value1", "setting2": "value2"}
    context.set_detailed_stats_table_writer_config(config)
    assert context.get_detailed_stats_table_writer_config == config


def test_set_dq_expectations():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    dq_expectations = {"column1": "expectation1", "column2": "expectation2"}
    context.set_dq_expectations(dq_expectations)
    assert context.get_dq_expectations == dq_expectations


def test_set_rules_execution_settings_config():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    config = {"setting1": "value1", "setting2": "value2"}
    context.set_rules_execution_settings_config(config)
    assert context.get_rules_execution_settings_config == config


def test_get_row_dq_start_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._row_dq_start_time = datetime.now()
    assert context.get_row_dq_start_time == context._row_dq_start_time


def test_get_row_dq_end_time():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._row_dq_end_time = datetime.now()
    assert context.get_row_dq_end_time == context._row_dq_end_time


def test_get_row_dq_start_time_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._row_dq_start_time = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, 
            please assign '_row_dq_start_time'  before 
            accessing it""",
    ):
        context.get_row_dq_start_time


def test_get_row_dq_end_time_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._row_dq_end_time = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_row_dq_end_time'  before 
            accessing it""",
    ):
        context.get_row_dq_end_time


def test_set_query_dq_detailed_stats_status():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    assert context._enable_query_dq_detailed_result == True
    assert context.get_query_dq_detailed_stats_status == True


def test_get_query_dq_output_custom_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    context.set_dq_detailed_stats_table_name("test_table")
    context.set_query_dq_output_custom_table_name("test_table")
    assert context.get_query_dq_output_custom_table_name == "test_table"


def test_get_query_dq_output_custom_table_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    context.set_dq_detailed_stats_table_name(None)
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign 
            '_dq_detailed_stats_table_name,query_dq_detailed_stats_status' before 
            accessing it""",
    ):
        context.get_query_dq_output_custom_table_name


def test_get_dq_detailed_stats_table_name():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    context.set_dq_detailed_stats_table_name("test_table")
    assert context.get_dq_detailed_stats_table_name == "test_table"


def test_get_dq_detailed_stats_table_name_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context.set_query_dq_detailed_stats_status(True)
    context.set_dq_detailed_stats_table_name(None)
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign 
            '_dq_detailed_stats_table_name' before 
            accessing it""",
    ):
        context.get_dq_detailed_stats_table_name


def test_get_dq_expectations():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    dq_expectations = {"column1": "expectation1", "column2": "expectation2"}
    context.set_dq_expectations(dq_expectations)
    assert context.get_dq_expectations == dq_expectations


def test_get_dq_expectations_exception():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    context._dq_expectations = None
    with pytest.raises(
        SparkExpectationsMiscException,
        match="""The spark expectations context is not set completely, please assign '_dq_expectations' before 
            accessing it""",
    ):
        context.get_dq_expectations


def test_set_querydq_secondary_queries():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    querydq_secondary_queries = {"query1": "query1", "query2": "query2"}
    context.set_querydq_secondary_queries(querydq_secondary_queries)
    assert context.get_querydq_secondary_queries == querydq_secondary_queries


def test_get_querydq_secondary_queries():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    querydq_secondary_queries = {"query1": "query1", "query2": "query2"}
    context.set_querydq_secondary_queries(querydq_secondary_queries)
    assert context.get_querydq_secondary_queries == querydq_secondary_queries


def test_get_source_query_dq_output():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    source_query_dq_output = [{"column1": "value1", "column2": "value2"}]
    context._source_query_dq_output = source_query_dq_output
    assert context.get_source_query_dq_output == source_query_dq_output


def test_set_target_query_dq_output():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    target_query_dq_output = [{"column1": "value1", "column2": "value2"}]
    context.set_target_query_dq_output(target_query_dq_output)
    assert context._target_query_dq_output == target_query_dq_output


def test_get_target_query_dq_output():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    target_query_dq_output = [{"column1": "value1", "column2": "value2"}]
    context._target_query_dq_output = target_query_dq_output
    assert context.get_target_query_dq_output == target_query_dq_output


def test_get_source_query_dq_output():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    source_query_dq_output = [{"column1": "value1", "column2": "value2"}]
    context._source_query_dq_output = source_query_dq_output
    assert context.get_source_query_dq_output == source_query_dq_output


def test_set_source_query_dq_output():
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    source_query_dq_output = [{"column1": "value1", "column2": "value2"}]
    context.set_source_query_dq_output(source_query_dq_output)
    assert context._source_query_dq_output == source_query_dq_output


def test_set_enable_error_table():
    # default case is True for enabling error table
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    assert context.get_se_enable_error_table is True

    # testing for False do not write error records in error table
    context.set_se_enable_error_table(False)
    assert context.get_se_enable_error_table is False


def test_set_dq_rules_params():
    # default case is empty dictionary for dq rules params and testing negative scenario
    context = SparkExpectationsContext(product_id="product1", spark=spark)
    assert context.get_dq_rules_params == {}

    # testing when passing parameterizied values to dq rules
    context._dq_rules_params = {"env": "local"}
    assert context.get_dq_rules_params == {"env": "local"}


def test_get_dq_expectations():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_dq_expectations({"rule1": "expectation1", "rule2": "expectation2"})

    # Test when _dq_expectations is set
    assert context.get_dq_expectations == {
        "rule1": "expectation1",
        "rule2": "expectation2",
    }

    # Test when _dq_expectations is not set
    context._dq_expectations = None
    with pytest.raises(SparkExpectationsMiscException):
        context.get_dq_expectations()


def test_set_dq_expectations():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    dq_expectations = {
        "rule1": "expectation1",
        "rule2": "expectation2",
        "rule3": "expectation3",
    }
    context.set_dq_expectations(dq_expectations)
    assert context._dq_expectations == dq_expectations


def test_set_job_metadata():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_job_metadata("{'job_name': 'test_job_metadata'}")
    assert context._job_metadata == "{'job_name': 'test_job_metadata'}"


def test_get_job_metadata():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context._job_metadata = "{'job_name': 'test_job_metadata'}"
    assert context.get_job_metadata == "{'job_name': 'test_job_metadata'}"

    # testing for None condition
    context._job_metadata = None
    assert context.get_job_metadata is None


def test_set_enable_obs_dq_report_result():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_enable_obs_dq_report_result(True)
    assert context.get_enable_obs_dq_report_result is True


def test_get_enable_obs_dq_report_result():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_enable_obs_dq_report_result(True)
    assert context.get_enable_obs_dq_report_result is True

    # testing for None condition
    context._enable_obs_dq_report_result = None
    assert context.get_enable_obs_dq_report_result is None


def test_set_se_dq_obs_alert_flag():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_se_dq_obs_alert_flag(True)
    assert context.get_se_dq_obs_alert_flag is True


def test_get_se_dq_obs_alert_flag():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_se_dq_obs_alert_flag(True)
    assert context.get_se_dq_obs_alert_flag is True

    # testing for None condition
    context._se_dq_obs_alert_flag = None
    assert context.get_se_dq_obs_alert_flag is None


def test_set_detailed_default_template():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_detailed_default_template("test_template")
    assert context.get_detailed_default_template == "test_template"


def test_get_detailed_default_template():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_detailed_default_template("test_template")
    assert context.get_detailed_default_template == "test_template"

    # testing for None condition
    context._detailed_default_template = None
    assert context.get_detailed_default_template is None


def test_set_basic_default_template():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_basic_default_template("test_template")
    assert context.get_basic_default_template == "test_template"


def test_get_basic_default_template():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_basic_default_template("test_template")
    assert context.get_basic_default_template == "test_template"

    # testing for None condition
    context._basic_default_template = None
    assert context.get_basic_default_template is None


def test_set_stats_detailed_dataframe():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    data = [("test_product_id", "test_schema.table1", 5)]
    columns = ["product_id", "table_name", "error_count"]
    df = spark.createDataFrame(data, columns)
    context.set_stats_detailed_dataframe(df)


def test_get_stats_detailed_dataframe():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    data = [("test_product_id", "test_schema.table1", 5)]
    columns = ["product_id", "table_name", "error_count"]
    df = spark.createDataFrame(data, columns)
    context._stats_detailed_dataframe = df

    if context.get_stats_detailed_dataframe is None:
        assert context.get_stats_detailed_dataframe is None
    else:
        assert context.get_stats_detailed_dataframe.collect() == df.collect()


def test_set_custom_detailed_dataframe():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    data = [("test_product_id", "test_schema.table1", 5)]
    columns = ["product_id", "table_name", "error_count"]
    df = spark.createDataFrame(data, columns)
    context.set_custom_detailed_dataframe(df)


def test_get_custom_detailed_dataframe():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    data = [("test_product_id", "test_schema.table1", 5)]
    columns = ["product_id", "table_name", "error_count"]
    df = spark.createDataFrame(data, columns)
    context._custom_detailed_dataframe = df

    if context.get_custom_detailed_dataframe is None:
        assert context.get_custom_detailed_dataframe is None
    else:
        assert context.get_custom_detailed_dataframe.collect() == df.collect()


def test_set_report_table_name():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_report_table_name("test_table")
    assert context.get_report_table_name == "test_table"


def test_get_report_table_name():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_report_table_name("test_table")
    assert context.get_report_table_name == "test_table"

    # testing for None condition
    context._report_table_name = None
    assert context.get_report_table_name is None


def test_set_dq_obs_rpt_gen_status_flag():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_dq_obs_rpt_gen_status_flag(True)
    assert context.get_dq_obs_rpt_gen_status_flag is True


def test_get_dq_obs_rpt_gen_status_flag():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    context.set_dq_obs_rpt_gen_status_flag(True)
    assert context.get_dq_obs_rpt_gen_status_flag is True

    # testing for None condition
    context._dq_obs_rpt_gen_status_flag = None
    assert context.get_dq_obs_rpt_gen_status_flag is None


def test_set_df_dq_obs_report_dataframe():
    #
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    data = [("test_product_id", "test_schema.table1", 5)]
    columns = ["product_id", "table_name", "error_count"]
    df = spark.createDataFrame(data, columns)
    context.set_df_dq_obs_report_dataframe(df)


def test_get_df_dq_obs_report_dataframe():
    context = SparkExpectationsContext(product_id="test_product", spark=spark)
    data = [("test_product_id", "test_schema.table1", 5)]
    columns = ["product_id", "table_name", "error_count"]
    df = spark.createDataFrame(data, columns)
    context._df_dq_obs_report_dataframe = df

    if context.get_df_dq_obs_report_dataframe is None:
        assert context.get_df_dq_obs_report_dataframe is None
    else:
        assert context.get_df_dq_obs_report_dataframe.collect() == df.collect()
