from .... pyaz_utils import _call_az

def create(account, compute_policy_name, object_id, object_type, max_dop_per_job=None, min_priority_per_job=None, resource_group=None):
    '''
    Create a compute policy in the Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - compute_policy_name -- None
    - object_id -- None
    - object_type -- None

    Optional Parameters:
    - max_dop_per_job -- None
    - min_priority_per_job -- None
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account compute-policy create", locals())


def update(account, compute_policy_name, max_dop_per_job=None, min_priority_per_job=None, resource_group=None):
    '''
    Update a compute policy in the Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - compute_policy_name -- None

    Optional Parameters:
    - max_dop_per_job -- None
    - min_priority_per_job -- None
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account compute-policy update", locals())


def list(account, resource_group=None):
    '''
    List compute policies in the a Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account compute-policy list", locals())


def show(account, compute_policy_name, resource_group=None):
    '''
    Retrieve a compute policy in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - compute_policy_name -- The name of the compute policy to retrieve.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account compute-policy show", locals())


def delete(account, compute_policy_name, resource_group=None):
    '''
    Delete a compute policy in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - compute_policy_name -- The name of the compute policy to delete.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account compute-policy delete", locals())

