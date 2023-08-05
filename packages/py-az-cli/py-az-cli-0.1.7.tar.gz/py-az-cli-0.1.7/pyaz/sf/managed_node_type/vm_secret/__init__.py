from .... pyaz_utils import _call_az

def add(certificate_store, certificate_url, cluster_name, resource_group, source_vault_id):
    '''
    Add a secret to the node type.

    Required Parameters:
    - certificate_store -- Specifies the certificate store on the Virtual Machine to which the certificate should be added. The specified certificate store is implicitly in the LocalMachine account.
    - certificate_url -- This is the URL of a certificate that has been uploaded to Key Vault as a secret. For adding a secret to the Key Vault, see [Add a key or secret to the key vault](https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add). In this case, your certificate needs to be It is the Base64 encoding of the following JSON Object which is encoded in UTF-8: <br><br> {<br>  "data":"<Base64-encoded-certificate>",<br>  "dataType":"pfx",<br>  "password":"<pfx-file-password>"<br>}/
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - source_vault_id -- Key Vault resource id containing the certificates.
    '''
    return _call_az("az sf managed-node-type vm-secret add", locals())

