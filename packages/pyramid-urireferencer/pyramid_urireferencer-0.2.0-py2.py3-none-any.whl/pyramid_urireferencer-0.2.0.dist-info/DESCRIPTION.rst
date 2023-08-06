pyramid_urireferencer
=====================

This plugin for pyramid helps in handling references to resources in other
applications by allowing querying on references to certain URI's.


.. image:: https://travis-ci.org/OnroerendErfgoed/pyramid_urireferencer.png?branch=master
        :target: https://travis-ci.org/OnroerendErfgoed/pyramid_urireferencer
.. image:: https://coveralls.io/repos/OnroerendErfgoed/pyramid_urireferencer/badge.png?branch=master
        :target: https://coveralls.io/r/OnroerendErfgoed/pyramid_urireferencer

.. image:: https://badge.fury.io/py/pyramid_urireferencer.png
        :target: http://badge.fury.io/py/pyramid_urireferencer

Please consult the documentatation for `UriRegistry
<http://uriregistry.readthedocs.org/en/latest/>`_ for more information on how
to use this library.


0.2.0 (2015-06-07)
------------------

- Changed ApplicationResponse.url to service_url.
- Cleaned up some documentation.
- Added an AbstractReferencer that has no implementation whatsoever.
- Make sure that the uri parameter is properly urlencoded.


0.1.0 (2015-05-21)
------------------

-  Initial version


