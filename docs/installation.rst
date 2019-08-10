Installation
============

Install the package

.. tabs::

   .. tab:: from PyPI

      .. prompt:: bash

         pip install sphinx-version-warning

   .. tab:: from GitHub

      .. prompt:: bash

         pip install git+https://github.com/humitos/sphinx-version-warning@master


Once you have the package installed,
you have to configure it on your Sphinx documentation.
To do this, add this extension to your Sphinx's extensions in the ``conf.py`` file.

.. code-block:: python

   # conf.py
   extensions = [
        # ... other extensions here
        'versionwarning.extension',
   ]


After installing the package and adding the extension in the ``conf.py`` file,
if you build the documentation of an old version on Read the Docs,
you will see a nice banner pointing to your latest release.

In case you want to show a customized banner in a specific version,
see :doc:`configuration` setting.
