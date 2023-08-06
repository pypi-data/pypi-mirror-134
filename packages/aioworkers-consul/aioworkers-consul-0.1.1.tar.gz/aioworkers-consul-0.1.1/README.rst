aioworkers-consul
=================

.. image:: https://img.shields.io/pypi/v/aioworkers-consul.svg
  :target: https://pypi.org/project/aioworkers-consul
  :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-consul.svg
  :target: https://pypi.org/project/aioworkers-consul
  :alt: Python versions

About
=====

Integration with `Hashicorp Consul <https://www.consul.io>`_.

Use
---

.. code-block:: yaml

    consul:
      host: localhost:8500  # optional
      service:              # optional
        name: my
        tags:
          - worker


Development
-----------

Install dev requirements:


.. code-block:: shell

    poetry install


Run linters:

.. code-block:: shell

    make
