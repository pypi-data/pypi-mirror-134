from .... pyaz_utils import _call_az

def create(name, resource_group, workspace_name, description=None, if_match=None, no_wait=None):
    '''
    Create an self-hosted integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - description -- The integration runtime description.
    - if_match -- ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse integration-runtime self-hosted create", locals())

