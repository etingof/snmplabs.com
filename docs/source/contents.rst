
Welcome to SNMP Laboratories
============================

.. toctree::
   :maxdepth: 2

We are a small hobby software development shop aiming at building
high-quality, free and open source tools primarily in the area of
network management and monitoring.

Our projects
------------

Our expertise and interests somehow revolve around
`SNMP <https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol>`_.
We mostly code our stuff in `Python <http://www.python.org>`_.
You will notice that momentarily!

SNMP Simulator
++++++++++++++

The `SNMP Agent Simulator <http://snmplabs.com/snmpsim>`_ tool pretends
to be a large network of SNMP-speaking devices. It aims at helping
fellow developers and QE people to model the environment their products
will work in once released out to the world.

SNMP Proxy Forwarder
++++++++++++++++++++

The alternative acronym for *SNMP* is *Security? Not My Problem!* The
`SNMP Proxy Forwarder <http://snmplabs.com/snmpfwd>`_ tool tries to
improve the security and usability of the SNMP technology in many ways.

For example it can shield your totally insecure SNMPv1 device from the
hostile network by putting this proxy tool in front of it and only
expose cryptographically sound SNMPv3 to the world.

.. _pysnmp:

SNMP library for Python
+++++++++++++++++++++++

The `pysnmp project <http://snmplabs.com/pysnmp/>`_ delivers the
fully-functional SNMP engine implementation in pure-Python.
It support reasonably advanced features such as SNMPv3 and IPv6,
can deal with MIB files and it is fully asynchronous internally.

.. _pysmi:

SNMP SMI compiler
+++++++++++++++++

With SNMP, the things you can tackle are formally expressed in the
`SMI <https://en.wikipedia.org/wiki/Structure_of_Management_Information>`_
language. The `SMI compiler <http://snmplabs.com/pysmi/>`_ can parse those
MIB files into Python code or JSON documents for further consumption by
:ref:`pysnmp <pysnmp>` or other automation tools.

ASN.1 types and codecs
++++++++++++++++++++++

`ASN.1 <https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One>`_
is essentially a data serialisation technology on steroids. Many
Internet, security and telecom protocols let alone data formats rely on
ASN.1.

The `pyasn1 <http://snmplabs.com/pyasn1/>`_ library deals with
ASN.1 data structures in pure Python.

Source code
-----------

Our projects source code is hosted at `GitHub <https://github.com/etingof/>`_.
Everyone is welcome to fork and contribute back!

License
-------

Our software is distributed under 2-clause BSD License.

.. toctree::
   :maxdepth: 2

   /license

Consulting services
-------------------

Run into a missing feature in our software and consider sponsoring its
implementation? Lose no time `getting in touch <mailto:etingof@gmail.com>`_!
Let's brew some free and open source software together!
