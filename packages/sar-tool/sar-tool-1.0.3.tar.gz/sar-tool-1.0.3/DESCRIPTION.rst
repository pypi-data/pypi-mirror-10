Description
===========

|PyPI version| |PyPI downloads| |GitHub license|

sar.py is a simple search and replace script that outputs a valid
``diff`` file for review and later apply with ``patch``.

Installation
============

``$ pip install sar-tool``

Usage
=====

``$ sar unified_diff megasuper_diff sar.py``

::

    Searching for 'unified_diff' and replacing to 'megasuper_diff'

    Processing file sar.py ... MATCH FOUND
    Index: sar.py
    ================================================================================
    --- sar.py (original)
    +++ sar.py (modified)
    @@ -88,7 +88,7 @@
                 debug("MATCH FOUND\n")
                 print "Index:", filename
                 print "=" * 80
    -            diff = ''.join(list(difflib.unified_diff(orig.splitlines(1),
    +            diff = ''.join(list(difflib.megasuper_diff(orig.splitlines(1),
                                                          res.splitlines(1),
                                                          filename + " (original)",
                                                          filename + " (modified)")))

Licence
=======

This script is released under the MIT licence

.. |PyPI version| image:: https://img.shields.io/pypi/v/sar-tool.svg
   :target: https://pypi.python.org/pypi/sar-tool
.. |PyPI downloads| image:: https://img.shields.io/pypi/dm/sar-tool.svg
   :target: https://pypi.python.org/pypi/sar-tool#downloads
.. |GitHub license| image:: https://img.shields.io/github/license/mashape/apistatus.svg
   :target: 
