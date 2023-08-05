from eyja.interfaces.plugins import BasePlugin
from eyja.constants.types import PluginTypes

from .client import RedisClient


class RedisPlugin(BasePlugin):
    name = 'redis'
    plugin_type = PluginTypes.STORAGE_CLIENT

    @classmethod
    async def run(cls, **params):
        client = RedisClient(params)
        await client.init()

        return client
