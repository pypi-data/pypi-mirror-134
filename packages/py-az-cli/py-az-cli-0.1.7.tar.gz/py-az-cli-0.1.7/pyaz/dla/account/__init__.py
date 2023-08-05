'''
Manage Data Lake Analytics accounts.
'''
from ... pyaz_utils import _call_az
from . import blob_storage, compute_policy, data_lake_store, firewall


def create(account, default_data_lake_store, location=None, max_degree_of_parallelism=None, max_job_count=None, query_store_retention=None, resource_group=None, tags=None, tier=None):
    '''
    Create a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - default_data_lake_store -- None

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - max_degree_of_parallelism -- None
    - max_job_count -- None
    - query_store_retention -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The desired commitment tier for this account to use.
    '''
    return _call_az("az dla account create", locals())


def update(account, allow_azure_ips=None, firewall_state=None, max_degree_of_parallelism=None, max_job_count=None, query_store_retention=None, resource_group=None, tags=None, tier=None):
    '''
    Update a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - allow_azure_ips -- Allow/block Azure originating IPs through the firewall
    - firewall_state -- Enable/disable existing firewall rules.
    - max_degree_of_parallelism -- The maximum supported degree of parallelism for this account.
    - max_job_count -- The maximum supported jobs running under the account at the same time.
    - query_store_retention -- The number of days that job metadata is retained.
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The desired commitment tier for this account to use.
    '''
    return _call_az("az dla account update", locals())


def list(resource_group=None):
    '''
    List available Data Lake Analytics accounts.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dla account list", locals())


def show(account, resource_group=None):
    '''
    Get the details of a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account show", locals())


def delete(account, resource_group=None):
    '''
    Delete a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account delete", locals())

