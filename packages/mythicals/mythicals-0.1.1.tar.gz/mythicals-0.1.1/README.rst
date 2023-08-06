=====
mythical
=====

.. image:: https://magnum.travis-ci.com/verygood/mythical.svg?token=token&branch=master
    :target: https://magnum.travis-ci.com/verygood/mythical

A fictitious processor used to perform online transactions:

- holds
- ...

and offline submissions:

- capture
- credit
- ...

against funding instruments:

- credit card
- bank account
- ...

and then simulate settlement. In addition it does:

- merchant provisioning

dev
===

Prep like:

.. code:: bash

   $ git clone git@github.com:verygood/mythical.git
   $ cd mythical
   $ mkvirtualenv mythical
   (mythical)$ pip install -e .[tests]
   (mythical)$ ./bin/mythicals db create -- -l i
   (mythical)$ ./bin/mythicals db schema -- upgrade head

then unit test:

.. code:: bash

   (mythical)$ PYTHONWARNINGS=error nosetests -svx --processes=4
   
and to integration test use `client <https://github.com/verygoodgroup/mythical-client>`_.

infra
=====

See `infra-vault <https://github.com/verygoodgroup/infra-vault>`_.

http
====

Implemented by ``mythicals.domain.*`` and exposed by:

- ``mythicals.commands.http``
- ``mythicals.http``

to these entry points:

- ``bin/mythicals http``
- ``bin/mythicald http``

sftp
====

Implemented by ``mythicals.domain.Company.mount`` and exposed by:

- ``mythicals.commands.sftp``
- ``mythicals.sftp``

to these entry points:

- ``bin/mythicals sftp``

shell
=====

.. code:: bash

   $ bin/mythicals shell
   
or to drop into a ``domain`` context:

.. code:: bash

   $ bin/mythicals shell -d
