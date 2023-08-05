from ... pyaz_utils import _call_az

def show(profile_name, resource_group, rule_set_name):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rule set.
    '''
    return _call_az("az afd rule-set show", locals())


def list(profile_name, resource_group):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd rule-set list", locals())


def create(profile_name, resource_group, rule_set_name):
    '''
    Creates a new rule set under the specified profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rule set.
    '''
    return _call_az("az afd rule-set create", locals())


def delete(profile_name, resource_group, rule_set_name, yes=None):
    '''
    Delete the rule set.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rule set.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd rule-set delete", locals())

