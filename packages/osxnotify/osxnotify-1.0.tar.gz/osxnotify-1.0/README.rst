osxnotify
=========

No nonsense OS X notifications for Python scripts (native wrapper).

About
-----

osxnotify is a wrapper for libosxnotify_. It allows Python scripts to display
native OS X notifications.

This module uses a native C extension to interface *libosxnotify*. For
CFFI-based module see `osxnotify-cffi`_.

Requirements
------------

* OS X >= 10.9.4 - should work on Mountain Lion but it's not tested,
* Python 2.7 (for Python 3.4+ see `osxnotify-cffi`_),
* libosxnotify >= 1.0,
* Xcode and command line utilities.

Installation
------------

To install osxnotify from PyPI, issue the following command:

.. sourcecode:: console

    $ pip install osxnotify

Alternatively, you can install from the source code:

.. sourcecode:: console

    $ git clone https://github.com/tomekwojcik/osxnotify-python.git
    $ cd osxnotify-python
    $ python2.7 setup.py install

Usage
-----

.. sourcecode:: python

    import osxnotify

    osnotify.notify('Title', subtitle='Subtitle', informative_text='Informative text')

Issues and limitations
----------------------

UTF-8 is the only supported text encoding.

Project status
--------------

This project should be considered **beta**. Proceed with caution if you decide
to use osxnotify in production.

License
-------

osxnotify is licensed under MIT License.

Author
------

osxnotify was written by `Tomek Wójcik`_.

Source code and issues
----------------------

Source code is available on GitHub at: `tomekwojcik/osxnotify-python`_.

To file issue reports and feature requests use the project's issue tracker on
GitHub.

.. _libosxnotify: http://tomekwojcik.github.io/libosxnotify/
.. _osxnotify-cffi: https://pypi.python.org/pypi/osxnotify-cffi
.. _Tomek Wójcik: http://www.tomekwojcik.com/
.. _tomekwojcik/osxnotify-python: https://github.com/tomekwojcik/osxnotify-python
