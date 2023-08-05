'''
Manage Azure Service Bus namespaces, queues, topics, subscriptions, rules and geo-disaster recovery configuration alias
'''
from .. pyaz_utils import _call_az
from . import georecovery_alias, migration, namespace, queue, topic

