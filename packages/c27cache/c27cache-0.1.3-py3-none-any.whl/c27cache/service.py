from typing import Callable, Any
from functools import wraps
from c27cache.config import C27Cache
from c27cache.backend import C27RedisCacheBackend
from c27cache.logger import log_error

def cache(
    key: str,
    obj: Any = None,
    obj_attr: str = None,
    ttl_in_seconds: int = None,
    expire_end_of_day: bool = True,
    expire_end_of_week: bool = False,
    namespace: str = None,
):
    """Decorator method that sets the return value to cache before returning.

    Args:
        key (str): Key to be used for cache. The key is namespaced before storage
        obj (Any, optional): Name of the optional object from the router method needs 
                             to be accessed to generate the key. Defaults to None.
        obj_attr (str, optional): Name of the attribute for the optional object from the router 
                                  method that needs to be accessed to generate the key. Defaults to None.
        ttl_in_seconds (int, optional): Time To Live - Duration till which key stays in cache. Defaults to None.
        expire_end_of_day (bool, optional): Helper to set TTL which expires at the end of the day. Defaults to True.
        expire_end_of_week (bool, optional): Helper to set TTL expires at the end of the week. Defaults to False.
        namespace (str, optional): Namespace used for the keys inside redis. 
                                   Defaults to use env vars `APP_NAME`_`ENV` 
    """
    if not namespace:
        namespace = C27Cache.namespace
        
    def wrapper(func: Callable):
        @wraps(func)
        async def inner(*args, **kwargs):
            try:
                # extracts the `id` attribute from the `obj_attr` parameter passed to the `@cache` method
                _key = (
                    key.format(
                        getattr(kwargs[f"{obj}"], obj_attr),
                    )
                    if obj
                    else key
                )
                _cache = C27RedisCacheBackend(redis=C27Cache.redis_client, namespace=namespace)
                _request = kwargs.get("request", None)
                _response = kwargs.get("response", None)

                # check cache and return if value is present
                ttl, response = await _cache.get(key=_key)
                if response:
                    if _request and _response:
                        _response.headers["Cache-Control"] = f"max-age={ttl}"
                        _response.headers["C27Cache-Hit"] = "true"
                    return response

                # if not a cache-hit populate current response.
                _computed_response = await func(*args, **kwargs)

                # if http request store the response body data
                _cacheable_response = (
                    _computed_response.body
                    if kwargs.get("request", None)
                    else _computed_response
                )

                await _cache.set(
                    key=_key,
                    value=_cacheable_response,
                    ttl_in_seconds=ttl_in_seconds,
                    end_of_day=expire_end_of_day,
                    end_of_week=expire_end_of_week,
                )
                return _computed_response
            except Exception as e:
                log_error(msg=f"Cache Error: {e}", e=e, method="cache")
                return await func(*args, **kwargs)

        return inner

    return wrapper


def invalidate_cache(
    key: str,
    obj: Any = None,
    obj_attr: str = None,
    namespace: str = None,
):
    """Invalidates a specific cache key

    Args:
        key (str): Key to be invalidated
        obj (Any, optional): Name of the optional object from the router method needs 
                             to be accessed to generate the key. Defaults to None.
        obj_attr (str, optional): Name of the attribute for the optional object from the router 
        namespace (str, optional): Namespace used for the keys inside redis. 
                                   Defaults to use env vars `APP_NAME`_`ENV` 
    """
    if not namespace:
        namespace = C27Cache.namespace
        
    def wrapper(func: Callable):
        @wraps(func)
        async def inner(*args, **kwargs):
            try:
                # extracts the `id` attribute from the `obj_attr` parameter passed to the `@cache` method
                _key = (
                    key.format(
                        getattr(kwargs[f"{obj}"], obj_attr),
                    )
                    if obj
                    else key
                )
                _cache = C27RedisCacheBackend(redis=C27Cache.redis_client, namespace=namespace)
                await _cache.invalidate(key=_key)
                _computed_response = await func(*args, **kwargs)
                return _computed_response
            except Exception as e:
                log_error(msg=f"Cache Error: {e}", e=e, method="cache")
                return await func(*args, **kwargs)
        return inner
    return wrapper
