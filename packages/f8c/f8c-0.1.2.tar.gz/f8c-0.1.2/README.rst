f8c
======================

Provides a conventional cli entrypoint as a thin wrapper around
`flake8_codes <https://github.com/orsinium-labs/flake8-codes/tree/master/flake8_codes>`_ so that
I can install it with `pipx <https://pypa.github.io/pipx/>`_. That's it.

If you work in projects that use any flake8 plugins that provide new error
codes, you will need to install f8c in the local venv to introspect them.

Actually, you should probably just use flake8_codes as indicated in its README
and not use f8c at all.

Installation
------------

.. code-block :: console

    pip3 install f8c

Usage
-----

.. code-block :: console

    $ f8c w6
    pycodestyle          | W601     | .has_key() is deprecated, use 'in'
    pycodestyle          | W602     | deprecated form of raising exception
    pycodestyle          | W603     | '<>' is deprecated, use '!='
    pycodestyle          | W604     | backticks are deprecated, use 'repr()'
    pycodestyle          | W605     | invalid escape sequence '\%s'
    pycodestyle          | W606     | 'async' and 'await' are reserved keywords starting with Python 3.7
