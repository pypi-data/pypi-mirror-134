# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['obfuskey']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'obfuskey',
    'version': '0.1.0',
    'description': 'A small library for creating reversible, obfuscated, identifier hashes using a given alphabet.',
    'long_description': "# ObfusKey\n\nObfusKey is a utility for generating obfuscated keys of integer values. While working\nto modernize its predecessor, [BaseHash](basehash), it was found that a lot of\nsimplifications could be made, thus ObfusKey was born.\n\nObfusKey was built solely for Python 3.6 or higher. For lower versions, you can still\nuse [BaseHash][basehash].\n\nObfusKey will generate obfuscated, reversible keys using a given alphabet and key\nlength. The maximum value it can process is `base ** key_length - 1`, where `base` is\nthe length of the provided alphabet. An optional modifier can also be provided, which is\nthen required when reversing the key into it's original value. If a modifier is not \nprovided, ObfusKey will generate the next prime integer after\n`base ** key_length - 1` along with a prime modifier. The default prime modifier will\ngenerate golden ratio primes, but this can be overwritten.\n\n## Install\n\n```text\n$ pip install obfuskey\n```\n\nIf you're building from source\n\n```text\n$ pip install .\n\nOR\n\n$ poetry install\n```\n\n## Usage\n\nTo use ObfusKey, you can use one of the available alphabets, or provide your own. You\ncan also provide your own multiplier, or leave it blank to use the built-in prime\ngenerator.\n\n```python\nfrom obfuskey import ObfusKey, alphabets\n\n\nobfuscator = ObfusKey(alphabets.BASE36, key_length=8)\n\nkey = obfuscator.to_key(1234567890)     # FWQ8H52I\nvalue = obfuscator.to_value('FWQ8H52I') # 1234567890\n```\n\nTo provide a custom multiplier, or if you to provide the prime generated from a\nprevious instance, you can pass it in with `multiplier=`. This value has to be an odd\ninteger.\n\n```python\nfrom obfuskey import ObfusKey, alphabets\n\n\nobfuscator = ObfusKey(alphabets.BASE62, multiplier=46485)\nkey = obfuscator.to_key(12345) # 0cpqVJ\n```\n\nIf you wish to generate a prime not within the golden prime set, you can overwrite the\nmultiplier with\n\n```python\nfrom obfuskey import ObfusKey, alphabets\n\n\nobfuscator = ObfusKey(alphabets.BASE62, key_length=3)\nkey = obfuscator.to_key(123) # 1O9\n\nobfuscator.set_prime_multiplier(1.75)\nkey = obfuscator.to_key(123) # Fyl\n```\n\n## Extras\n\nIf you need to obfuscate integers that are larger than 512-bit, you will need to also\nhave [gmp2][gmpy2] installed.\n\n```text\n$ pip install gmpy2\n\nOR\n\npoetry install -E gmpy2\n```\n\n[basehash]: https://github.com/bnlucas/python-basehash\n[gmpy2]: https://pypi.org/project/gmpy2/",
    'author': 'Nathan Lucas',
    'author_email': 'nathan@bnlucas.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bnlucas/obfuskey',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
