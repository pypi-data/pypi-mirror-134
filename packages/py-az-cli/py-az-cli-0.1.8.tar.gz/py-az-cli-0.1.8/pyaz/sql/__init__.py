'''
Manage Azure SQL Databases and Data Warehouses.
'''
from .. pyaz_utils import _call_az
from . import db, dw, elastic_pool, failover_group, instance_failover_group, instance_pool, mi, midb, server, stg, virtual_cluster, vm


def list_usages(location):
    '''
    

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az sql list-usages", locals())


def show_usage(location, usage):
    '''
    

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - usage -- Name of usage metric to return.
    '''
    return _call_az("az sql show-usage", locals())

