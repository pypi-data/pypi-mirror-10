.. _docker: http://docker.com/
.. _dotCloud: http://dotcloud.com/
.. _hipache: https://github.com/hipache/hipache


hipachectl
==========

hipachectl is a command-line tool to manage `dotCloud`_'s `hipache`_
load balancer and reverse proxy. hipachectl lets you:

- list configured virtual hosts
- add a new virtual host
- delete a virtual host


Installation
------------

Either pull the prebuilt `Docker`_ image::

    $ docker pull prologic/hipachectl

Or install from the development repository::

    $ git clone https://github.com/prologic/hipachectl.git
    $ cd hipachectl
    $ pip install -r requirements.txt


Usage
-----

To use hipachectl from `Docker`_::

    $ docker run prologic/hipachectl -H <hipache_ip> <command>

Or::

    $ hipachectl -H <docker_ip> <command>

For help user the ``--help`` option.

Change Log
==========

0.2 (2015-05-26)
----------------

-  Moved project to `Github <https://github.com/prologic/hipachectl>`_

0.1 (2015-05-26)
----------------

-  Added an API

0.0.1 (2014-11-01)
------------------

-  Initial Release


