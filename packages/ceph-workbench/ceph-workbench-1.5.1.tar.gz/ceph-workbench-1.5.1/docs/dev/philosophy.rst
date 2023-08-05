Development Philosophy
======================

ceph-workbench is a command line tool that implements a development
workflow for `Ceph <http://ceph.com>`_. All its functionalities are
tested (integration and unit tested) by running tox. It relies on
containers running redmine, gitlab, jenkins, etc. instances that are
spawned for the purpose of the tests and shutdown afterwards.

A new functionality is first developped as a set of manually run
snippets and tools, outside of ceph-workbench. Once it prooved useful
a few times, it is implemented and tested. This helps fighting the
temptation of overengineering a process that does not need to be.

ceph-workbench does not claim to be useful to all developers working
on Ceph and will never do. Trying to address all the workflows would
only succeed in creating something bloated and unmaintained.
