# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sign_off']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['sign-off = sign_off.sign_off:main']}

setup_kwargs = {
    'name': 'sign-off',
    'version': '0.1.0',
    'description': 'pre-commit hook to add "signed-off-by" line to commit messages',
    'long_description': '# sign-off\n\n**_Hook for [pre-commit](https://pre-commit.com/) to add a signature line to\ncommit messages._**\n\n[![PyPI version](https://img.shields.io/pypi/v/sign-off.svg)](https://pypi.python.org/pypi/sign-off/)\n[![PyPI downloads](https://img.shields.io/pypi/dm/sign-off.svg)](https://pypi.python.org/pypi/sign-off/)\n[![Tests passing](https://github.com/dynobo/sign-off/actions/workflows/python.yaml/badge.svg)](https://github.com/dynobo/sign-off/actions/workflows/python.yaml)\n[![Coverage Status](https://coveralls.io/repos/github/dynobo/sign-off/badge.svg)](https://coveralls.io/github/dynobo/sign-off)\n[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.gnu.org/licenses/mit)\n[![Code style: black](https://img.shields.io/badge/Code%20style-black-%23000000)](https://github.com/psf/black)\n\nThe hook is running in the `prepare-commit-msg`-stage and intended to add\n`Signed-off-by:`-lines often used in the context of\n[DOC](https://en.wikipedia.org/wiki/Developer_Certificate_of_Origin), but it\nshould be flexible enough for other use-cases as well.\n\n## Using with pre-commit\n\nAdd this to your `.pre-commit-config.yaml`:\n\n```yaml\n- repo: https://github.com/dynobo/sign-off\n    rev: v0.1.0\n    hooks:\n      - id: sign-off\n```\n\nThe default behavior is to append a signature line (if it does not yet contain\n`Signed-off-by:` as substring) which will result in a commit message like:\n\n```\nChanged something important\n\nSigned-off-by: dynobo <dynobo@mailbox.org>\n```\n\n## Optional arguments\n\nYou can add two optional arguments in the `.pre-commit-config.yaml`, e.g. here\nare the defaults:\n\n```yaml\n- repo: https://github.com/dynobo/sign-off\n    rev: v0.1.0\n    hooks:\n      - id: sign-off\n      - args:\n        - \'--template=\\n\\nSigned-off-by: <GIT_AUTHOR_IDENT>\'\n        - \'--skip-containing=Signed-off-by:\'\n```\n\nThe argument `--template` defines the text or template that is going to be\nappended _right_ after the commit message. Be sure to add white space in the\ntemplate, if needed.\n\nThe argument `--skip-containing` is a stopping criteria: If this string is\ncontained _somewhere_ in the commit message, the signature text will _not_ be\nappended. This avoids appending the same signature twice, when doing\n`git --amend` or such.\n\nIf you want to _always_ add the the signature, set the argument, but leave it\'s\nvalue empty empty: `--skip-containing=`\n\nBoth arguments support template tags in the form `<VariableName>`, where\n`VariableName` is one of the variables displayed when running `git var -l`. The\ntemplate tag will be replaced by the variables value in the corresponding\nstring.\n\nThe values of the two git variables `GIT_AUTHOR_IDENT` and `GIT_COMMITER_IDENT`\ncontain a timestamp at the end, which will get stripped when used as template\ntag.\n\nYou can add additional "git vars", e.g. if you add the following section to your\n`.gitconfig`...\n\n```conf\n[my-signature]\n    hash = sha:123456789\n    company_mail = dynobo@dynobo.corp\n```\n\n... then you can use those variables in the hook:\n\n```yaml\n- repo: https://github.com/dynobo/sign-off\n    rev: v0.1.0\n    hooks:\n      - id: sign-off\n      - args:\n        - \'--template=\\n\\nBy: <my-signature.company_mail> (<my-signature.company_mail>)\'\n        - \'--skip-containing=\\nBy: \'\n```\n',
    'author': 'dynobo',
    'author_email': 'dynobo@mailbox.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dynobo/sign-off',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
