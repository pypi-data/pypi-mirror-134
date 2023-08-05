from ... pyaz_utils import _call_az

def list(hsm_name=None, resource_group=None, vault_name=None):
    '''
    List the private link resources supported for a Key Vault/HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them)
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault private-link-resource list", locals())

