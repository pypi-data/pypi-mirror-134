from ..... pyaz_utils import _call_az

def create(gateway_name, name, path_map_name, paths, resource_group, address_pool=None, http_settings=None, no_wait=None, redirect_config=None, rewrite_rule_set=None, waf_policy=None):
    '''
    Create a rule for a URL path map.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the url-path-map rule.
    - path_map_name -- The name of the URL path map.
    - paths -- Space-separated list of paths to associate with the rule. Valid paths start and end with "/" (ex: "/bar/")
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - address_pool -- The name or ID of the backend address pool to use with the created rule.
    - http_settings -- The name or ID of the HTTP settings to use with the created rule.
    - no_wait -- Do not wait for the long-running operation to finish.
    - redirect_config -- The name or ID of the redirect configuration to use with the created rule.
    - rewrite_rule_set -- The name or ID of the rewrite rule set. If not specified, the default for the map will be used.
    - waf_policy -- Name or ID of a Firewall Policy resource.
    '''
    return _call_az("az network application-gateway url-path-map rule create", locals())


def delete(gateway_name, name, path_map_name, resource_group, no_wait=None):
    '''
    Delete a rule of a URL path map.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the url-path-map rule.
    - path_map_name -- The name of the URL path map.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway url-path-map rule delete", locals())

