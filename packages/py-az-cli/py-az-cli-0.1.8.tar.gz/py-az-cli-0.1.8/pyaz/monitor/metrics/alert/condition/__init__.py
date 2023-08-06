'''
Manage near-realtime metric alert rule conditions.
'''
from ..... pyaz_utils import _call_az

def create(aggregation, metric, operator, type, dimension=None, namespace=None, num_periods=None, num_violations=None, sensitivity=None, since=None, skip_metric_validation=None, threshold=None):
    '''
    Build a metric alert rule condition.

    Required Parameters:
    - aggregation -- Time aggregation.
    - metric -- Name of metric.
    - operator -- Operator for static threshold can be 'Equals', 'NotEquals', 'GreaterThan', 'GreaterThanOrEqual', 'LessThan' or 'LessThanOrEqual'. Operator for dynamic threshold can be 'GreaterThan', 'LessThan', 'GreaterOrLessThan'.
    - type -- Type of condition threshold.

    Optional Parameters:
    - dimension -- Dimension created by 'az monitor metrics alert dimension create'.
    - namespace -- Namespace of metric.
    - num_periods -- The number of evaluation periods for dynamic threshold. Range: 1-6.
    - num_violations -- The number of violations to trigger an dynamic alert. Range: 1-6. It should be less than or equal to --num-periods.
    - sensitivity -- Alert sensitivity for dynamic threshold.
    - since -- The date from which to start learning the metric historical data and calculate the dynamic thresholds. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm)
    - skip_metric_validation -- Cause the metric validation to be skipped. This allows to use a metric that has not been emitted yet.
    - threshold -- Static threshold value.
    '''
    return _call_az("az monitor metrics alert condition create", locals())

