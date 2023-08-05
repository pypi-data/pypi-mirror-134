# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['monobank_handler', 'monobank_handler.handler_utils']

package_data = \
{'': ['*']}

install_requires = \
['ecdsa>=0.13.2,<0.14.0', 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'monobank-handler',
    'version': '0.1.6',
    'description': 'Monobank.ua API implementation with handlers(poll/webhook)',
    'long_description': '# monobank_handler\n## forked and modded from:\nhttps://github.com/vitalik/python-monobank\n\n![GitHub-issues](https://img.shields.io/github/issues/vitalik/python-monobank)\n\n![python-monobank](https://raw.githubusercontent.com/vitalik/python-monobank/master/docs/logo.png)\n\nPython client for Monobank API (https://api.monobank.ua/docs/)\n\n## Installation\n\n```\npip install monobank_handler\n```\n\n\n# Usage\n\n## Personal api\n\n1) Request your token at https://api.monobank.ua/\n\n2) Use that token to initialize client:\n\n```python\n\nfrom src import monobank_handler\n\ntoken = \'xxxxxxxxxxxxxxx\'\n\nmono = monobank_handler.Client(token)\nuser_info = mono.get_client_info()\nprint(user_info)\n```\n# MODDED:\n## AMOUNT WITHOUT POINTS! \n### example:\nif you need 10.57 UAH - write amount=1057\n\nif you need 1.00 UAH - write amount=100\n## poll handler (sync/async):\n```\n@mono.pay_handler(amount=0, comment=None, may_be_bigger=True)\ndef func(pay_history):  #   may be async\n    print(pay_history)\nmono.run()  #   for async use await mono.start(account="0") or\n            #   await mono.idle(account="0")\n```\n## webhook handler (sync):\n```\n@mono.pay_handler_webhook(amount=0, account=None, comment=None, may_be_bigger=True)\ndef func(pay_history):  \n    print(pay_history)\nmono.run_webhook(http://your.web.address:port/route, port=3000, route="/webhook", host="0.0.0.0")\n```\n##  or you can do it by yourself using mono.\n### Methods\n\nGet currencies\n\n```python\n>>> mono.get_currency()\n[\n {\'currencyCodeA\': 840,\n  \'currencyCodeB\': 980,\n  \'date\': 1561686005,\n  \'rateBuy\': 25.911,\n  \'rateSell\': 26.2357},\n {\'currencyCodeA\': 978,\n  \'currencyCodeB\': 980,\n  \'date\': 1561686005,\n  \'rateBuy\': 29.111,\n  \'rateSell\': 29.7513},\n  ...\n```\n\nGet client info\n\n```python\n>>> mono.get_client_info()\n{\n  \'name\': \'Dmitriy Dubilet\'\n  \'accounts\': [\n    {\n      \'id\': \'accidxxxxx\'\n      \'balance\': 100000000,\n      \'cashbackType\': \'UAH\',\n      \'creditLimit\': 100000000,\n      \'currencyCode\': 980,\n      }\n  ],\n}\n\n```\n\n\nGet statements\n```python\n>>> mono.get_statements(\'accidxxxxx\', date(2019,1,1), date(2019,1,30))\n[\n  {\n    \'id\': \'iZDPhf8v32Qass\',\n    \'amount\': -127603,\n    \'balance\': 99872397,\n    \'cashbackAmount\': 2552,\n    \'commissionRate\': 0,\n    \'currencyCode\': 978,\n    \'description\': \'Smartass club\',\n    \'hold\': True,\n    \'mcc\': 5411,\n    \'operationAmount\': 4289,\n    \'time\': 1561658263\n  },\n  ...\n]\n```\n\nYou can as well pass datetime objects\n```python\n>>> mono.get_statements(\'accidxxxxx\', datetime(2019,1,1,11,15), datetime(2019,1,2,11,15))\n```\n\n\nCreate a Webhook\n```python\n>>> mono.create_webhook(\'https://myserver.com/hookpath\')\n```\n\n\n\n## Corporatre API\n\nDocumentation is here - https://api.monobank.ua/docs/corporate.html\n\nCorporate API have the same methods as Public API, but it does not have rate limitation, and it is a recomended way if you are handling data for commercial use (or just storing lot of personal data).\n\n### Getting access\n\n#### 1) Generate private key\n\n```\nopenssl ecparam -genkey -name secp256k1 -rand /dev/urandom -out priv.key\n```\n\nThis will output file **priv.key** \n\n**Warning**: do not share it with anyone, do not store it in public git repositories\n\n#### 2) Generate public key\n\n```\nopenssl ec -in priv.key  -pubout -out pub.key\n```\n\nThis will output file **pub.key** \n\n#### 3) Request API access \nSend an email to api@monobank.ua - describe your project, and attach **pub.key** (!!! NOT priv.key !!!)\n\n\n### Requesting permission from monobank user\n\nOnce your app got approved by Monobank team you can start using corporate API:\n\n\n#### 1) Create monobank user access request\n\n```python\nprivate_key = \'/path/to/your/priv.key\'\nrequest = monobank.access_request(\'ps\', private_key)\n```\nIf all fine you should recive the following:\n```python\nprint(request)\n{\'tokenRequestId\': \'abcdefg_Wg\', \'acceptUrl\': \'https://mbnk.app/auth/abcdefg_Wg\'}\n```\n\nYou should save tokenRequestId to database, and then give user the link acceptUrl\n\nNote: To be notified about user acceptance you can use web callback:\n\n```python\nmonobank.access_request(\'ps\', private_key, callback_url=\'https://yourserver.com/callback/\')\n```\n\n#### 2) Check if user accepted\n\nYou can check if user accepted access request like this:\n\n\n```python\nrequest_token = \'abcdefg_Wg\'  # the token from access_request result\nprivate_key = \'/path/to/your/priv.key\'\n\nmono = monobank.CorporateClient(request_token, private_key)\n\n\nmono.check()  # returns True if user accepted, False if not\n\n```\n\n\n#### 3) Use methods\n\nOnce user accepts your access-request, you can start using all the methods same ways as Public API\n\n```python\nmono.get_statements(....)\n```\n\n## Handling Errors\n\nIf you use Personal API you may encounter "Too Many Requests" error. To properly catch it and retry - use *monobank.TooManyRequests* exception\n\n```python\ntry:\n    mono.get_statements(....)\nexcept monobank.TooManyRequests:\n    time.sleep(1)\n    # try again:\n    mono.get_statements(....)\n```\n\nYou can use ratelimiter library (like https://pypi.org/project/ratelimiter/ ) to download all transactions\n',
    'author': 'George Viznyuk - (bezumnui)',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bezumnui/monobank_handler',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
