.. vim: set fileencoding=utf-8 :
.. Manuel Guenther <manuel.guenther@idiap.ch>
.. Mon Nov 10 18:45:01 CET 2014

==========
Python API
==========

.. note::

  If this section is empty, please go to the console and type:

  .. code-block:: sh

     $ ./bin/sphinx-build doc sphinx

  again, after you have successfully patched the CSU code.

LRPCA
-----

.. autosummary::
   bob.bio.csu.preprocessor.LRPCA
   bob.bio.csu.extractor.LRPCA
   bob.bio.csu.algorithm.LRPCA

LDA-IR
------

.. autosummary::
   bob.bio.csu.preprocessor.LDAIR
   bob.bio.csu.extractor.LDAIR
   bob.bio.csu.algorithm.LDAIR

Details
-------

Generic functions
+++++++++++++++++
.. automodule:: bob.bio.csu

Preprocessors
+++++++++++++
.. automodule:: bob.bio.csu.preprocessor

Extractors
++++++++++
.. automodule:: bob.bio.csu.extractor

Algorithms
++++++++++
.. automodule:: bob.bio.csu.algorithm

.. include:: links.rst
