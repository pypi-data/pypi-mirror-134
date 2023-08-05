from ... pyaz_utils import _call_az

def rerun(name, run_id, workspace_name):
    '''
    Rerun single trigger instance by runId.

    Required Parameters:
    - name -- The trigger name.
    - run_id -- The trigger run identifier.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse trigger-run rerun", locals())


def cancel(name, run_id, workspace_name):
    '''
    Cancel a single trigger instance by runId.

    Required Parameters:
    - name -- The trigger name.
    - run_id -- The trigger run identifier.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse trigger-run cancel", locals())


def query_by_workspace(last_updated_after, last_updated_before, workspace_name, continuation_token=None, filters=None, order_by=None):
    '''
    Query trigger runs in the workspace based on input filter conditions.

    Required Parameters:
    - last_updated_after -- The time at or after which the run event was updated in 'ISO 8601' format.
    - last_updated_before -- The time at or before which the run event was updated in 'ISO 8601' format.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - continuation_token -- The continuation token for getting the next page of results. Null for first page.
    - filters -- List of filters.
    - order_by -- List of OrderBy option.
    '''
    return _call_az("az synapse trigger-run query-by-workspace", locals())

