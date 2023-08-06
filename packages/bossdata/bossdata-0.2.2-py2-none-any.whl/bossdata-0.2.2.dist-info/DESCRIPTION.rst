===============================
bossdata
===============================

.. image:: https://img.shields.io/travis/dkirkby/bossdata.svg
        :target: https://travis-ci.org/dkirkby/bossdata

.. image:: https://img.shields.io/pypi/v/bossdata.svg
        :target: https://pypi.python.org/pypi/bossdata

.. image:: https://readthedocs.org/projects/bossdata/badge/?version=latest
        :target: https://readthedocs.org/projects/bossdata/?badge=latest
        :alt: Documentation Status

Tools to access and work with SDSS BOSS data from http://dr12.sdss3.org.

* Free software: MIT license
* Documentation: https://bossdata.readthedocs.org
* Code: https://github.com/dkirkby/bossdata




History
-------

0.1.0 (2015-05-24)
------------------

* First release on PyPI.

0.2.0 (2015-06-09)
------------------

* Fix issues #3 #5 #6.
* Add support for accessing subtracted sky flux to the `spec` module and `bossplot` script.
* This version breaks backwards compatiblity with 0.1.0 since the previous `$BOSS_SAS_ROOT` environment variable is now named `$BOSS_SAS_PATH` and has the instrument name (usually `boss`) appended.
* bash users can update by replacing `export BOSS_SAS_ROOT=/sas/dr12` with `export BOSS_SAS_PATH=/sas/dr12/boss` in their `.bashrc` file.

0.2.1 (2015-06-13)
------------------

* Fix issues #9 #12 #13.

0.2.2 (2015-06-15)
------------------

* Really fix issues #9 #13.
* Add support for finding and fetching spFrame and spCFrame files (#17).


