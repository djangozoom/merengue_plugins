from merengue.plugins import Plugin
from plugins.subscription.actions import SubscriptionAction


class PluginConfig(Plugin):
    name = 'Subscription'
    description = 'Subscription plugin'
    version = '0.0.1a'

    url_prefixes = (
        ('jugadores', 'plugins.subscription.urls'),
    )

    @classmethod
    def get_actions(cls):
        return [SubscriptionAction]
