=======
Segpy 2
=======

Segpy is open source software created by Sixty North and licensed under the GNU Affero General Public License.

Status
======

Build status:

.. image:: https://travis-ci.org/sixty-north/segpy.svg?branch=master
    :target: https://travis-ci.org/sixty-north/segpy

Segpy is alpha software but is usable in its current form.  That said you should expect minor breaking API changes
between now and official release of a Segpy 2.

What is Segpy?
==============

The SEG Y file format is one of several standards developed by the Society of Exploration Geophysicists for storing
geophysical seismic data. It is an open standard, and is controlled by the SEG Technical Standards Committee, a
non-profit organization.

This project aims to implement an open SEG Y module in Python for transporting seismic data between SEG Y files and
Python data structures in pure Python.


Contributing
============

The easiest way to contribute is to use Segpy submit reports for defects or any other issues you come across.  It's our
intention to open up Segpy for contributions once we have achieved a stable API and architecture.  This time is close,
but in the interim we are won't be merging pull-requests until we have our ducks in a row.


Segpy Versions
==============

Segpy 2.0 is a complete re-imagining of a SEG Y reader in Python and represents a complete break from any and all older
versions of Segpy.  No attempt has been made to maintain API compatibility with earlier versions of Segpy and no code is
shared across versions.  Although earlier versions of Segpy were open source, they were never 'released' as such.
Earlier versions of Segpy are deprecated and completely unsupported.
