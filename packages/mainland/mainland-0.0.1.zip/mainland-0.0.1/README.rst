.. Copyright (c) Moshe Zadka
   See LICENSE for details.

mainland
--------

The main() for your scripts

.. image:: https://travis-ci.org/moshez/mainland.svg?branch=master
    :target: https://travis-ci.org/moshez/mainland

.. image:: https://readthedocs.org/projects/mainland/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://readthedocs.org/projects/mainland/

Hacking
=======

  $ tox

Should DTRT -- if it passes, it means
unit tests are passing, and 100% coverage.

Release
========

* admin/release <next version number>
* gpg --use-agent -u zadka.moshe@gmail.com --detach-sign --armor dist/*.whl
* gpg --use-agent -u zadka.moshe@gmail.com --detach-sign --armor dist/*.zip
* admin/upload

Contributors
=============

Moshe Zadka <zadka.moshe@gmail.com>

License
=======

MIT License
