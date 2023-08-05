===============================
System Git
===============================

.. image:: https://img.shields.io/pypi/v/pysysgit.svg
        :target: https://pypi.python.org/pypi/pysysgit


Utility to call git from python. Examples::

  >>> from sysgit import *
  >>> res = git('ls-files')
  .editorconfig
  .gitignore
  AUTHORS.rst
  CONTRIBUTING.rst
  HISTORY.rst
  LICENSE
  MANIFEST.in
  README.rst
  docs/Makefile
  docs/authors.rst
  docs/conf.py
  docs/contributing.rst
  docs/history.rst
  docs/index.rst
  docs/installation.rst
  docs/make.bat
  docs/readme.rst
  docs/usage.rst
  requirements.txt
  setup.cfg
  setup.py
  sysgit/__init__.py
  tox.ini
  >>> print res
  0
  >>> res = git('ls-files', f=CHECK_OUTPUT)
  >>> print res
  .editorconfig
  .gitignore
  AUTHORS.rst
  CONTRIBUTING.rst
  HISTORY.rst
  LICENSE
  MANIFEST.in
  README.rst
  docs/Makefile
  docs/authors.rst
  docs/conf.py
  docs/contributing.rst
  docs/history.rst
  docs/index.rst
  docs/installation.rst
  docs/make.bat
  docs/readme.rst
  docs/usage.rst
  requirements.txt
  setup.cfg
  setup.py
  sysgit/__init__.py
  tox.ini

  >>> res = git('blah', f=CHECK_OUTPUT)
  git: 'blah' is not a git command. See 'git --help'.

  Did you mean this?
          blame
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "sysgit/__init__.py", line 79, in git
      return f(full_args, **full_kwargs)
    File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 573, in check_output
      raise CalledProcessError(retcode, cmd, output=output)
  subprocess.CalledProcessError: Command '('git', 'blah')' returned non-zero exit status 1

* Free software: BSD license
* Documentation: https://pysysgit.readthedocs.org.

Features
--------

* TODO




History
-------

0.1.0 (2015-01-11)
---------------------

* First release on PyPI.


