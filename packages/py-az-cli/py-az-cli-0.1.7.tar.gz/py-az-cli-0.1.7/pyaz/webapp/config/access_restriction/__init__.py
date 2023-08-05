from .... pyaz_utils import _call_az

def show(name, resource_group, slot=None):
    '''
    Show Access Restriction settings for webapp.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config access-restriction show", locals())


def add(name, priority, resource_group, action=None, description=None, http_headers=None, ignore_missing_endpoint=None, ip_address=None, rule_name=None, scm_site=None, service_tag=None, slot=None, subnet=None, vnet_name=None, vnet_resource_group=None):
    '''
    Adds an Access Restriction to the webapp.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - priority -- Priority of the access restriction rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - action -- Allow or deny access
    - description -- Description of the access restriction rule
    - http_headers -- space-separated http headers in a format of `<name>=<value>`
    - ignore_missing_endpoint -- Create access restriction rule with checking if the subnet has Microsoft.Web service endpoint enabled
    - ip_address -- IP address or CIDR range (optional comma separated list of up to 8 ranges)
    - rule_name -- Name of the access restriction rule to add
    - scm_site -- True if access restrictions is added for scm site
    - service_tag -- Service Tag (optional comma separated list of up to 8 tags)
    - slot -- the name of the slot. Default to the productions slot if not specified
    - subnet -- Subnet name (requires vNet name) or subnet resource id
    - vnet_name -- vNet name
    - vnet_resource_group -- Resource group of virtual network (default is web app resource group)
    '''
    return _call_az("az webapp config access-restriction add", locals())


def remove(name, resource_group, action=None, ip_address=None, rule_name=None, scm_site=None, service_tag=None, slot=None, subnet=None, vnet_name=None):
    '''
    Removes an Access Restriction from the webapp.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - action -- Allow or deny access
    - ip_address -- IP address or CIDR range (optional comma separated list of up to 8 ranges)
    - rule_name -- Name of the access restriction to remove
    - scm_site -- True if access restriction should be removed from scm site
    - service_tag -- Service Tag (optional comma separated list of up to 8 tags)
    - slot -- the name of the slot. Default to the productions slot if not specified
    - subnet -- Subnet name (requires vNet name) or subnet resource id
    - vnet_name -- vNet name
    '''
    return _call_az("az webapp config access-restriction remove", locals())


def set(name, resource_group, use_same_restrictions_for_scm_site, slot=None):
    '''
    Sets if SCM site is using the same restrictions as the main site.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - use_same_restrictions_for_scm_site -- Use same access restrictions for scm site

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config access-restriction set", locals())

