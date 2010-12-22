===================
collective.ATClamAV
===================

Introduction
------------

collective.ATClamAV aims at providing antivirus integration to plone sites. It does that by defining a validator that can be used with any content type that uses FileField(s). At the moment the open-source `Clam Antivirus <http://www.clamav.net/>`_  is supported. Clam Antivirus is available for all platforms.


Usage
-----

To start, you need to have *clamd* running on some host accessible by your instances. collective.ATClamAV supports either UNIX socket connections or remote connections. 

Install collective.ATClamAV and setup the host & port or the path to the clamd socket in the control panel (default is a network connection to *clamd* listening on *localhost* at port 3310). By default *Files* are going to be checked for viruses when added or updated.

Adding anti-virus protection to non-ATFile based content
--------------------------------------------------------
In order to add anti-virus protection to your custom content types you only need to add the *isVirusFree* validator to your FileField(s). For instance::

      FileField('file',
        validators = (('isNonEmptyFile', V_REQUIRED),
                      ('isVirusFree', V_REQUIRED),),
        widget = FileWidget(label=u'File'),
      )
  
Credits
-------
Some code was shamelessly borrowed from `pyClamd <http://xael.org/norman/python/pyclamd/>`_. 

