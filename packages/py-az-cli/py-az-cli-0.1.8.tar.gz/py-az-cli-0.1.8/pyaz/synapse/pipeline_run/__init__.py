from ... pyaz_utils import _call_az

def query_by_workspace(last_updated_after, last_updated_before, workspace_name, continuation_token=None, filters=None, order_by=None):
    '''
    Query pipeline runs in the workspace based on input filter conditions.

    Required Parameters:
    - last_updated_after -- The time at or after which the run event was updated in 'ISO 8601' format.
    - last_updated_before -- The time at or before which the run event was updated in 'ISO 8601' format.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - continuation_token -- The continuation token for getting the next page of results. Null for first page.
    - filters -- List of filters.
    - order_by -- List of OrderBy option.
    '''
    return _call_az("az synapse pipeline-run query-by-workspace", locals())


def show(run_id, workspace_name):
    '''
    Get a pipeline run by its run ID.

    Required Parameters:
    - run_id -- The pipeline run identifier.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse pipeline-run show", locals())


def cancel(run_id, workspace_name, is_recursive=None, yes=None):
    '''
    Cancel a pipeline run by its run ID.

    Required Parameters:
    - run_id -- The pipeline run identifier.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - is_recursive -- If true, cancel all the Child pipelines that are triggered by the current pipeline.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse pipeline-run cancel", locals())

