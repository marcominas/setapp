#!/usr/bin/python
# -*- coding: utf-8 -*

from os import getenv

WAIT_TIME = 30
TOTAL_WORKERS = 1
TOTAL_THREADS = 1
APPLICATION_NAME = "Gestalt Sample application"
APPLICATION_DESCRIPTION = "Gestalt is just a synonym of settings/configuration"

LOG_MIN_LEVEL = 1
LOG_LOG_FILE = getenv('LOG_LOG_FILE')
LOG_ROTATION_INTERVAL = 1
LOG_BACKUP_FILES_LIMIT = 5

SQL_SERVERS = 'my-sql-server.net'
SQL_DATABASE = 'my-database'
SQL_DATABASE_USERNAME = getenv('MY_SQL_DATABASE_USERNAME')
SQL_DATABASE_PASSWORD = getenv('MY_SQL_DATABASE_PASSWORD')
SQL_DATABASE_QUERIES_PATH = '/Repo/GIT/gestalt/gestalt/sql/queries'

AWS_ACCOUNT = getenv('AWS_ACCOUNT')
SQS_AWS_KEY = getenv('SQS_AWS_KEY')
SQS_AWS_SECRET = getenv('SQS_AWS_SECRET')
SQS_AWS_REGION = "sa-east-1"
SQS_QUEUE_NAME_TEMPLATE = "https://sqs.{region}.amazonaws.com/{account}/my-queue-name"
SQS_QUEUE_NAME = SQS_QUEUE_NAME_TEMPLATE.format(region=SQS_AWS_REGION, account=AWS_ACCOUNT)
SQS_TOTAL_ITEMS = 1
SQS_POOL_TIME = 1
