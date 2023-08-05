from .... pyaz_utils import _call_az

def add(cluster_name, resource_group, common_name=None, is_admin=None, issuer_thumbprint=None, thumbprint=None):
    '''
    Add a new client certificate to the managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - common_name -- Client certificate common name.
    - is_admin -- Client authentication type.
    - issuer_thumbprint -- Space-separated list of issuer thumbprints.
    - thumbprint -- Client certificate thumbprint.
    '''
    return _call_az("az sf managed-cluster client-certificate add", locals())


def delete(cluster_name, resource_group, common_name=None, thumbprint=None):
    '''
    Delete a client certificate from the managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - common_name -- A single or Space-separated list of client certificate common name(s) to be remove.
    - thumbprint -- A single or Space-separated list of client certificate thumbprint(s) to be remove.
    '''
    return _call_az("az sf managed-cluster client-certificate delete", locals())

