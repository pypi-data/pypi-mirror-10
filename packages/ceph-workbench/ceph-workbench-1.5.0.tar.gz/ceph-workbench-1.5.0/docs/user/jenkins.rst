.. _jenkins:

Jenkins
=======

::

                        +----------------+
                        | commit pushed  |
                        |    in ceph     |
                        +----------------+
                                | (0)
                                v
                        +----------------+
            ssh tunnel  | jenkins master |   ssh tunnel
          +-------------| ceph job       |----------------+
          |    (1)      +----------------+                |
          |                                               |
          |                                               |
          v                                               v
     +----------+                                    +----------+
     | jenkins  |                                    | jenkins  |
     | slave    |                                    | slave    |
     | (docker) |                                    | (qemu)   |
     +----------+                                    +----------+
          |  |          (3)                               |
      (2) |  +-------------------------+              (3) |
          |                            |                  |
          v                            v                  v
     +-----------+             +--------------+   +--------------+
     | container |             | container    |   | qemu i386    |
     | centos 7  |             | ubuntu 14.04 |   | ubuntu 14.04 |
     +-----------+             +--------------+   +--------------+
          |                            |                  |
          v                            v                  |
     +-------------------+     +-------------------+      |
     | run-make-check.sh |     | run-make-check.sh |      |
     +-------------------+     +-------------------+      |
          |                            |                  v
          |                            |         +-------------------+
          |     +-----------------+    |         | run-make-check.sh |
          +---->|  jenkins master |<---+         +-------------------+
                |  ceph-report    |                       |
                |  job            |<----------------------+
                +-----------------+
                          |
                          | (4)
                          v


.. _`jenkins master`: http://jenkins.ceph.dachary.org/
.. _`jenkins job`: http://jenkins.ceph.dachary.org/job/ceph/
.. _`run-make-check.sh`: http://workbench.dachary.org/ceph/ceph/blob/master/run-make-check.sh
.. _`ceph repository`: http://workbench.dachary.org/ceph/ceph/

A `jenkins job`_ is triggered every time a commit is pushed to the
`ceph repository`_ and executes the `run-make-check.sh`_ script to
verify it compiles and passes unit and functional tests.

The `jenkins master`_ delegates the execution of `run-make-check.sh`_
to `jenkins slaves <http://jenkins.ceph.dachary.org/computer/>`_. If
the git branch matches a pull request found in the `Ceph official
repository <http://github.com/ceph/ceph/>`_, a comment is added when
the run is complete. When there is a failure the full output of the
script can be browsed to figure out what went wrong.

Jenkins slave CPU & RAM requirements
------------------------------------

The minimum configuration of a slave is:

- bare metal with 32GB RAM, SSD with 16GB free space, 8 cores OR
- virtual machine with 32GB RAM, 20GB root disk, 8 cores

It can be hosted on a private IP: it will initiate a tunnel to the
jenkins master.

Hosting a jenkins slave
-----------------------

In the simplest way to contribute a jenkins slave is when a jenkins
admin can ssh to it as root. If the slave is behind a firewall
hosting_private it :ref:`requires two more steps <hosting_private>`.

#. Add the following public key to the ``/root/.ssh/authorized_keys`` file
   of the machine hosting the jenkins slave.

   ::

      ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDA9mo/xFNhLSCADCjmPQ0MnlTdpIaC8O6vHT5/z7i0boZhLsTe84Gq6sg6qIQY/847/FX52wN6YxMYYjr4478eGa1n84L88WHA4updDT4/LbKzu3aYOVPD6NlkMGKmoJOQazY5z2Mpa/gYHDboZgyyLQ3ApSlM9SCc0xJIJwhGv4uAPjWDzkjCyMCjAOu0NPzJ97uuKgS7e5u1vxL3+6hn7HlIU9wSnA3PEmMUHC8p3f0sHnX5OeZcLwxOAD8v3Q74Lg7yNTc8K0wBuA/G32Tad2QZxFsuSkOyuvhQnWe7dqPL6Jvr20A9wu2A7WVbQ7YaxwngMjB26Pezxg4mFUYV ubuntu@jenkins
#. Send a mail to `Ceph Development
   <mailto:ceph-devel@vger.kernel.org>`_ with the IP of the machine

The jenkins admin will then do the following:

#. ssh -A ``root@slave.domain``
#. Create a jenkins user with a home at ``/home/jenkins``
#. Allow the jenkins user to use docker

   ::

       $ sudo usermod -aG docker jenkins

#. :ref:`Install <install>` ceph-workbench
#. Logout
#. ssh -A ``jenkins@slave.domain``
#. Create a new node on the jenkins master, create a jenkins slave container and connect it with the new node.

   ::

      $ ceph-workbench jenkins \
           --jenkins-url http://jenkins.ceph.dachary.org/ \
           --jenkins-user admin \
           --jenkins-password XXXXXXXX \
           --jenkins-ssh-host ubuntu@jenkins.ceph.dachary.org \
           --jenkins-docker-run-slave new
      slave940
#. Verify that the newly created node is connected and ready to run
   jobs at http://jenkins.ceph.dachary.org/computer/slave094/

.. _hosting_private:

Hosting a jenkins slave on a private IP
---------------------------------------

The process for hosting a jenkins slave requires more steps if the
hosted slave cannot be access from the net:

#. Send a mail to `Ceph Development
   <mailto:ceph-devel@vger.kernel.org>`_ with the configuration (RAM,
   disk, CPU) of the machine that could host a jenkins slave.
#. Wait for the following to be sent:
   - a ssh key
   - the name of the slave (for instance **slave904**)
#. Create a jenkins user with a home at ``/home/jenkins``
#. Allow the jenkins user to use docker

   ::

       sudo usermod -aG docker jenkins

#. :ref:`Install <install>` ceph-workbench
#. Login as jenkins
#. Add the ssh key to ``~/.ssh``
#. Connect to the jenkins master

   ::

      ceph-workbench jenkins \
         --jenkins-url http://jenkins.ceph.dachary.org/ \
         --jenkins-ssh-host ubuntu@jenkins.ceph.dachary.org \
         --jenkins-docker-run-slave slave904
