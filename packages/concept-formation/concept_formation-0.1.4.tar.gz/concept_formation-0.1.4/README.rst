=================
Concept Formation
=================

This is a Python library of algorithms that perform concept formation written by
Christopher MacLellan (http://www.christopia.net) and Erik Harpstead
(http://www.erikharpstead.net). 

Overview
========

In this library, the `COBWEB
<http://axon.cs.byu.edu/~martinez/classes/678/Papers/Fisher_Cobweb.pdf>`_ and
`COBWEB/3
<http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.97.4676&rep=rep1&type=pdf>`_
algorithms are implemented. These systems accept a stream of instances, which
are represented as dictionaries of attributes and values (where values can be
nominal for COBWEB and either numeric or nominal for COBWEB/3), and learns a
concept hierarchy. The resulting hierarchy can be used for clustering and
prediction.

This library also includes
`TRESTLE <http://christopia.net/data/articles/publications/maclellan1-2015.pdf>`_,
an extension of COBWEB and COBWEB/3 that support structured and relational data
objects. This system employs partial matching to rename new objects to align
with previous examples, then categorizes these renamed objects.

Lastly, we have extended the COBWEB/3 algorithm to support two key
improvements. First, COBWEB/3 now uses an `unbiased estimator
<https://en.wikipedia.org/wiki/Unbiased_estimation_of_standard_deviation>`_ to
calculate the standard deviation of numeric values. This is particularly useful
in situations where the number of available data points is low. Second,
COBWEB/3 supports online normalization of the continuous values, which is
useful in situations where numeric values are on different scales and helps to
ensure that numeric values do not impact the model more than nominal values.

Installation
============

You can install this software using pip::

    pip install -U concept_formation

You can install the latest version of the code directly from github::
    
    pip install -U git+https://github.com/cmaclell/concept_formation@master

Important Links
===============

- Source code: `<https://github.com/cmaclell/concept_formation>`_
- Documentation: `<http://concept-formation.readthedocs.org>`_

Fast Examples
=============

.. ipython::

    In [1]: from pprint import pprint
    In [2]: from concept_formation.trestle import TrestleTree
    In [3]: from concept_formation.cluster import cluster

    # Data is stored in a list of dictionaries where values can be either nominal,
    # numeric, component, or relational.
    In [4]: data = [{'f1': 'v1', #nominal value
       ...:          'f2': 2.6, #numeric value
       ...:          'f3': {'sub-feature1': 'v1'}, # component value
       ...:          'f4': {'sub-feature1': 'v1'}, # component value
       ...:          'f5': ['some-relation', 'f3', 'f4'] #relational value
       ...:         },
       ...:         {'f1': 'v1', #nominal value
       ...:          'f2': 2.8, #numeric value
       ...:          'f3': {'sub-feature1': 'v2'}, # component value
       ...:          'f4': {'sub-feature1': 'v1'}, # component value
       ...:          'f5': ['some-relation', 'f3', 'f4'] #relational value
       ...:         }]

    # Data can be clustered with a TrestleTree, which supports all data types or
    # with a specific tree (CobwebTree or Cobweb3Tree) that supports subsets of
    # datatypes (CobwebTree supports only Nominal and Cobweb3Tree supports only
    # nominal or numeric).
    In [5]: tree = TrestleTree()
    In [6]: tree.fit(data)

    # Trees can be printed in plaintext or exported in JSON format
    In [7]: print(tree)
    In [8]: pprint(tree.root.output_json())

    # Trees can also be used to predict missing attributes of new data points.
    In [9]: new = {'f2': 2.6, 'f3': {'sub-feature1': 'v1'}, 'f4': {'sub-feature1': 'v1'},
       ....:        'f5': ['some-relation', 'f3', 'f4']};
    In [10]: concept = tree.categorize(new)
    In [11]: print(concept.predict('f1'))

    # Or to get the probability of a particular attribute value
    In [12]: print(concept.get_probability('f1', 'v1'))

    # Trees can also be used to produce flat clusterings
    In [13]: new_tree = TrestleTree()
    In [14]: clustering = cluster(new_tree, data, minsplit=1, maxsplit=1)
    In [15]: print(clustering)

We have created a number of examples to demonstrate the basic functionality of
this library. The examples can be found 
`here <http://concept-formation.readthedocs.org>`_.  

Citing this Software 
====================

If you use this software in a scientific publiction, then we would appreciate
citation of the following paper:

MacLellan, C.J., Harpstead, E., Aleven, V., Koedinger, K.R. (2015) `TRESTLE:
Incremental Learning in Structured Domains using Partial Matching and
Categorization <http://christopia.net/data/articles/publications/maclellan1-2015.pdf>`_.
The Third Annual Conference on Advances in Cognitive Systems.
Atlanta, GA. May 28-31, 2015.

Bibtex entry::

    @inproceedings{trestle:2015a,
    author={MacLellan, C.J. and Harpstead, E. and Aleven, V. and Koedinger, K.R.},
    title={TRESTLE: Incremental Learning in Structured Domains using Partial
           Matching and Categorization.},
    booktitle = {The Annual Third Conference on Advances in Cognitive Systems},
    year={2015}
    }
