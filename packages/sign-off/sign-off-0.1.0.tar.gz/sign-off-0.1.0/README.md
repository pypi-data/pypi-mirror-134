# sign-off

**_Hook for [pre-commit](https://pre-commit.com/) to add a signature line to
commit messages._**

[![PyPI version](https://img.shields.io/pypi/v/sign-off.svg)](https://pypi.python.org/pypi/sign-off/)
[![PyPI downloads](https://img.shields.io/pypi/dm/sign-off.svg)](https://pypi.python.org/pypi/sign-off/)
[![Tests passing](https://github.com/dynobo/sign-off/actions/workflows/python.yaml/badge.svg)](https://github.com/dynobo/sign-off/actions/workflows/python.yaml)
[![Coverage Status](https://coveralls.io/repos/github/dynobo/sign-off/badge.svg)](https://coveralls.io/github/dynobo/sign-off)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.gnu.org/licenses/mit)
[![Code style: black](https://img.shields.io/badge/Code%20style-black-%23000000)](https://github.com/psf/black)

The hook is running in the `prepare-commit-msg`-stage and intended to add
`Signed-off-by:`-lines often used in the context of
[DOC](https://en.wikipedia.org/wiki/Developer_Certificate_of_Origin), but it
should be flexible enough for other use-cases as well.

## Using with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/dynobo/sign-off
    rev: v0.1.0
    hooks:
      - id: sign-off
```

The default behavior is to append a signature line (if it does not yet contain
`Signed-off-by:` as substring) which will result in a commit message like:

```
Changed something important

Signed-off-by: dynobo <dynobo@mailbox.org>
```

## Optional arguments

You can add two optional arguments in the `.pre-commit-config.yaml`, e.g. here
are the defaults:

```yaml
- repo: https://github.com/dynobo/sign-off
    rev: v0.1.0
    hooks:
      - id: sign-off
      - args:
        - '--template=\n\nSigned-off-by: <GIT_AUTHOR_IDENT>'
        - '--skip-containing=Signed-off-by:'
```

The argument `--template` defines the text or template that is going to be
appended _right_ after the commit message. Be sure to add white space in the
template, if needed.

The argument `--skip-containing` is a stopping criteria: If this string is
contained _somewhere_ in the commit message, the signature text will _not_ be
appended. This avoids appending the same signature twice, when doing
`git --amend` or such.

If you want to _always_ add the the signature, set the argument, but leave it's
value empty empty: `--skip-containing=`

Both arguments support template tags in the form `<VariableName>`, where
`VariableName` is one of the variables displayed when running `git var -l`. The
template tag will be replaced by the variables value in the corresponding
string.

The values of the two git variables `GIT_AUTHOR_IDENT` and `GIT_COMMITER_IDENT`
contain a timestamp at the end, which will get stripped when used as template
tag.

You can add additional "git vars", e.g. if you add the following section to your
`.gitconfig`...

```conf
[my-signature]
    hash = sha:123456789
    company_mail = dynobo@dynobo.corp
```

... then you can use those variables in the hook:

```yaml
- repo: https://github.com/dynobo/sign-off
    rev: v0.1.0
    hooks:
      - id: sign-off
      - args:
        - '--template=\n\nBy: <my-signature.company_mail> (<my-signature.company_mail>)'
        - '--skip-containing=\nBy: '
```
