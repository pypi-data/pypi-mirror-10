=============
nagare-jquery
=============

A ``jQuery`` ``Nagare`` Renderer for async.


Usage
=====

.. code-block:: python

    from nagare import wsgi
    from nagare.contrib.jquery import wsgi


    class WSGIApp(wsgi.WSGIApp):
        """
        My custom WSGIApp must inherit from nagare-jquery
        """


Requirements
============

* Python 2.6+ with nagare latest
* Stackless Python 2.6+ with Nagare >= 0.4.1


License
=======

BSD


Running Tests
=============

.. code-block:: sh

    $ git clone https://github.com/Alzakath/nagare-jquery.git
    $ cd nagare-jquery
    $ nosetests -v


Changelog
=========

Dev
    *

v0.0.1
    * Initial release