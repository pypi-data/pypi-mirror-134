# C27Cache

C27Cache is a simple HTTP caching library designed to work with [FastAPI](https://fastapi.tiangolo.com/)

## Installation

While C27Cache is still early in it's development it's been used in production on a couple of service. 


### With pip

```shell
pip install c27cache
```

### With Poetry

```shell
poetry add c27cache
```

## Usage and Examples

### Basic Usage

1. #### Initialize C27Cache

```python
from c27cache.config import C27Cache
C27Cache.init(redis_url=REDIS_URL, namespace='test_namespace')
```

2. #### Define your controllers

The `ttl_in_seconds` expires the cache in 180 seconds. There are other approaches to take with helpers like `expire_end_of_day` and `expires_end_of_week`

```python

import redis
from datetime import datetime
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from c27cache.config import C27Cache
from c27cache.service import cache

@app.get("/b/home")
@cache(key="b.home", ttl_in_seconds=180)
async def home(request: Request, response: Response):
    return JSONResponse({"page": "home", "datetime": str(datetime.utcnow())})

@app.get("/b/welcome")
@cache(key="b.home", end_of_week=True)
async def home(request: Request, response: Response):
    return JSONResponse({"page": "welcome", "datetime": str(datetime.utcnow())})    
```

### Building keys from parameter objects.

While it's always possible to explicitly pass keys onto the `key` attribute, there are scenarios where the keys need to be build based on the parameters received by the controller method. For instance, in an authenticated API where the `user_id` is fetched as a controlled `Depends` argument.

```python
@app.get("/b/logged-in")
@cache(key="b.logged_in.{}", obj="user", obj_attr="id")
async def logged_in(request: Request, response: Response, user=user):
    return JSONResponse(
        {"page": "home", "user": user.id, "datetime": str(datetime.utcnow())}
    )
```

In the example above, the key allows room for a dynamic attribute fetched from the object `user`. The key eventually becomes `b.logged_in.112358` if the `user.id` returns `112358` 


### Explicitly invalidating the cache

The cache invalidation can be managed using the `@invalidate_cache` decorator. 

```python
@app.post("/b/logged-in")
@invalidate_cache(
    key="b.logged_in.{}", obj="user", obj_attr="id", namespace="test_namespace"
)
async def post_logged_in(request: Request, response: Response, user=user):
    return JSONResponse(
        {"page": "home", "user": user.id, "datetime": str(datetime.utcnow())}
    )
```

## Full Example

```python
import os
import redis
from datetime import datetime
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from c27cache.config import C27Cache
from c27cache.service import cache, invalidate_cache

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/3")
redis_client = redis.Redis.from_url(REDIS_URL)

class User:
    id: str = "112358"

user = User()
app = FastAPI()

C27Cache.init(redis_url=REDIS_URL, namespace='test_namespace')

@app.get("/b/home")
@cache(key="b.home", ttl_in_seconds=180)
async def home(request: Request, response: Response):
    return JSONResponse({"page": "home", "datetime": str(datetime.utcnow())})


@app.get("/b/logged-in")
@cache(key="b.logged_in.{}", obj="user", obj_attr="id")
async def logged_in(request: Request, response: Response, user=user):
    return JSONResponse(
        {"page": "home", "user": user.id, "datetime": str(datetime.utcnow())}
    )


@app.post("/b/logged-in")
@invalidate_cache(
    key="b.logged_in.{}", obj="user", obj_attr="id", namespace="test_namespace"
)
async def post_logged_in(request: Request, response: Response, user=user):
    return JSONResponse(
        {"page": "home", "user": user.id, "datetime": str(datetime.utcnow())}
    )

```

## Caching methods that aren't controllers

C27Cache works exactly the same way with regular methods. The example below explains usage of the cache in service objects and application services.

```python
import os
import redis
from c27cache.config import C27Cache
from c27cache.service import cache, invalidate_cache

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/3")
redis_client = redis.Redis.from_url(REDIS_URL)

class User:
    id: str = "112358"

user = User()


C27Cache.init(redis_url=REDIS_URL, namespace='test_namespace')


@cache(key='cache.me', ttl_in_seconds=360)
async def cache_me(x:int, invoke_count:int):
    invoke_count = invoke_count + 1
    result = x * 2
    return [result, invoke_count]
````