'''
Manage Azure Container Services.
'''
from .. pyaz_utils import _call_az
from . import dcos, kubernetes


def browse(name, resource_group, disable_browser=None, ssh_key_file=None):
    '''
    Show the dashboard for a service container's orchestrator in a web browser.

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disable_browser -- Do not open browser after opening a proxy to the cluster web user interface
    - ssh_key_file -- If set a path to an SSH key to use, only applies to DCOS
    '''
    return _call_az("az acs browse", locals())


def create(name, resource_group, admin_password=None, admin_username=None, agent_count=None, agent_osdisk_size=None, agent_ports=None, agent_profiles=None, agent_storage_profile=None, agent_vm_size=None, agent_vnet_subnet_id=None, api_version=None, client_secret=None, deployment_name=None, dns_prefix=None, generate_ssh_keys=None, location=None, master_count=None, master_first_consecutive_static_ip=None, master_osdisk_size=None, master_profile=None, master_storage_profile=None, master_vm_size=None, master_vnet_subnet_id=None, no_wait=None, orchestrator_type=None, orchestrator_version=None, service_principal=None, ssh_key_value=None, tags=None, validate=None, windows=None):
    '''
    Create a new container service.

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - admin_password -- The adminstration password for Windows nodes. Only available if --windows=true
    - admin_username -- User name for the Linux Virtual Machines.
    - agent_count -- None
    - agent_osdisk_size -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. Set the default disk size for agent pools vms. Unit in GB. Default: corresponding vmsize disk size
    - agent_ports -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. Set the default ports exposed on the agent pools. Only usable for non-Kubernetes. Default: 8080,4000,80
    - agent_profiles -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. The file or dictionary representation of the agent profiles. Note it will override any agent settings once set
    - agent_storage_profile -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. Set default storage profile for agent pools. Default: varies based on Orchestrator
    - agent_vm_size -- Set the default size for agent pools vms.
    - agent_vnet_subnet_id -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. Set the default custom vnet subnet id for agent pools. Note agent need to used the same vnet if master set. Default: ""
    - api_version -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. Use API version of ACS to perform az acs operations. Available options: 2017-01-31, 2017-07-01. Default: the latest version for the location
    - client_secret -- None
    - deployment_name -- ==SUPPRESS==
    - dns_prefix -- Sets the Domain name prefix for the cluster. The concatenation of the domain name and the regionalized DNS zone make up the fully qualified domain name associated with the public IP address.
    - generate_ssh_keys -- Generate SSH public and private key files if missing
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - master_count -- The number of masters for the cluster.
    - master_first_consecutive_static_ip -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. The first consecutive ip used to specify static ip block.
    - master_osdisk_size -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. The disk size for master pool vms. Unit in GB. Default: corresponding vmsize disk size
    - master_profile -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. The file or dictionary representation of the master profile. Note it will override any master settings once set
    - master_storage_profile -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. Default: varies based on Orchestrator
    - master_vm_size -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. 
    - master_vnet_subnet_id -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. The custom vnet subnet id. Note agent need to used the same vnet if master set. Default: ""
    - no_wait -- Do not wait for the long-running operation to finish.
    - orchestrator_type -- The type of orchestrator used to manage the applications on the cluster.
    - orchestrator_version -- Feature in preview, only in canadacentral, canadaeast, centralindia, koreasouth, koreacentral, southindia, uksouth, ukwest, westcentralus, westindia, westus2. Use Orchestrator Version to specify the semantic version for your choice of orchestrator.
    - service_principal -- None
    - ssh_key_value -- Configure all linux machines with the SSH RSA public key string.  Your key should include three parts, for example 'ssh-rsa AAAAB...snip...UcyupgH azureuser@linuxvm
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - validate -- Generate and validate the ARM template without creating any resources
    - windows -- If true, set the default osType of agent pools to be Windows.
    '''
    return _call_az("az acs create", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a container service.

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acs delete", locals())


def list(resource_group=None):
    '''
    List container services.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acs list", locals())


def list_locations():
    '''
    List locations where Azure Container Service is in preview and in production.
    '''
    return _call_az("az acs list-locations", locals())


def scale(name, new_agent_count, resource_group):
    '''
    Change the private agent count of a container service.

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - new_agent_count -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acs scale", locals())


def show(name, resource_group):
    '''
    Show the details for a container service.

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acs show", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for a container service to reach a desired state.

    Required Parameters:
    - name -- Name of the container service. You can configure the default using `az configure --defaults acs=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az acs wait", locals())

