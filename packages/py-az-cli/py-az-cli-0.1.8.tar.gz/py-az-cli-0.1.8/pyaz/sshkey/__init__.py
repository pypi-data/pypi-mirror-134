'''
Manage ssh public key with vm
'''
from .. pyaz_utils import _call_az

def list(resource_group=None):
    '''
    List all of the SSH public keys.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sshkey list", locals())


def show(name, resource_group):
    '''
    Retrieve information about an SSH public key.

    Required Parameters:
    - name -- The name of the SSH public key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sshkey show", locals())


def create(name, resource_group, location=None, public_key=None, tags=None):
    '''
    Create a new SSH public key resource.

    Required Parameters:
    - name -- The name of the SSH public key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - public_key -- SSH public key used to authenticate to a virtual machine through ssh. If this property is not initially provided when the resource is created, the publicKey property will be populated when generateKeyPair is called. If the public key is provided upon resource creation, the provided public key needs to be at least 2048-bit and in ssh-rsa format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sshkey create", locals())


def update(name, resource_group, public_key=None, tags=None):
    '''
    Update an SSH public key resource.

    Required Parameters:
    - name -- The name of the SSH public key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - public_key -- SSH public key used to authenticate to a virtual machine through ssh. If this property is not initially provided when the resource is created, the publicKey property will be populated when generateKeyPair is called. If the public key is provided upon resource creation, the provided public key needs to be at least 2048-bit and in ssh-rsa format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sshkey update", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete an SSH public key.

    Required Parameters:
    - name -- The name of the SSH public key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sshkey delete", locals())

