microarray-quantilenorm
=======================

|Build Status|

|Coverage Status|

Documentation
-------------

`microarray-quantilenorm
documentation <https://microarray-quantilenorm.readthedocs.org/en/latest/>`__

Description
~~~~~~~~~~~

This is an implementation of quantile normalization for microarray data
analysis.

Usage
~~~~~

.. code:: bash

        python quantile_normalization CSV

``microarray-quantilenorm`` will then do the following:

-  Output a list of expression values for genes of interest in each
   sample to stdout.
-  Create a PDF and PNG file graphing the distribution for each sample
   both before and after normalization.

Restrictions
~~~~~~~~~~~~

1.) Each CSV file must contain the same gene set.

2.) Each gene must be unique.

Example:

::

    > ABCD1 5.675
    > ABCD2 3.456
    > ABCD3 5.432

Requirements
~~~~~~~~~~~~

Matplotlib = 1.4.3

Scipy = 0.5.1

Installation
~~~~~~~~~~~~

``pip install microarray-quantilenorm``

.. |Build Status| image:: https://travis-ci.org/githubuser8392/microarray-quantilenorm.png?branch=develop
   :target: https://travis-ci.org/githubuser8392/microarray-quantilenorm
.. |Coverage Status| image:: https://coveralls.io/repos/githubuser8392/microarray-quantilenorm/badge.png?branch=develop
   :target: https://coveralls.io/r/githubuser8392/microarray-quantilenorm?branch=develop
