# LPaaS-Python-client

**LPaaS-Python-client** is a client to enable comunication with [LPaaS-ws](https://gitlab.com/pika-lab/lpaas/lpaas-ws/-/tree/develop).

## How to install

```bash
pip install lpaas-client
```

## How to use

You have just to create a LPClient and use it.

```python
# you can use `lpaas_client.asyn` for the async version
# or `from lpaas_client import AsyncLPClient`
from lpaas_client import LPClient
from lpaas_client import AuthData
url = 'url to LPaaS'
client = LPClient(url)
with client:
    client.authenticate(AuthData('user', 'passw0rd'))
    theories = client.get_theories()
    ...
```

| Remember to call `client.authenticate` to authenticate yourself to the server.