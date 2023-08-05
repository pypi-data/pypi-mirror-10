.. _install:

Installation
============

This part of the documentation covers the installation of ceph-workbench.


Distribute & Pip
----------------

Installing ceph-workbench requires `pip <https://pip.pypa.io>`_::

    $ pip install ceph-workbench

or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_::

    $ easy_install ceph-workbench

But, you really `shouldn't do that <https://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`_.


Get the Code
------------

ceph-workbench is actively developed and the code is
`always available <http://workbench.dachary.org/dachary/ceph-workbench>`_.

You can clone the public repository::

    $ git clone http://workbench.dachary.org/dachary/ceph-workbench.git

Once you have a copy of the source install it into your site-packages::

    $ python setup.py install
