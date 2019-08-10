Releasing a new version
=======================

These are the steps needed to release a new version:

#. Increment the version in ``versionwarning/__init__.py``
#. Increment the version in ``package.json``
#. Update the ``CHANGELOG.rst``
#. Update ``npm``::

     $ npm update

#. Compile assets::

     $ npm install
     $ ./node_modules/.bin/webpack

#. Commit the changes: ``git commit -m "Release $NEW_VERSION"``
#. Tag the release in git: ``git tag $NEW_VERSION``
#. Push the tag to GitHub: ``git push --tags origin``
#. Upload the package to PyPI::

     $ rm -rf dist/
     $ python setup.py sdist bdist_wheel
     $ twine upload dist/*
