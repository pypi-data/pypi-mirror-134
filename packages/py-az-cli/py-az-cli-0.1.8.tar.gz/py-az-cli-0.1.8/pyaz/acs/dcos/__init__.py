'''
Commands to manage a DC/OS-orchestrated Azure Container Service.
'''
from ... pyaz_utils import _call_az

def browse(name, resource_group, disable_browser=None, ssh_key_file=None):
    '''
    

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disable_browser -- Do not open browser after opening a proxy to the cluster web user interface
    - ssh_key_file -- Path to an SSH key file to use.
    '''
    return _call_az("az acs dcos browse", locals())


def install_cli(client_version=None, install_location=None):
    '''
    Download and install the DC/OS command-line tool for a cluster.

    Optional Parameters:
    - client_version -- Version of kubectl to install.
    - install_location -- Path at which to install kubectl.
    '''
    return _call_az("az acs dcos install-cli", locals())

