from ... pyaz_utils import _call_az

def list(location):
    '''
    Show all commitment tiers for Azure Cognitive Services.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az cognitiveservices commitment-tier list", locals())

