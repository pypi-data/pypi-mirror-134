from .... pyaz_utils import _call_az

def create(name, resource_group, workspace_name, compute_type=None, core_count=None, description=None, if_match=None, location=None, no_wait=None, time_to_live=None):
    '''
    Create an managed integration runtime.

    Required Parameters:
    - name -- The integration runtime name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - compute_type -- Compute type of the data flow cluster which will execute data flow job.
    - core_count -- Core count of the data flow cluster which will execute data flow job.
    - description -- The integration runtime description.
    - if_match -- ETag of the integration runtime entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    - location -- The integration runtime location.
    - no_wait -- Do not wait for the long-running operation to finish.
    - time_to_live -- Time to live (in minutes) setting of the data flow cluster which will execute data flow job.
    '''
    return _call_az("az synapse integration-runtime managed create", locals())

