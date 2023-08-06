from ... pyaz_utils import _call_az

def set(distribution, name, resource_group):
    '''
    Configure routing traffic to deployment slots.

    Required Parameters:
    - distribution -- space-separated slot routings in a format of `<slot-name>=<percentage>` e.g. staging=50. Unused traffic percentage will go to the Production slot
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az webapp traffic-routing set", locals())


def show(name, resource_group):
    '''
    Display the current distribution of traffic across slots.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az webapp traffic-routing show", locals())


def clear(name, resource_group):
    '''
    Clear the routing rules and send all traffic to production.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az webapp traffic-routing clear", locals())

