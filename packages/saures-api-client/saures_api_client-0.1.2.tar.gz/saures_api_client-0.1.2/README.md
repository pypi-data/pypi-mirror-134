SAURES API Client
=================

[SAURES](https://saures.ru) API client

Stage: Alpha

Installation
------------

1. From this repository (`poetry` required)
* `git clone https://github.com/Yurzs/saures_api_client.git`
* `cd saures_api_client`
* `poetry install --no-dev`

2. From PyPi
* `pip install saures_api_client`

Usage
-----

1. You can use all the api methods like they are named in [SAURES API docs](https://api.saures.ru/doc/):
```python
from saures_api_client import SauresAPIClient

async def main():
    client = SauresAPIClient("your email", "your password")

    objects = await client.user_objects()

...
```

2. Or you can use more user-friendly wrapper around the client:
```python
from saures_api_client import SauresAPIClient
from saures_api_client import types

async def main():
    user = SauresAPIClient.get_user("your email", "your password")
    
    locations = await user.get_locations()
    # returns typing.List[types.Location]
    
    location = locations[0]
    location_controllers = await location.get_controllers()
    # returns typing.List[types.Controller]
    # so you can easily propagate deeper in entities without
    # specifically providing their IDs to the client.

```
