# -*- coding: utf-8 -*-

import boto3
from phcli.ph_aws.aws_root import PhAWS

class PhDynamoDB(PhAWS):
    def __init__(self, *args, **kwargs):
        self.access_key = kwargs.get('access_key', None)
        self.secret_key = kwargs.get('secret_key', None)
        if self.access_key and self.secret_key:
            self.dynamodb_client = boto3.client('dynamodb', region_name='cn-northwest-1',
                                          aws_access_key_id=self.access_key,
                                          aws_secret_access_key=self.secret_key)
            self.dynamodb_resource = boto3.resource('dynamodb', region_name='cn-northwest-1',
                                              aws_access_key_id=self.access_key,
                                              aws_secret_access_key=self.secret_key)
            return

        self.phsts = kwargs.get('phsts', None)
        if self.phsts and self.phsts.credentials:
            self.dynamodb_client = boto3.client('dynamodb', **self.phsts.get_cred())
            self.dynamodb_resource = boto3.resource('dynamodb', **self.phsts.get_cred())
            return

        self.dynamodb_client = boto3.client('dynamodb')
        self.dynamodb_resource = boto3.resource('dynamodb')

    def put_data(self, table_name, items):
        """
        向DynamoDB的表中 插入数据
        :param table_name: 写入数据表的名称
        :param items: 插入的数据
        :return:
        """
        table = self.dynamodb_resource.Table(table_name)
        table.put_item(
            Item=items
        )

