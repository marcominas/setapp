#!/usr/bin/python
# -*- coding: utf-8 -*

from gestalt.default import *

# tip: to remove a unnecessary var from settings - not usual but possible.
del SQS_QUEUE_NAME_TEMPLATE
APPLICATION_NAME = APPLICATION_NAME + ' in staging environment'
