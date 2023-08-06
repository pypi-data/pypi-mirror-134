====================
Mimetypes Extensions
====================

.. raw:: html

  <p align="center">
    <a href="https://pypi.org/project/mimetypes_extensions/">
      <img src="https://img.shields.io/pypi/pyversions/mimetypes_extensions" alt="Supported versions"/>
    </a>
    <a href="https://pypi.org/project/mimetypes_extensions/">
      <img src="https://img.shields.io/pypi/v/mimetypes_extensions" alt="PyPI Package latest release"/>
    </a>
    <a href="https://github.com/ThScheeve/mimetypes_extensions/blob/main/LICENSE">
      <img src="https://img.shields.io/pypi/l/mimetypes_extensions" alt="License"/>
    </a>
  </p>
  <p align="center">
    <a href="https://github.com/ThScheeve/mimetypes_extensions/issues/">
      <img src="https://img.shields.io/github/issues-raw/ThScheeve/mimetypes_extensions" alt="Open issues"/>
    </a>
    <a href="https://github.com/ThScheeve/mimetypes_extensions/issues">
      <img src="https://img.shields.io/github/issues-closed-raw/ThScheeve/mimetypes_extensions" alt="Closed issues"/>
    </a>
  </p>

Overview
========

The ``mimetypes_extensions`` module enables experimentation with features that
are not found in the ``mimetypes`` module.

Included Items
==============

This module currently contains the following:

- Experimental features

  - ``MimeTypes.get_all_extensions()``
  - ``get_all_extensions()``
  - ``image_file_extensions``
  - ``audio_file_extensions``
  - ``video_file_extensions``

Running Tests
=============
To run tests, run ``test_mimetypes_extensions.py``. You will also need to install
the latest version of ``mimetypes`` if you are using a version of Python that
does not include ``mimetypes`` as a part of the standard library.