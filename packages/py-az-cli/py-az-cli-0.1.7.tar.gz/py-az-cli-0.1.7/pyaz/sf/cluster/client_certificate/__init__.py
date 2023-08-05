from .... pyaz_utils import _call_az

def add(cluster_name, resource_group, admin_client_thumbprints=None, certificate_common_name=None, certificate_issuer_thumbprint=None, client_certificate_common_names=None, is_admin=None, readonly_client_thumbprints=None, thumbprint=None):
    '''
    Add a common name or certificate thumbprint to the cluster for client authentication.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - admin_client_thumbprints -- client certificate thumbprint that only has admin permission.
    - certificate_common_name -- client certificate common name.
    - certificate_issuer_thumbprint -- client certificate issuer thumbprint.
    - client_certificate_common_names -- JSON encoded parameters configuration. Use @{file} to load from a file. For example: [{"isAdmin":true, "certificateCommonName": "test.com", "certificateIssuerThumbprint": "22B4AE296B504E512DF880A77A2CAE20200FF922"}]
    - is_admin -- Client authentication type.
    - readonly_client_thumbprints -- Space-separated list of client certificate thumbprint that has read only permission.
    - thumbprint -- client certificate thumbprint.
    '''
    return _call_az("az sf cluster client-certificate add", locals())


def remove(cluster_name, resource_group, certificate_common_name=None, certificate_issuer_thumbprint=None, client_certificate_common_names=None, thumbprints=None):
    '''
    Remove client certificates or subject names used for authentication.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - certificate_common_name -- client certificate common name.
    - certificate_issuer_thumbprint -- client certificate issuer thumbprint.
    - client_certificate_common_names -- JSON encoded parameters configuration. Use @{file} to load from a file. For example: [{"certificateCommonName": "test.com","certificateIssuerThumbprint": "22B4AE296B504E512DF880A77A2CAE20200FF922"}]
    - thumbprints -- A single or Space-separated list of client certificate thumbprint(s) to be remove.
    '''
    return _call_az("az sf cluster client-certificate remove", locals())

