collective.complexrecordsproxy
==============================

Providing a proxy class for plone.registry allowing IObject fields to be stored as separate records using the plone.registry collection support.

Motivation
----------

With z3c.form it is possible to create forms allowing users to create and edit lists of complex records.

An example:

TODO from here.

We have a main interface with an object field etc.

We build a hierarchic structure composed of native types.
All boils down to simple native types in the end, and so in theory is possible to store in the registry without violating this principle of plone.registry:

"To avoid potentially
breaking the registry with persistent references to symbols that may go away,
we purposefully limit the number of fields supported.



Usage
-----

