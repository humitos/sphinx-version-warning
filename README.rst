|PyPI version| |Docs badge| |License|

sphinx-version-warning
======================

``sphinx-version-warning`` is a Sphinx extension that allows you to show a Warning banner at the top of your documentation.
By default, the banner is shown based on the version that is displayed compared (using SemVer_) with the latest version on the server.


Installation
------------

::

   pip install sphinx-version-warning


Configuration
-------------

Add this extension in your ``conf.py`` file as:

.. code-block:: python

   extensions = [
    # ... other extensions here

    'versionwarning.extension',
   ]


Documentation
-------------

Check out the full documentation at https://sphinx-version-warning.readthedocs.io/

.. _SemVer: https://semver.org/


.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-version-warning.svg
   :target: https://pypi.org/project/sphinx-version-warning
   :alt: Current PyPI version
.. |Docs badge| image:: https://readthedocs.org/projects/sphinx-version-warning/badge/?version=latest
   :target: https://sphinx-version-warning.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation status
.. |License| image:: https://img.shields.io/github/license/humitos/sphinx-version-warning.svg
   :target: LICENSE
   :alt: Repository license
