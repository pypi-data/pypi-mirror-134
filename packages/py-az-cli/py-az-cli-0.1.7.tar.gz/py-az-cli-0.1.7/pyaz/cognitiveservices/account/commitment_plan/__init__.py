from .... pyaz_utils import _call_az

def create(auto_renew, commitment_plan_name, hosting_model, name, plan_type, resource_group, current_count=None, current_tier=None, next_count=None, next_tier=None):
    '''
    Create a commitment plan for Azure Cognitive Services account.

    Required Parameters:
    - auto_renew -- A boolean indicating whether to apply auto renew.
    - commitment_plan_name -- Cognitive Services account commitment plan name
    - hosting_model -- Cognitive Services account hosting model
    - name -- cognitive service account name
    - plan_type -- Cognitive Services account commitment plan type
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - current_count -- Cognitive Services account commitment plan current commitment period count.
    - current_tier -- Cognitive Services account commitment plan current commitment period tier.
    - next_count -- Cognitive Services account commitment plan next commitment period count.
    - next_tier -- Cognitive Services account commitment plan next commitment period tier.
    '''
    return _call_az("az cognitiveservices account commitment-plan create", locals())


def delete(commitment_plan_name, name, resource_group):
    '''
    Delete a commitment plan from Azure Cognitive Services account.

    Required Parameters:
    - commitment_plan_name -- Cognitive Services account commitment plan name
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account commitment-plan delete", locals())


def show(commitment_plan_name, name, resource_group):
    '''
    Show a commitment plan from Azure Cognitive Services account.

    Required Parameters:
    - commitment_plan_name -- Cognitive Services account commitment plan name
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account commitment-plan show", locals())


def list(name, resource_group):
    '''
    Show all commitment plans from Azure Cognitive Services account.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account commitment-plan list", locals())

