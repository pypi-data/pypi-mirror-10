.. -*-mode: rst; encoding: utf-8-*-
   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
   >>>>>>>>>>>>>>>> IMPORTANT: READ THIS BEFORE EDITING! <<<<<<<<<<<<<<<<
   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
   Please keep each sentence on its own unwrapped line.
   It looks like crap in a text editor, but it has no effect on rendering, and it allows much more useful diffs.
   Thank you!

Copyright |(c)| 2014-2015 `Matt Bogosian`_ (|@posita|_).

.. |(c)| unicode:: u+a9
.. _`Matt Bogosian`: mailto:mtb19@columbia.edu?Subject=dimgx
.. |@posita| replace:: **@posita**
.. _`@posita`: https://github.com/posita

Please see the accompanying |LICENSE|_ (or |LICENSE.txt|_) file for rights and restrictions governing use of this software.
All rights not expressly waived or licensed are reserved.
If such a file did not accompany this software, then please contact the author before viewing or using this software in any capacity.

.. |LICENSE| replace:: ``LICENSE``
.. _`LICENSE`: LICENSE
.. |LICENSE.txt| replace:: ``LICENSE.txt``
.. _`LICENSE.txt`: LICENSE

``dimgx``
=========

.. image:: https://pypip.in/version/dimgx/badge.svg
   :target: https://pypi.python.org/pypi/dimgx/
   :alt: Latest Version

.. image:: https://readthedocs.org/projects/dimgx/badge/?version=v0.1.5
   :target: https://dimgx.readthedocs.org/en/v0.1.5/
   :alt: Documentation

.. image:: https://pypip.in/license/dimgx/badge.svg
   :target: http://opensource.org/licenses/MIT
   :alt: License

.. image:: https://pypip.in/py_versions/dimgx/badge.svg
   :target: https://pypi.python.org/pypi/dimgx/0.1.5
   :alt: Supported Python Versions

.. image:: https://pypip.in/implementation/dimgx/badge.svg
   :target: https://pypi.python.org/pypi/dimgx/0.1.5
   :alt: Supported Python Implementations

.. image:: https://pypip.in/status/dimgx/badge.svg
   :target: https://pypi.python.org/pypi/dimgx/0.1.5
   :alt: Development Stage

Status
------

.. image:: https://travis-ci.org/posita/py-dimgx.svg?branch=v0.1.5
   :target: https://travis-ci.org/posita/py-dimgx?branch=v0.1.5
   :alt: Build Status

.. image:: https://coveralls.io/repos/posita/py-dimgx/badge.svg?branch=v0.1.5
   :target: https://coveralls.io/r/posita/py-dimgx?branch=v0.1.5
   :alt: Coverage Status

Curious about integrating your project with the above services?
Jeff Knupp (|@jeffknupp|_) `describes how <http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/>`__.

.. |@jeffknupp| replace:: **@jeffknupp**
.. _`@jeffknupp`: https://github.com/jeffknupp

**TL;DR**
---------

``dimgx`` extracts and flattens `Docker <https://www.docker.com/whatisdocker/>`_ `image <https://docs.docker.com/terms/image/>`__ `layers <https://docs.docker.com/terms/layer/>`__:

::

  % dimgx
  usage:
  dimgx [options] [-l LAYER_SPEC] ... [-t PATH] IMAGE_SPEC
  dimgx -h # for help
  dimgx: error: too few arguments

..

::

  % dimgx nifty-box # show layers for "nifty-box[:latest]"
  IMAGE TAG               IMAGE ID        PARENT ID       CREATED         LAYER SIZE      VIRTUAL SIZE
  -                       3cb35ae859e7    -               16 days ago     125.1 MB        125.1 MB
  debian:jessie           41b730702607    3cb35ae859e7    16 days ago     0 Bytes         125.1 MB
  -                       60aa72e3db11    41b730702607    7 days ago      0 Bytes         125.1 MB
  -                       390ac3ff1e87    60aa72e3db11    6 days ago      1.7 kB          125.1 MB
  -                       fec4e64b2b57    390ac3ff1e87    6 days ago      9.4 MB          134.5 MB
  -                       51a39b466ad7    fec4e64b2b57    6 days ago      0 Bytes         134.5 MB
  nifty-box               0bb92bb75744    51a39b466ad7    4 days ago      1.7 kB          134.5 MB

..

::

  % dimgx -l 2:4 nifty-box # show only the second through fourth layers
  IMAGE TAG               IMAGE ID        PARENT ID       CREATED         LAYER SIZE      VIRTUAL SIZE
  debian:jessie           60aa72e3db11    41b730702607    7 days ago      0 Bytes         0 Bytes
  -                       390ac3ff1e87    60aa72e3db11    6 days ago      1.7 kB          1.7 kB
  -                       fec4e64b2b57    390ac3ff1e87    6 days ago      9.4 MB          9.4 MB

..

::

  % dimgx -l 2:4 -t nifty.tar nifty-box # extract them
  % du -h nifty.tar
  9.0M    nifty.tar

``dimgx`` is licensed under the `MIT License <http://opensource.org/licenses/MIT>`_.
Source code is `available on GitHub <https://github.com/posita/py-dimgx>`__.
See `the docs <https://dimgx.readthedocs.org/en/v0.1.5/>`__ for more information.

Issues
------

``dimgx`` does what I want, so I'm just maintaining it at this point.
If you find a bug, or want a feature, please `file an issue <https://github.com/posita/py-dimgx/issues>`__ (if it hasn't already been filed).
If you're willing and able, consider `contributing <https://dimgx.readthedocs.org/en/v0.1.5/submissions.html>`__.
