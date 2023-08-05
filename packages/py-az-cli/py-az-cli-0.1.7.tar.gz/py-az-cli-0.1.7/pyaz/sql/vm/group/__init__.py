'''
Manage SQL virtual machine groups.
'''
from .... pyaz_utils import _call_az
from . import ag_listener


def update(name, resource_group, add=None, bootstrap_acc=None, domain_fqdn=None, force_string=None, fsw_path=None, operator_acc=None, ou_path=None, remove=None, sa_key=None, service_acc=None, set=None, storage_account=None, tags=None):
    '''
    Updates a SQL virtual machine group if there are not SQL virtual machines attached to the group.

    Required Parameters:
    - name -- Name of the SQL virtual machine group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - bootstrap_acc -- Account name used for creating cluster (at minimum needs permissions to 'Create Computer Objects' in domain).
    - domain_fqdn -- Fully qualified name of the domain.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - fsw_path -- Optional path for fileshare witness.
    - operator_acc -- Account name used for operating cluster i.e. will be part of administrators group on all the participating virtual machines in the cluster.
    - ou_path -- Organizational Unit path in which the nodes and cluster will be present. Example: OU=WSCluster,DC=testdomain,DC=com
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - sa_key -- Primary key of the witness storage account.
    - service_acc -- Account name under which SQL service will run on all participating SQL virtual machines in the cluster.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - storage_account -- Storage account url of the witness storage account.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sql vm group update", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the SQL virtual machine group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql vm group show", locals())


def list(resource_group=None):
    '''
    

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql vm group list", locals())


def delete(name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - name -- Name of the SQL virtual machine group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql vm group delete", locals())


def create(domain_fqdn, image_offer, image_sku, name, operator_acc, resource_group, service_acc, storage_account, bootstrap_acc=None, fsw_path=None, location=None, ou_path=None, sa_key=None, tags=None):
    '''
    Creates a SQL virtual machine group.

    Required Parameters:
    - domain_fqdn -- Fully qualified name of the domain.
    - image_offer -- SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.
    - image_sku -- SQL image sku.
    - name -- Name of the SQL virtual machine group.
    - operator_acc -- Account name used for operating cluster i.e. will be part of administrators group on all the participating virtual machines in the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_acc -- Account name under which SQL service will run on all participating SQL virtual machines in the cluster.
    - storage_account -- Storage account url of the witness storage account.

    Optional Parameters:
    - bootstrap_acc -- Account name used for creating cluster (at minimum needs permissions to 'Create Computer Objects' in domain).
    - fsw_path -- Optional path for fileshare witness.
    - location -- Location. If not provided, group will be created in the same reosurce group location.You can configure the default location using `az configure --defaults location=<location>`.
    - ou_path -- Organizational Unit path in which the nodes and cluster will be present. Example: OU=WSCluster,DC=testdomain,DC=com
    - sa_key -- Primary key of the witness storage account.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sql vm group create", locals())

