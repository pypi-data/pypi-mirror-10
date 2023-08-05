If we specify a temporary directory with ``--tempdir``, the ``-k`` option
should also be used to prevent the temporary directory from being deleted.  It
is useful to debugging.

::

  $ rm -rf tempdir/
  $ if [ ! -a tempdir ]; then echo "Good, no directory"; fi
  Good, no directory
  $ mkdir -p tempdir/
  $ pstake ${SRCDIR}/example/sample.tex --tempdir mytmp/ -k > /dev/null 2>&1
  $ if [ -a tempdir ]; then echo "Good, we still have the directory"; fi
  Good, we still have the directory

The ``-k`` option itself can work alone::

  $ pstake ${SRCDIR}/example/sample.tex -k > /dev/null 2>&1

.. vim: set ft=rst:
