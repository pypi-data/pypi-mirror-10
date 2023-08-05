=============================
mezzanine-buffer
=============================

.. image:: https://badge.fury.io/py/mezzanine-buffer.png
    :target: https://badge.fury.io/py/mezzanine-buffer

.. image:: https://travis-ci.org/caffodian/mezzanine-buffer.png?branch=master
    :target: https://travis-ci.org/caffodian/mezzanine-buffer

.. image:: https://coveralls.io/repos/caffodian/mezzanine-buffer/badge.png?branch=master
    :target: https://coveralls.io/r/caffodian/mezzanine-buffer?branch=master

Buffer integration for Mezzanine CMS

Documentation
-------------

The full documentation is at https://mezzanine-buffer.readthedocs.org.

Quickstart
----------

This assumes you already have a Mezzanine_ install.

.. _Mezzanine: http://mezzanine.jupo.org

Install mezzanine-buffer::

    pip install mezzanine-buffer  --process-dependency-links

Unfortunately, the process-dependency-links is required until buffer-python is updated on pypi.

Then use it in a project:

- Add the following to your installed_apps::

    "mezzanine_buffer"

- Create a Buffer_ account (if you don't have one already)

.. _Buffer: http://buffer.com

- Create a `Buffer App`_ for your Mezzanine site.  You will receive an email with your client key, client secret,
 and access token
.. _Buffer App: https://buffer.com/developers/apps/create

- Enter your client key, client secret, and access token into your Mezzanine site settings.

Features
--------

- Adds a list of your Buffer profiles to the status section of any `Displayable` admin.
- If the publish_date of `Displayable` is in the future, it will be scheduled for that time.

TODO
----

- tests
- proper multi-profile support (buffpy doesn't support it)
- error handling (max 10 updates per profile, rate limits etc)