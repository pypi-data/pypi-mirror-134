#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

from typing import Any, Dict, List, Optional, Tuple, Union
import requests
import json
from pyspark.sql import SparkSession
import pyspark.sql as sql
import pyspark.sql.catalog as catalog


class FeatureStore:
    feature_query_service_url: str
    spark_session: SparkSession

    def __init__(self, feature_query_service_url: str, spark_session: SparkSession):
        self.feature_query_service_url = feature_query_service_url
        self.spark_session = spark_session

    def get_table_name(self, table: catalog.Table):
        table.name

    def get_history_feature(self, label_table_info: dict,
                            feature_refs: List[str], dts: str, user: str, result_table_name: str,
                            is_local: bool) -> sql.dataframe:
        # curl "http://localhost:8080/offline_join_features?labelTable=defatic:user_model,magazi011,
        # 20211012&user=80261445&busType=rec"
        label_table_path = label_table_info.get('label_table_path')
        id_name = label_table_info.get('id_name')
        field_names = label_table_info.get('field_names')
        timestamp = label_table_info.get('timestamp')
        if not is_local:
            submit_job_request = self.feature_query_service_url + '/offline_join_features?' + "labelTable={0}&" \
                                                                                              "lableFieldNames={1}&" \
                                                                                              "uidName={2}&" \
                                                                                              "timestamp={3}&" \
                                                                                              "features={4}&" \
                                                                                              "dss={5}&user={6}".format(
                label_table_path, ','.join(field_names), id_name, timestamp, ','.join(feature_refs), dts, user)
            print(submit_job_request)
            r = requests.get(submit_job_request)
            task_id = ''
            if r.status_code == 200:
                content = json.loads(r.content)
                task_id = content['task_id']
                print(task_id)
            else:
                raise Exception('submit job failed ' + submit_job_request)
            table_name: str
            while 1:
                get_status_request = self.feature_query_service_url + "/get_job_status?" + "taskId=" + task_id
                print(get_status_request)
                r = requests.get(get_status_request)
                if r.status_code == 200:
                    content = json.loads(r.content)
                    status = content['status']
                    app_id = content['appId']
                    if status == 'FAILED' or status == 'KILLED':
                        print('spark job failed app id is ' + app_id)
                        raise Exception('job failed app id is ' + app_id)
                        break
                    if status == 'FINISHED':
                        table_name = content['tableName']
                        break
                else:
                    print('http request failed' + app_id)
                    raise Exception('http request failed ' + app_id)
                    break
                time.sleep(30)

            return self.spark_session.table(table_name)
        else:
            table_exists = False
            if result_table_name is None or result_table_name.isspace():
                {}
            else:
                table_exists = self.spark_session._jsparkSession.catalog().tableExists(result_table_name.split('.')[0],
                                                                        result_table_name.split('.')[1])
            submit_job_request = self.feature_query_service_url + '/get_assemble_sql?' + "labelTable={0}&" \
                                                                                         "lableFieldNames={1}&" \
                                                                                         "uidName={2}&" \
                                                                                         "timestamp={3}&" \
                                                                                         "features={4}&" \
                                                                                         "dss={5}&user={6}&" \
                                                                                         "resultTableName={7}&" \
                                                                                         "resultTableExists={8}".format(
                label_table_path, ','.join(field_names), id_name, timestamp, ','.join(feature_refs), dts, user,
                result_table_name, table_exists)
            print(submit_job_request)
            r = requests.get(submit_job_request)
            if r.status_code == 200:
                content = json.loads(r.content)
                sqls = str(content['sql'])
                table_name = str(content['resultTableName'])
                print(sqls)
                for sqltxt in sqls.strip().split(';'):
                    if not sqltxt.isspace():
                        print(sqltxt)
                        self.spark_session.sql(sqltxt)
                return self.spark_session.table(table_name)
            else:
                raise Exception('submit job failed ' + submit_job_request)

# if __name__ == '__main__':
# spark_session = SparkSession.builder.config('deploy-mode', 'client').master('local[*]').enableHiveSupport().getOrCreate()
# ml_feature_store = ml_feature_store.offline_store.FeatureStore('http://localhost:8080/', spark_session)
# feature_list = ['magazine.static:user_model', 'magazine.static:user_stage', 'magazine.static:user_province',
#                 'magazine.static:user_tourism']
# df = ml_feature_store.get_history_feature_store('default.feeds_label_feature_article_test',
#                                              'userid',
#                                              'predictId,docId,predictscore',
#                                              feature_list, '20211011', '80348083')
# print(df.head())
