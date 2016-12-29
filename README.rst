sphinxcontrib-toc
=================

``sphinxcontrib-toc`` is a Sphinx extension to allow .toc file to build
the Table of Contents.

This extension empower you to build complicated document with markup
languages which can not define toctrees.  Specifically, combination with
recommonmark, you don't need to write any reStructuredText in your document!

Usage
-----

Append this extension in conf.py::

    extensions = ['sphinxcontrib.toc']


And configure following settings:

``toc_title``
    The default title of toctree if no titles in .toc file.  By default,
    ``"{project} Documentation"``.

``toc_numbered``
    Same as ``:numbered:`` option of toctree directive.  If enabled,
    Sphinx assigns section numbers.  By default, ``true``.


.toc file
---------

.toc file is a list of documents like ``toctree`` directive::

   section1
   section2
   section3

You may define the title of toctree at top of the file::

   # The title of document
   section1
   section2
   section3


Tips
----

You can use "nested" .toc file like following::

   /index.toc
   /part1.rst
   /part2.rst
   /part3/index.toc
   /part3/section1.toc
   /part3/section2.toc

   # In /index.toc
   part1
   part2
   part3/index

   # In /part3/index.toc
   section1
   section2
