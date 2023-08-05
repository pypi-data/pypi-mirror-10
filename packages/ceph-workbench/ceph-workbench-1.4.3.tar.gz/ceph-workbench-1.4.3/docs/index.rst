ceph-workbench
==============

Quick link to :ref:`the installation guide <install>`.

ceph-workbench is a :ref:`GPLv3+ Licensed <gplv3>` command line tool
that implements a development workflow for `Ceph <http://ceph.com>`_.
::
    $ sudo pip install ceph-workbench
    $ ceph-workbench --help
    usage: ceph-workbench [-h] [-v] [--libdir LIBDIR] 

    development workflow for Ceph

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         be more verbose
      --libdir LIBDIR       directory containing helpers programs
      --datadir DATADIR     directory for persistent data

    subcommands:
      valid subcommands

      {github2gitlab,backport,jenkins}
                            sub-command -h
        github2gitlab       Mirror a GitHub project to GitLab
        backport            Backport reports
        jenkins             Drive and inspect the Jenkins building Ceph

User Guide
----------

This part of the documentation, which is mostly prose, begins with some
background information about ceph-workbench, then focuses on step-by-step
instructions for getting the most out of ceph-workbench.

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/jenkins


Contributor Guide
-----------------

If you want to contribute to the project, this part of the documentation is for
you.

.. toctree::
   :maxdepth: 1

   dev/philosophy
   dev/authors
