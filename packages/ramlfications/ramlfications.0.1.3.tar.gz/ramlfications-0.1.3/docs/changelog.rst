Changelog
=========


0.1.3 (2015-05-14)
------------------

Added:

- New ``#ramlfications`` channel on `freenode`_ (web chat link)! Come chat, I'm lonely.
- Documentation for configuration and the ``update`` command.

Fixed:

- Handle recursive/cyclical ``!includes`` in RAML files for now (`PR`_)
- Encoding issues from upgrading to tox 2.0
- ``tests/test_utils.py`` would create ``ramlfications/data/supported_mime_types.json``; now mocked out.

0.1.2 (2015-04-21)
------------------

Fixed:

- pypy 2.5.x would fail a parser test because order of list was not expected

0.1.1 (2015-04-21)
------------------

New:

- Added ability to parse IANA-supported MIME media types
- Added ``update`` command for user to update IANA-supported MIME types if/when needed

0.1.0a1 (2015-04-18)
--------------------
Initial alpha release of ``ramlfications``\!


.. _`PR`: https://github.com/spotify/ramlfications/pull/8
.. _`freenode`: http://webchat.freenode.net?channels=%23ramlfications&uio=ND10cnVlJjk9dHJ1ZQb4
