import uuid
import aioredis
import json


from slugify import slugify

from eyja.interfaces.db import BaseStorageClient, DataFilter
from eyja.utils import EyjaJSONEncoder

from .config import RedisConfig


class RedisClient(BaseStorageClient):
    _connection = None
    _config: RedisConfig
    _config_cls = RedisConfig

    def key(self, obj):
        result = []

        key_template_nodes = obj._key_template.split('.')
        for node in key_template_nodes:
            if hasattr(obj, node):
                result.append(slugify(getattr(obj, node)))
            else:
                result.append(node)

        return '.'.join(result)

    def filtered_key(self, obj_cls, filter = {}):
        result = []

        key_template_nodes = obj_cls._key_template.split('.')
        for node in key_template_nodes:
            if node in filter:
                result.append(slugify(filter[node]))
            else:
                result.append('*')

        return '.'.join(result)

    def get_redis_url(self, db_name):
        return f'redis://{self._config.host}:{self._config.port}/{self._config.db[db_name]}'

    def get_redis_connection(self, db_name):
        return aioredis.from_url(self.get_redis_url(db_name))

    async def init(self):
        self._buckets.extend(list(self._config.db.keys()))

    async def save(self, obj, object_space, object_type):
        if not obj.object_id:
            obj.object_id = str(uuid.uuid4())

        hierarchical_key = f'{object_type}.{self.key(obj)}'

        async with self.get_redis_connection(object_space).client() as conn:
            await conn.delete(hierarchical_key)

            set_args = [
                hierarchical_key,
                json.dumps(obj.data, cls=EyjaJSONEncoder),
            ]

            if obj._expiration > 0:
                set_args.append(obj._expiration)

            await conn.set(*set_args)

    async def delete(self, obj, object_space, object_type):
        hierarchical_key = f'{object_type}.{self.key(obj)}'

        async with self.get_redis_connection(object_space).client() as conn:
            await conn.delete(hierarchical_key)

    async def delete_all(self, obj, object_space, object_type, filter):
        search_key = self.filtered_key(obj, filter)
        hierarchical_key = f'{object_type}.{search_key}'
        async with self.get_redis_connection(object_space).client() as conn:
            keys = await conn.keys(hierarchical_key)
            for key in keys:
                await conn.delete(key)

    async def get(self, obj_cls, object_space, object_type, object_id):
        filter = DataFilter(fields={'object_id': object_id})
        items = await self.find(obj_cls, object_space, object_type, filter)
        
        if len(items) > 0:
            return items[0]
        
        return None

    async def find(self, obj_cls, object_space, object_type, filter):
        result = []

        search_key = self.filtered_key(obj_cls, filter.fields)
        hierarchical_key = f'{object_type}.{search_key}'
        async with self.get_redis_connection(object_space).client() as conn:
            keys = await conn.keys(hierarchical_key)
            for key in keys:
                data = await conn.get(key)
                obj_data = json.loads(data)
                result.append(obj_cls(**obj_data))
        
        return result
