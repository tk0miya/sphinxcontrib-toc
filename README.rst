sphinxcontrib-toc
=================

``sphinxcontrib-toc`` is a Sphinx extension to allow .toc file to build
the Table of Contents.

Usage
-----

Append this extension in conf.py::

    extensions = ['sphinxcontrib.toc']


And configure following settings:

``toc_title``
    The title of document.  By default, ``"{project} Documentation"``.

``toc_numbered``
    Same as ``:numbered:`` option of toctree directive.  If enabled,
    Sphinx assigns section numbers.  By default, ``true``.


.toc file
---------

.toc file is a list of documents like ``toctree`` directive::

   section1
   section2
   section3/part1
   section3/part2
   section3/part3
