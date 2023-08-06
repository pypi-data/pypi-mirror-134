from ..... pyaz_utils import _call_az

def list(port_name, resource_group):
    '''
    List ExpressRoute links.

    Required Parameters:
    - port_name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route port link list", locals())


def show(name, port_name, resource_group):
    '''
    Get the details of an ExpressRoute link.

    Required Parameters:
    - name -- The link name of the ExpressRoute Port
    - port_name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route port link show", locals())


def update(name, port_name, resource_group, add=None, admin_state=None, force_string=None, macsec_cak_secret_identifier=None, macsec_cipher=None, macsec_ckn_secret_identifier=None, macsec_sci_state=None, no_wait=None, remove=None, set=None):
    '''
    Manage MACsec configuration of an ExpressRoute Link.

    Required Parameters:
    - name -- The link name of the ExpressRoute Port
    - port_name -- ExpressRoute port name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - admin_state -- Enable/Disable administrative state of an ExpressRoute Link
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - macsec_cak_secret_identifier -- The connectivity association key (CAK) ID that stored in the KeyVault.
    - macsec_cipher -- Cipher Method
    - macsec_ckn_secret_identifier -- The connectivity key name (CKN) that stored in the KeyVault.
    - macsec_sci_state -- Sci mode
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network express-route port link update", locals())

