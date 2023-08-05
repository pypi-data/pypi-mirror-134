from ... pyaz_utils import _call_az

def show(profile_name, resource_group, security_policy_name):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - security_policy_name -- Name of the security policy.
    '''
    return _call_az("az afd security-policy show", locals())


def list(profile_name, resource_group):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd security-policy list", locals())


def create(domains, profile_name, resource_group, security_policy_name, waf_policy):
    '''
    Creates a new security policy within the specified profile.

    Required Parameters:
    - domains -- The domains to associate with the WAF policy. Could either be the ID of an endpoint (default domain will be used in that case) or ID of a custom domain.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - security_policy_name -- Name of the security policy.
    - waf_policy -- The ID of Front Door WAF policy.
    '''
    return _call_az("az afd security-policy create", locals())


def update(profile_name, resource_group, security_policy_name, domains=None, waf_policy=None):
    '''
    Update an existing security policy within the specified profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - security_policy_name -- Name of the security policy.

    Optional Parameters:
    - domains -- The domains to associate with the WAF policy. Could either be the ID of an endpoint (default domain will be used in that case) or ID of a custom domain.
    - waf_policy -- The ID of Front Door WAF policy.
    '''
    return _call_az("az afd security-policy update", locals())


def delete(profile_name, resource_group, security_policy_name, yes=None):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - security_policy_name -- Name of the security policy.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd security-policy delete", locals())

