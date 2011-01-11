collective.ATClamAV
===================

Introduction
------------

``collective.ATClamAV`` aims at providing antivirus integration to Plone
sites. It does that by defining a validator that can be used with any content
type that uses File or Image field(s). The open-source `Clam Antivirus`_  is
supported which is available for all platforms.

Usage
-----

To start, you need to have ``clamd`` running on some host accessible by your
instances. ``collective.ATClamAV`` supports either UNIX socket connections or
remote connections.

Install collective.ATClamAV and setup the host & port or the path to the
``clamd`` socket in the control panel (default is a network connection to
``clamd`` listening on *localhost* at port 3310). By default *Files* and
*Images* are going to be checked for viruses when added or updated.

Adding anti-virus protection to non-ATFile based content
--------------------------------------------------------
In order to add anti-virus protection to your custom content types you only
need to add the *isVirusFree* validator to your FileField(s). For instance:

::

      FileField('file',
        validators = (('isNonEmptyFile', V_REQUIRED),
                      ('isVirusFree', V_REQUIRED),),
        widget = FileWidget(label=u'File'),
      )

Testing
-------
By default tests mock ``clamd`` and do not require it being installed. If you
want to test your ``clamd`` setup as well, run tests on all levels i.e.

::

  ./bin/test -a2

using the provided buildout. Two ``plone.app.testing`` layers (with the mocker
and without) are provided if you want to integrate the package in your own
tests, see ``testing.py``.

Development
-----------
If you want to get involved with the development of collective.ATClamAV please
use `github`_ to submit your patches/issues.

Credits
-------
Some code was shamelessly borrowed from `pyClamd`_.

.. _Clam Antivirus: http://www.clamav.net
.. _github: https://github.com/ggozad/collective.ATClamAV
.. _pyClamd: http://xael.org/norman/python/pyclamd
