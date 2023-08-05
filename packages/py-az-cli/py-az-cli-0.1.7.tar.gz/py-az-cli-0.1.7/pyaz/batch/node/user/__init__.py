'''
Manage the user accounts of a Batch compute node.
'''
from .... pyaz_utils import _call_az

def create(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None, expiry_time=None, is_admin=None, json_file=None, name=None, password=None, ssh_public_key=None):
    '''
    Add a user account to a Batch compute node.

    Required Parameters:
    - node_id -- The ID of the machine on which you want to create a user Account.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - expiry_time -- If omitted, the default is 1 day from the current time. For Linux Compute Nodes, the expiryTime has a precision up to a day. Expected format is an ISO-8601 timestamp.
    - is_admin -- Whether the Account should be an administrator on the Compute Node. The default value is false. True if flag present.
    - json_file -- A file containing the user specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'User Arguments' are ignored.
    - name -- Required.
    - password -- The password is required for Windows Compute Nodes (those created with 'cloudServiceConfiguration', or created with 'virtualMachineConfiguration' using a Windows Image reference). For Linux Compute Nodes, the password can optionally be specified along with the sshPublicKey property.
    - ssh_public_key -- The public key should be compatible with OpenSSH encoding and should be base 64 encoded. This property can be specified only for Linux Compute Nodes. If this is specified for a Windows Compute Node, then the Batch service rejects the request; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request).
    '''
    return _call_az("az batch node user create", locals())


def delete(node_id, pool_id, user_name, account_endpoint=None, account_key=None, account_name=None, yes=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the machine on which you want to delete a user Account.
    - pool_id -- The ID of the Pool that contains the Compute Node.
    - user_name -- The name of the user Account to delete.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batch node user delete", locals())


def reset(node_id, pool_id, user_name, account_endpoint=None, account_key=None, account_name=None, expiry_time=None, json_file=None, password=None, ssh_public_key=None):
    '''
    Update the properties of a user account on a Batch compute node. Unspecified properties which can be updated are reset to their defaults.

    Required Parameters:
    - node_id -- The ID of the machine on which you want to update a user Account.
    - pool_id -- The ID of the Pool that contains the Compute Node.
    - user_name -- The name of the user Account to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - expiry_time -- If omitted, the default is 1 day from the current time. For Linux Compute Nodes, the expiryTime has a precision up to a day. Expected format is an ISO-8601 timestamp.
    - json_file -- A file containing the node update user parameter specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Node Update User Arguments' are ignored.
    - password -- The password is required for Windows Compute Nodes (those created with 'cloudServiceConfiguration', or created with 'virtualMachineConfiguration' using a Windows Image reference). For Linux Compute Nodes, the password can optionally be specified along with the sshPublicKey property. If omitted, any existing password is removed.
    - ssh_public_key -- The public key should be compatible with OpenSSH encoding and should be base 64 encoded. This property can be specified only for Linux Compute Nodes. If this is specified for a Windows Compute Node, then the Batch service rejects the request; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). If omitted, any existing SSH public key is removed.
    '''
    return _call_az("az batch node user reset", locals())

