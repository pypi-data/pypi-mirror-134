'''
Manage Azure Event Grid topics, domains, domain topics, system topics partner topics, event subscriptions, system topic event subscriptions and partner topic event subscriptions.
'''
from .. pyaz_utils import _call_az
from . import domain, event_subscription, extension_topic, system_topic, topic, topic_type

