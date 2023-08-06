from .... pyaz_utils import _call_az

def list(profile_name, resource_group):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd log-analytic location list", locals())

