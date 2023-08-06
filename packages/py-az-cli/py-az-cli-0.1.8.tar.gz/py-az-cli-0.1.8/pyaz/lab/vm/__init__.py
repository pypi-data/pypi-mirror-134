'''
Manage VMs in an Azure DevTest Lab.
'''
from ... pyaz_utils import _call_az

def show(lab_name, name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Specify the $expand query. Example: 'properties($expand=artifacts,computeVm,networkInterface,applicableSchedule)'
    '''
    return _call_az("az lab vm show", locals())


def delete(lab_name, name, resource_group):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab vm delete", locals())


def start(lab_name, name, resource_group):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab vm start", locals())


def stop(lab_name, name, resource_group):
    '''
    

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab vm stop", locals())


def apply_artifacts(lab_name, name, resource_group, artifacts=None):
    '''
    Apply artifacts to a virtual machine in Azure DevTest Lab.

    Required Parameters:
    - lab_name -- The name of the lab.
    - name -- The name of the virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - artifacts -- The list of artifacts to apply.
    '''
    return _call_az("az lab vm apply-artifacts", locals())


def list(lab_name, resource_group, all=None, claimable=None, environment=None, expand=None, filters=None, object_id=None, order_by=None, top=None):
    '''
    List the VMs in an Azure DevTest Lab.

    Required Parameters:
    - lab_name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - all -- None
    - claimable -- None
    - environment -- None
    - expand -- None
    - filters -- None
    - object_id -- None
    - order_by -- None
    - top -- None
    '''
    return _call_az("az lab vm list", locals())


def claim(lab_name=None, name=None, resource_group=None):
    '''
    Claim a virtual machine from the Lab.

    Optional Parameters:
    - lab_name -- None
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az lab vm claim", locals())


def create(lab_name, name, resource_group, admin_password=None, admin_username=None, allow_claim=None, artifacts=None, authentication_type=None, disk_type=None, expiration_date=None, formula=None, generate_ssh_keys=None, image=None, image_type=None, ip_configuration=None, notes=None, saved_secret=None, size=None, ssh_key=None, subnet=None, tags=None, vnet_name=None):
    '''
    Create a VM in a lab.

    Required Parameters:
    - lab_name -- None
    - name -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - admin_password -- None
    - admin_username -- None
    - allow_claim -- None
    - artifacts -- None
    - authentication_type -- None
    - disk_type -- None
    - expiration_date -- None
    - formula -- None
    - generate_ssh_keys -- None
    - image -- None
    - image_type -- None
    - ip_configuration -- None
    - notes -- None
    - saved_secret -- None
    - size -- None
    - ssh_key -- None
    - subnet -- None
    - tags -- None
    - vnet_name -- None
    '''
    return _call_az("az lab vm create", locals())

