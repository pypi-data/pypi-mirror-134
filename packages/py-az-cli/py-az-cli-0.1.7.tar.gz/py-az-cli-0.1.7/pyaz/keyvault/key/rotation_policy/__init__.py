from .... pyaz_utils import _call_az

def show(hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Get the rotation policy of a Key Vault key.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key rotation-policy show", locals())


def update(value, hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Update the rotation policy of a Key Vault key.

    Required Parameters:
    - value -- The rotation policy file definition as JSON, or a path to a file containing JSON policy definition.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key rotation-policy update", locals())

