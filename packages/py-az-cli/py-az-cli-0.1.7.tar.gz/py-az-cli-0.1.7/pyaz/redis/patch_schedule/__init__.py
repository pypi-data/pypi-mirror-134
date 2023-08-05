from ... pyaz_utils import _call_az

def create(name, resource_group, schedule_entries):
    '''
    Create patching schedule for Redis cache.

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schedule_entries -- List of Patch schedule entries. Example Value:[{"dayOfWeek":"Monday","startHourUtc":"00","maintenanceWindow":"PT5H"}]
    '''
    return _call_az("az redis patch-schedule create", locals())


def update(name, resource_group, schedule_entries):
    '''
    Update the patching schedule for Redis cache.

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schedule_entries -- List of Patch schedule entries. Example Value:[{"dayOfWeek":"Monday","startHourUtc":"00","maintenanceWindow":"PT5H"}]
    '''
    return _call_az("az redis patch-schedule update", locals())


def delete(name, resource_group):
    '''
    Deletes the patching schedule of a redis cache.

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis patch-schedule delete", locals())


def show(name, resource_group):
    '''
    Gets the patching schedule of a redis cache.

    Required Parameters:
    - name -- Name of the Redis cache.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az redis patch-schedule show", locals())

