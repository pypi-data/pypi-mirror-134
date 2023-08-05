# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['structlogzio']

package_data = \
{'': ['*']}

install_requires = \
['logzio-python-handler==3.0.0']

setup_kwargs = {
    'name': 'logzio-structlog-handler',
    'version': '0.1.1',
    'description': 'Package for sending structlog-s to logzio',
    'long_description': '# logzio-structlog-handler\n\nHandler to send structlog logger to logzio\n\nAll logs have `host`, `pid` and `tid` added to them.\n\nExample of log created with handler:\n\n```python\nlogger.info(\n    "request_finished",\n    request=f"{METHOD} {ENDPOINT}",\n    code=response.status_code,\n    request_id=uuid4()\n)\n```\nLogzio:\n```shell\n  "_source": {\n    "request": "GET /account/ping",\n    "code": 200,\n    "level": "info",\n    "logger": "django_structlog.middlewares.request",\n    "ip": "127.0.0.1",\n    "log_level": "INFO",\n    "pid": 1,\n    "type": "http-bulk",\n    "message": "request_finished FOR GET /account/ping",\n    "tid": [\n      140649178957632\n    ],\n    "tags": [\n      "_logz_http_bulk_json_8070"\n    ],\n    "@timestamp": "2022-01-10T19:34:19.932Z",\n    "line_number": 71,\n    "host": "name-of-host",\n    "event": "request_finished",\n    "request_id": "3777349e-0247-4c89-ace2-ea2174930f39",\n    "path_name": "path/to/file.py",\n    "timestamp": "2022-01-10T19:34:19.931955Z",\n    "random_tag_1": "some_value",\n    "random_tag_2": 123\n  }\n```\n\n## Instructions:\n\n1. Install\n\n```shell\n❯ pip install logzio-structlog-handler\n```\n\n2. Add the following handler to you LOGGING file:\n\n```python    \nLOGGING = {\n    "handlers": {\n        "logzio": {\n            "class": "structlogzio.LogzIoStructlogHandler",\n            "level": "INFO",\n            "token": "YOUR_TOKEN",\n            "logs_drain_timeout": 5,\n            "url": "https://listener.logz.io:8071",\n            "network_timeout": 10,\n            # accepts any Dict[str, Any] value and passes it to all logs\n            "tags": {"random_tag_1": "some_value", "random_tag_2": 123},\n        }\n    },\n    "loggers": {\n        "": {"level": "INFO", "handlers": ["logzio"], "propagate": True},\n    },\n}   \n```\n',
    'author': 'nikooola',
    'author_email': 'nikolassmiljanic5@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/programeri-tech/logzio-structlog-handler',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
