Fanstatic tools |Build Status|_
===============================

Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

.. |Build Status| image:: https://travis-ci.org/MiCHiLU/fanstatic-tools.png
.. _`Build Status`: http://travis-ci.org/MiCHiLU/fanstatic-tools

Shell Utilities
---------------
Fanstatic tools comes with a utility script called ``mkfanstaticsymlink``.
Please type ``mkfanstaticsymlink --help`` at the shell prompt to
know more about this tool.

::

  $ mkfanstaticsymlink
  make symlink fanstatic/angularjs to ../site-packages/js/angular/resources
  make symlink fanstatic/bootstrap to ../site-packages/js/bootstrap/resources
  make symlink fanstatic/jquery to ../site-packages/js/jquery/resources

  $ mkfanstaticsymlink --sys_path_appends=site-packages --versioning --versioning_use_md5 --base_url=static --publisher_signature=lib --dry-run
  make symlink static/lib/angularjs/+version+643d90594087d56cea34e2b460fc94f2 to ../../../site-packages/js/angular/resources
  make symlink static/lib/bootstrap/+version+94b615ca583b25c0374fac2f91e6a814 to ../../../site-packages/js/bootstrap/resources
  make symlink static/lib/jquery/+version+171ea6989058db3f1fa646d1292bb650 to ../../../site-packages/js/jquery/resources


Installation
------------
Installing from PyPI using ``pip``::

    pip install fanstatic-tools

Installing from PyPI using ``easy_install``::

    easy_install fanstatic-tools

Installing from source::

    python setup.py install


Dependencies
------------
1. Python 2.6, 2.7, 3.2+ or PyPy.
2. six_


Licensing
---------
Fanstatic tools is licensed under the terms of the `BSD 3-Clause`_.

Copyright 2012 ENDOH takanao.

Project `source code`_ is available at Github. Please report bugs and file
enhancement requests at the `issue tracker`_.


.. links:
.. _six: http://pypi.python.org/pypi/six
.. _BSD 3-Clause: http://opensource.org/licenses/BSD-3-Clause
.. _issue tracker: http://github.com/MiCHiLU/fanstatic-tools/issues
.. _source code: http://github.com/MiCHiLU/fanstatic-tools
