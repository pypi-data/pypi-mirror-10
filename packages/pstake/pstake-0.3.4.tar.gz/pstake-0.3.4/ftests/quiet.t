Suppress all message output::

  $ rm -f sample.*
  $ if [ ! -a sample.png ]; then echo "Good, no file"; fi
  Good, no file
  $ pstake ${SRCDIR}/example/sample.tex -t png -q
  $ if [ -a sample.png ]; then echo "Good, file created"; fi
  Good, file created

.. vim: set ft=rst:
