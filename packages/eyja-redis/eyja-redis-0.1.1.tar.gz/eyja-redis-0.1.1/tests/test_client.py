import aioredis
import json

from unittest import IsolatedAsyncioTestCase

from slugify import slugify

from eyja.main import Eyja
from eyja.interfaces.db import BaseStorageModel
from eyja.utils import EyjaJSONEncoder


class RedisClientTest(IsolatedAsyncioTestCase):
    redis_url = 'redis://localhost:30002/5'
    config = '''
        storages:
            redis:
                port: 30002
                db:
                    base: 5
    '''

    class TestModel(BaseStorageModel):
        _namespace = ':::test_table'
        _key_template = 'object_id.test_str'
        
        test_str: str

    async def test_connection(self):
        await Eyja.reset()
        await Eyja.init(
            config=self.config,
            plugins=['eyja_redis']
        )

        self.assertTrue(Eyja.is_initialized())

    async def test_save_model(self):
        await Eyja.reset()
        await Eyja.init(
            config=self.config,
            plugins=['eyja_redis']
        )

        obj = self.TestModel(
            test_str='Test123'
        )
        await obj.save()

        str_data = json.dumps(obj.data, cls=EyjaJSONEncoder)

        key = f'test_table.{obj.object_id}.{slugify("Test123")}'

        redis_connection = aioredis.from_url(self.redis_url)
        async with redis_connection.client() as conn:
            redis_data = await conn.get(key)

        self.assertEqual(str_data, redis_data.decode())


    async def test_delete_model(self):
        await Eyja.reset()
        await Eyja.init(
            config=self.config,
            plugins=['eyja_redis']
        )

        obj = self.TestModel(
            test_str='Test1'
        )
        await obj.save()
        await obj.delete()

        key = f'test_table.{obj.object_id}.{slugify("Test1")}'

        redis_connection = aioredis.from_url(self.redis_url)
        async with redis_connection.client() as conn:
            redis_data = await conn.get(key)

        self.assertIsNone(redis_data)

    async def test_delete_all_models(self):
        await Eyja.reset()
        await Eyja.init(
            config=self.config,
            plugins=['eyja_redis']
        )

        await self.TestModel(test_str='Test2').save()
        await self.TestModel(test_str='Test2').save()
        await self.TestModel(test_str='Test2').save()
        await self.TestModel(test_str='Test22').save()
        await self.TestModel(test_str='Test22').save()

        await self.TestModel.delete_all({'test_str': 'Test2'})

        self.assertEqual(len(await self.TestModel.find({'test_str': 'Test2'})), 0)
        self.assertEqual(len(await self.TestModel.find({'test_str': 'Test22'})), 2)

    async def test_get_model(self):
        await Eyja.reset()
        await Eyja.init(
            config=self.config,
            plugins=['eyja_redis']
        )

        obj = self.TestModel(
            test_str='Test3'
        )
        await obj.save()

        get_obj = await self.TestModel.get(obj.object_id)

        self.assertEqual(get_obj.test_str, obj.test_str)

    async def test_find_models(self):
        await Eyja.reset()
        await Eyja.init(
            config=self.config,
            plugins=['eyja_redis']
        )

        await self.TestModel(test_str='Test4').save()
        await self.TestModel(test_str='Test4').save()
        await self.TestModel(test_str='Test4').save()
        await self.TestModel(test_str='Test44').save()
        await self.TestModel(test_str='Test44').save()

        self.assertEqual(len(await self.TestModel.find({'test_str': 'Test4'})), 3)
        self.assertEqual(len(await self.TestModel.find({'test_str': 'Test44'})), 2)
