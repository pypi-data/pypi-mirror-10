****
HashFS
****

|version| |travis| |coveralls| |license|


A content-addressable file management system.


Links
=====

- Project: https://github.com/dgilland/hashfs
- Documentation: http://hashfs.readthedocs.org
- PyPI: https://pypi.python.org/pypi/hashfs/
- TravisCI: https://travis-ci.org/dgilland/hashfs


Quickstart
==========

Install using pip:


::

    pip install hashfs



For more details, please see the full documentation at http://hashfs.readthedocs.org.



.. |version| image:: http://img.shields.io/pypi/v/hashfs.svg?style=flat-square
    :target: https://pypi.python.org/pypi/hashfs/

.. |travis| image:: http://img.shields.io/travis/dgilland/hashfs/master.svg?style=flat-square
    :target: https://travis-ci.org/dgilland/hashfs

.. |coveralls| image:: http://img.shields.io/coveralls/dgilland/hashfs/master.svg?style=flat-square
    :target: https://coveralls.io/r/dgilland/hashfs

.. |license| image:: http://img.shields.io/pypi/l/hashfs.svg?style=flat-square
    :target: https://pypi.python.org/pypi/hashfs/

Changelog
=========


v0.0.1 (2015-05-27)
-------------------

- First release.
- Add ``HashFS`` class.
- Add ``HashFS.put`` method that saves a file path or file-like object by content hash.
- Add ``HashFS.files`` method that returns all files under root directory.
- Add ``HashFS.exists`` which checks either a file hash or file path for existence.


