import redis
from typing import Union, Any, Tuple
import pytz
from c27cache.logger import log_info
from c27cache.expiry import C27CacheExpiry
from c27cache.config import C27Cache
import json


class C27RedisCacheBackend:
    def __init__(self, redis: redis.Redis, namespace: str = None):
        self.redis = redis
        self.namespace = namespace or C27Cache.namespace

    async def get_namespaced_key(self, key: str) -> str:
        return f"{self.namespace}:{key}".replace(" ", "")

    async def set(
        self,
        key: str,
        value: str,
        ttl_in_seconds: int = None,
        end_of_day: bool = False,
        end_of_week: bool = False,
    ):
        namespaced_key = await self.get_namespaced_key(key=key)
        ttl: int = await C27CacheExpiry.get_ttl(
            ttl_in_seconds=ttl_in_seconds,
            end_of_day=end_of_day,
            end_of_week=end_of_week,
        )

        stringified_value = value

        if not type(value) == bytes:
            stringified_value = json.dumps(value)

        with self.redis.pipeline(transaction=True) as pipe:
            pipe.multi()
            pipe.delete(namespaced_key)
            pipe.set(namespaced_key, stringified_value, ex=ttl)
            log_info(msg=f"CacheSet: {namespaced_key}")
            result = pipe.execute()

        del_status, set_status = result
        if del_status:
            log_info(msg=f"CacheClearedOnSet: {namespaced_key}")

        if set_status:
            log_info(msg=f"CacheSet: {namespaced_key}")
        return result

    async def get(self, key: str) -> Tuple[Union[int, None], Union[Any, None]]:
        namespaced_key = await self.get_namespaced_key(key=key)
        with self.redis.pipeline(transaction=True) as pipe:
            pipe.ttl(namespaced_key).get(namespaced_key)
            ttl, result = pipe.execute()

        if result:
            original_val = json.loads(result)
            log_info(msg=f"CacheHit: {namespaced_key}")
        else:
            original_val = None
        return ttl, original_val

    async def invalidate(self, key: str) -> bool:
        namespaced_key = await self.get_namespaced_key(key=key)

        with self.redis.pipeline(transaction=True) as pipe:
            pipe.multi()
            pipe.delete(namespaced_key)
            log_info(msg=f"CacheInvalidated: {namespaced_key}")
            result = pipe.execute()
        return result



