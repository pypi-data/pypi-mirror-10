Markdown2PDF
============

Markdown2pdf is a command-line tool to convert markdown file into pdf,
was originally designed for myself to create resume.


Installation
------------

To install Markdown2PDF you may need to install PDF convertion tool first,

Install Markdown2PDF by pip:

.. code-block:: shell

    pip install markdown2pdf


Usage
-----

You can use Markdown2PDF via simple command ``md2pdf``:

.. code-block:: shell

    md2pdf resume.md

You can also appoint a theme by argument ``--theme``:

.. code-block:: shell

    md2pdf resume.md --theme=github

By now, GitHub flavoured theme is the only supported.


Trouble shooting
----------------

1. ``ffi.h no such file or directory``

.. code-block:: shell

    apt-get install libffi-dev
