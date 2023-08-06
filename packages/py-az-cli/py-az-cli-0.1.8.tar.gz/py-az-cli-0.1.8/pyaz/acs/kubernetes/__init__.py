'''
Commands to manage a Kubernetes-orchestrated Azure Container Service.
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
    return _call_az("az acs kubernetes browse", locals())


def get_credentials(name, resource_group, file=None, overwrite_existing=None, ssh_key_file=None):
    '''
    Download and install credentials to access a cluster.  This command requires the same private-key used to create the cluster.

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - file -- Where to install the kubectl config file
    - overwrite_existing -- If specified, overwrite any existing credentials.
    - ssh_key_file -- Path to an SSH key file to use
    '''
    return _call_az("az acs kubernetes get-credentials", locals())


def install_cli(base_src_url=None, client_version=None, install_location=None, kubelogin_base_src_url=None, kubelogin_install_location=None, kubelogin_version=None):
    '''
    Download and install the Kubernetes command-line tool for a cluster.

    Optional Parameters:
    - base_src_url -- Base download source URL for kubectl releases.
    - client_version -- Version of kubectl to install.
    - install_location -- Path at which to install kubectl.
    - kubelogin_base_src_url -- Base download source URL for kubelogin releases.
    - kubelogin_install_location -- Path at which to install kubelogin.
    - kubelogin_version -- Version of kubelogin to install.
    '''
    return _call_az("az acs kubernetes install-cli", locals())

