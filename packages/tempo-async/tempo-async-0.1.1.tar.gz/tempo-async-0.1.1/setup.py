# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tempo']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0',
 'httpx>=0.21.1,<0.22.0',
 'nest-asyncio>=1.5.4,<2.0.0',
 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'tempo-async',
    'version': '0.1.1',
    'description': 'An HTTP package for metering and managing async requests.',
    'long_description': "# Tempo\n\n*Asynchronous wrapper for HTTP requests.*\n\n## Installation\n\n```bash\npip install tempo-async\n```\n\n## Usage\n\n```python\nimport tempo\n\nurl = 'https://via.placeholder.com'\nnum_reqs = 100\n\nrequests = [ # map in any request parameters: url, query params, HTTP method, etc.\n  tempo.RequestConfig(url=url) for _ in range(num_reqs)\n]\n\nif __name__ == '__main__':\n  tempo.run(requests, rate=10) # fetch 100 cat pictures, 10 a second\n```\n\nTake it a step further by collecting the responses,\n\n```python\nimport tempo\n\nurl = 'https://via.placeholder.com'\nnum_reqs = 100\n\n### cat picture bucket\ncatpics = []\n###\n\nrequests = [ # map in any request parameters: url, query params, HTTP method, etc.\n  tempo.RequestConfig(url=url) for _ in range(num_reqs)\n]\n\nif __name__ == '__main__':\n  tempo.run(requests, collector=catpics, rate=10) # indicated `catpics` should store response\n  print(f'Pictures stored in list: {len(catpics)}')\n```\n\n… and adding any number of processing functions to handle responses.\n\n```python\nimport tempo\n\nurl = 'https://via.placeholder.com'\nnum_reqs = 100\ncatpics = []\n\nrequests = [ # map in any request parameters: url, query params, HTTP method, etc.\n  tempo.RequestConfig(url=url) for _ in range(num_reqs)\n]\n\n### processors\ndef say_hi(res) -> None:\n  # returns None so does not affect final processed response sent to collectors\n  print('Hello cat!')\n \ndef get_body(res) -> str:\n  # since it returns a value, this processor changes the final output of `tempo.run`\n  body = res.text\n  return body\n###\n\nif __name__ == '__main__':\n  # process the requests in order of listed processors\n  tempo.run(requests, collector=catpics, rate=10, processors=[say_hi, get_body])\n  # processors' return values affect output sent to collectors\n  print(f'Type of stored result: {type(catpics[0])}') # str, not Response object\n```\n\n\n\n## Contributing\n\nSubmit a pull request! Contributions are welcome!\n\nPlease write test coverage for your changes and run `tox` to test for backwards compatibility among the supported Python versions.\n\n## TODOS\n\nOpen an issue, create a branch, and submit a PR. (Tests for everything!)\n\n- Handle collection of results as a return value of the `run` function.\n- Decorator for basic async request function accepting iterator of request arguments.\n- Accept plain Python dictionaries and JSON in addition to RequestConfig objects for requests mapping.\n- Logging.\n- Exception handling.\n- GitHub Actions.\n- Retries with various back-off algorithms and HTTP response header search for 429 causes.\n- Generator option for `run` function.\n- Allow `collector` argument to be an iterable, a function passed a response / processed response object, or a file out. Maybe even stdout.\n- Like processors, allow multiple collectors (eg. file, queue).\n- Local database for keeping track of requests and their status, for retry and interrupts.\n- Asynchronous processor support.\n- Handle streaming responses.\n- CLI\n- Documentation page. Also, good docstrings.\n- Test coverage tracking.\n- …\n",
    'author': 'Nicholas Ballard',
    'author_email': 'nicholasericballard@gmail.com',
    'maintainer': 'Nicholas Ballard',
    'maintainer_email': 'nicholasericballard@gmail.com',
    'url': 'https://github.com/NicholasBallard/tempo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
