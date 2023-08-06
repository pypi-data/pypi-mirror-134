from ... pyaz_utils import _call_az

def approve(description=None, hsm_name=None, id=None, name=None, no_wait=None, resource_group=None, vault_name=None):
    '''
    Approve a private endpoint connection request for a Key Vault/HSM.

    Optional Parameters:
    - description -- Comments for the approve operation.
    - hsm_name -- Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - vault_name -- Name of the Key Vault. Required if --id is not specified
    '''
    return _call_az("az keyvault private-endpoint-connection approve", locals())


def reject(description=None, hsm_name=None, id=None, name=None, no_wait=None, resource_group=None, vault_name=None):
    '''
    Reject a private endpoint connection request for a Key Vault/HSM.

    Optional Parameters:
    - description -- Comments for the reject operation.
    - hsm_name -- Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - vault_name -- Name of the Key Vault. Required if --id is not specified
    '''
    return _call_az("az keyvault private-endpoint-connection reject", locals())


def delete(hsm_name=None, id=None, name=None, no_wait=None, resource_group=None, vault_name=None):
    '''
    Delete the specified private endpoint connection associated with a Key Vault/HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - vault_name -- Name of the Key Vault. Required if --id is not specified
    '''
    return _call_az("az keyvault private-endpoint-connection delete", locals())


def list(hsm_name, resource_group=None):
    '''
    List all private endpoint connections associated with a HSM.

    Required Parameters:
    - hsm_name -- Name of the HSM.

    Optional Parameters:
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    '''
    return _call_az("az keyvault private-endpoint-connection list", locals())


def show(hsm_name=None, id=None, name=None, resource_group=None, vault_name=None):
    '''
    Show details of a private endpoint connection associated with a Key Vault/HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - vault_name -- Name of the Key Vault. Required if --id is not specified
    '''
    return _call_az("az keyvault private-endpoint-connection show", locals())


def wait(created=None, custom=None, deleted=None, exists=None, hsm_name=None, id=None, interval=None, name=None, resource_group=None, timeout=None, updated=None, vault_name=None):
    '''
    Place the CLI in a waiting state until a condition of the private endpoint connection is met.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - hsm_name -- Name of the HSM. Required if --id is not specified.(--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The ID of the private endpoint connection associated with the Key Vault/HSM. If specified --vault-name/--hsm-name and --name/-n, this should be omitted.
    - interval -- polling interval in seconds
    - name -- The name of the private endpoint connection associated with the Key Vault/HSM. Required if --id is not specified
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    - vault_name -- Name of the Key Vault. Required if --id is not specified
    '''
    return _call_az("az keyvault private-endpoint-connection wait", locals())

