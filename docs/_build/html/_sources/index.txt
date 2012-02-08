.. controlchart documentation master file, created by
   sphinx-quickstart on Wed Feb  8 20:24:51 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Requests: HTTP for Humans
=========================

Release v\ |version|. (:ref:`Installation <install>`)

Controlchart is an :ref:`ISC Licensed <isc>` Control Chrat library, written in Python, for normal people.

Control charts are really useful tools to help you understand how 'in control your process is'
so you can help make management changes based on real information.

Control charts are really easy to create - read the code - but reading a control chart, and doing
the right thing is more important than writing the code. 

This is people's lives we're messing with :)

::
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> c = ControlChart(data)
    >>> c.mean = 5
    >>> c.lower_control_level = 2.339999999999999857891452848
    >>> c.upper_control_level = 7.660000000000000142108547152
    >>> c.to_json()
    >>> # TODO
    >>> c.to_python()
    >>> # TODO
    >>> c.to_flot()
    >>> # TODO
    >>> c.to_excel()
    >>> # TODO


Thanks
-------

**John Chaimberlain**
    All round systems thinking legend.

**Gino Franco**
    For bringing Systems Thinking to the masses.

**John Seddon**
    For applying uncommon sense to common practice.


User Guide
----------

This part of the documentation, which is mostly prose, begins with some
background information about Requests, then focuses on step-by-step
instructions for getting the most out of Requests.

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart
   user/advanced


Community Guide
-----------------

This part of the documentation, which is mostly prose, details the
Requests ecosystem and community.

.. toctree::
   :maxdepth: 2

   community/faq
   community/out-there.rst
   community/support
   community/updates

API Documentation
-----------------

If you are looking for information on a specific function, class or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


Developer Guide
---------------

If you want to contribute to the project, this part of the documentation is for
you.

.. toctree::
   :maxdepth: 2

   dev/internals
   dev/todo
   dev/authors