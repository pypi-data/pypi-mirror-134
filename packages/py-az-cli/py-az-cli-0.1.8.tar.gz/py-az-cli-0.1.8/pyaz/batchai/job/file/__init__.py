'''
Commands to list and stream files in job's output directories.
'''
from .... pyaz_utils import _call_az

def list(experiment, job, resource_group, workspace, expiry=None, output_directory_id=None, path=None):
    '''
    List job's output files in a directory with given id.

    Required Parameters:
    - experiment -- Name of experiment.
    - job -- Name of job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - expiry -- Time in minutes for how long generated download URL should remain valid.
    - output_directory_id -- The Id of the job's output directory (as specified by "id" element in outputDirectories collection in the job create parameters).
    - path -- Relative path in the given output directory.
    '''
    return _call_az("az batchai job file list", locals())


def stream(experiment, file_name, job, resource_group, workspace, output_directory_id=None, path=None):
    '''
    Stream the content of a file (similar to 'tail -f').

    Required Parameters:
    - experiment -- Name of experiment.
    - file_name -- The name of the file to stream.
    - job -- Name of job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - output_directory_id -- The Id of the job's output directory (as specified by "id" element in outputDirectories collection in the job create parameters).
    - path -- Relative path in the given output directory.
    '''
    return _call_az("az batchai job file stream", locals())

