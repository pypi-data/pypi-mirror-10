===============================
web.sh
===============================
.. image:: https://img.shields.io/travis/westurner/websh.svg
        :target: https://travis-ci.org/westurner/websh

.. image:: https://img.shields.io/pypi/v/websh.svg
        :target: https://pypi.python.org/pypi/websh

| Source: git https://github.com/westurner/web.sh

web.sh is a cross-platform script (web) and API for launching a browser
(with ``x-www-browser`` (Linux, Unix), ``open`` (OSX), ``start`` (Windows),
or ``python -m webbrowser``)

* Free software: BSD license

.. contents::


Features
--------

* Open the configured default system web browser with one or more
  paths or URIs
* Open to a relative path
* Open to an absolute path


Installation
--------------
Install the ``web`` (and ``x-www-browser-``) scripts:

.. code:: bash

   pip install web.sh
   pip install -e https://github.com/westurner/web.sh


Usage
-------

The ``web`` script commandline interface:

.. code:: bash

    web .
    web ./index.html
    web $WORKON_HOME/dotfiles/src/dotfiles/docs/_build/html/index.html
    web localhost:8082   #  pgs docs/_build/html  # pypi:pgs
    web https://westurner.org/dotfiles/
    web westurner.org/dotfiles github.com/westurner/dotfiles  # !HTTPS!
    x-www-browser- .

``web --help`` commandline help:

::

    Usage: web [-b|-x|-o|-s| <url1> [<url_n>]

    Open a webbrowser (default: detect sys.platform)

    Options:
    -h, --help           show this help message and exit
    -b, --webbrowser     Open with `python -m webbrowser`
    -x, --x-www-browser  Open with `x-www-browser`
    -o, --open           Open with `open`
    -s, --start          Open with `start `
    -v, --verbose
    -q, --quiet
    -t, --test

API
----
* Instances of ``websh.websh.WebBrowser`` implement ``open_new_tab()``
* ``websh.websh.WebBrowser.x_www_browser`` calls ``open_new_tab()``
  with a list of paths and/or URIs
* ``web <urls>`` calls ``websh.websh.WebBrowser.x_www_browser``
  to open new tabs for each path or URI:

  .. code:: python

      urls = (["https://westurner.org/dotfiles/",
               "https://github.com/westurner/dotfiles",
               "https://waffle.io/westurner/dotfiles"])
      output = list(WebBrowser.x_www_browser(urls))
      print(output)


Platform Notes
---------------
* OSX: ``web -o ./README.rst`` and ``web -b ./README.rst``
  open ``README.rst`` in the configured editor
  (not the configured system browser).

  Workarounds:

  * Specify the full path to a specific browser application followed
    by a quoted URI, for each URI in a newline-delimited list




History
-------

0.1.1 (2015-06-21)
---------------------

* DOC: README.rst: links, Features, Usage, API
* BLD: setup.py console_script entrypoint ``web = websh.web:main``
* BLD: setup.py console_script entrypoint ``x-www-browser- = websh.web:main``
* BUG,REF: websh.py: logging, logging config [07f9a0f]
* BUG,CLN,DOC,REF,TST: websh.py: match_domain, :PymodeLintAuto, argv, logging config [4b33395]
* ENH: websh.py: https://github.com/westurner/dotfiles/blob/master/scripts/web [29c0ca7]
* BLD,RLS: \*, setup.py, __init__.py: ``cookiecutter gh:audreyr/cookiecutter-pypackage`` [e288536]

0.1.2 (2015-06-21)
-------------------
* DOC: README.rst: API docs
* RLS: setup.py, __init__.py: ``__version__ = 0.1.2``
* First release on PyPI



