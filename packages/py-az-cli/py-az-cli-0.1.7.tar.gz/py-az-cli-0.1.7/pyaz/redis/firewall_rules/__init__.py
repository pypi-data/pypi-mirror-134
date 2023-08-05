from ... pyaz_utils import _call_az

def create(end_ip, name, resource_group, rule_name, start_ip):
    '''
    Create a redis cache firewall rule.

    Required Parameters:
    - end_ip -- Highest IP address included in the range.
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The name of the firewall rule.
    - start_ip -- Lowest IP address included in the range.
    '''
    return _call_az("az redis firewall-rules create", locals())


def update(end_ip, name, resource_group, rule_name, start_ip):
    '''
    Update a redis cache firewall rule.

    Required Parameters:
    - end_ip -- Highest IP address included in the range.
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The name of the firewall rule.
    - start_ip -- Lowest IP address included in the range.
    '''
    return _call_az("az redis firewall-rules update", locals())


def delete(name, resource_group, rule_name):
    '''
    

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The name of the firewall rule.
    '''
    return _call_az("az redis firewall-rules delete", locals())


def show(name, resource_group, rule_name):
    '''
    

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The name of the firewall rule.
    '''
    return _call_az("az redis firewall-rules show", locals())


def list(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis firewall-rules list", locals())

