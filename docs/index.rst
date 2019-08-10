Welcome to sphinx-version-warning!
==================================

``sphinx-version-warning`` is a Sphinx extension that allows you to show a Warning banner at the top of your documentation.
By default, the banner is shown based on the version that is displayed compared (using SemVer_) with the latest version on the server.


Online documentation:
    https://sphinx-version-warning.readthedocs.io/

Source code repository (and issue tracker):
    https://github.com/humitos/sphinx-version-warning/

Badges:
    |PyPI version| |Docs badge| |License|

Why do I need this extension?
-----------------------------

You *probably* don't.

Read the Docs `implements this feature by itself`_ adding a banner for you in old versions.

Although, comparing this extension with Read the Docs' core functionality,
``sphinx-version-warning`` allows the user to highly customize the banner by changing the message,
the style, the position, etc. which is not possible with Read the Docs feature.

The default settings behaves in the same manner that Read the Docs' core functionality,
so you will want to check out :doc:`configuration` for a better customization.

.. note::

   This extension was inspired by `this comment`_ on the Read the Docs issue tracker,
   where some discussions about what was missing from Read the Docs' feature took place.


How does it work?
-----------------

When visiting a page in Read the Docs that was built with this extension enabled,
an AJAX request is done to the `Read the Docs Public API`_ to retrieve all the **active versions** of the project.
These versions are compared against the one that the user is reading and if it's an old version,
a *warning banner* appears at the top of the page.


.. toctree::
   :maxdepth: 1
   :caption: Contents

   installation
   configuration
   get-involved
   who-is-using-it
   releasing

.. toctree::
   :maxdepth: 1
   :caption: API Reference

   autoapi/versionwarning/index

.. _SemVer: https://semver.org/
.. _Read the Docs Public API: https://docs.readthedocs.io/page/api/v2.html
.. _implements this feature by itself: https://docs.readthedocs.io/page/versions.html#version-warning
.. _this comment: https://github.com/readthedocs/readthedocs.org/issues/3481#issuecomment-378000845

.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-version-warning.svg
   :target: https://pypi.org/project/sphinx-version-warning
   :alt: Current PyPI version
.. |Docs badge| image:: https://readthedocs.org/projects/sphinx-version-warning/badge/?version=latest
   :target: https://sphinx-version-warning.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation status
.. |License| image:: https://img.shields.io/github/license/humitos/sphinx-version-warning.svg
   :target: LICENSE
   :alt: Repository license
