=============================
Pipeline
=============================

.. image:: https://badge.fury.io/py/pipeline.png
    :target: https://badge.fury.io/py/pipeline

.. image:: https://travis-ci.org/mikewaters/pipeline.png?branch=master
    :target: https://travis-ci.org/mikewaters/pipeline

.. image:: https://coveralls.io/repos/mikewaters/pipeline/badge.png?branch=master
    :target: https://coveralls.io/r/mikewaters/pipeline?branch=master

Execution pipeline built on celery, packages as a django app.

Documentation
-------------

The full documentation is at https://pipeline.readthedocs.org.

Quickstart
----------

Install Pipeline::

    pip install pipeline

Then use it in a project::

    import pipeline

Features
--------

* TODO

Notes:
- Tasks return a taskResult for a reason; we need a awy to determine if the task has
been called in a chain with mutable or immutable signature. If mutable, then the
first param to the function will be the return value of the last function. We want to
capture this scenario to update internal state table with that result in order
to make it available to tasks without requiring a change to the task function signature.
In this way we can write task functions that do not need to be aware of it they are
being executed in a chain or not. In order to make it available, we will pop it off
in PipelineTask.__call__ and add it as an instance variable to the task.
(the ony way to do this is to look at the type of arg 0, and if it's the same type that
we ask tasks to return, then we know we are a mutable signature in a chain).
