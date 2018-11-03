1.1.2
-----

:Date: 2018-11-03

  * Load JSON file in all the pages properly (https://github.com/humitos/sphinx-version-warning/pull/20)

1.1.1
-----

:Date: 2018-10-31

  * Fix calling to ``coerce`` by ``semver.coerce``

1.1.0
-----

:Date: 2018-10-31

  * Support semver prefixed with ``v``, like ``v2.0.5`` (https://github.com/humitos/sphinx-version-warning/pull/16)

1.0.2
-----

:Date: 2018-10-22

  * Fix a mistake when releasing

1.0.1
-----

:Date: 2018-10-22

  * Fix compatibility between Sphinx 1.7 and Sphinx 1.8


1.0.0
-----

:Date: 2018-10-21

  * Remove ability to add the warning banner statically

  * Make the banner more customizable (all the configs are included in the ``json`` file generated and available from Javascript)

  * Rename ``versionwarning_default_admonition_type`` by ``versionwarning_admonition_type``

  * Rename ``versionwarning_body_default_selector`` by ``versionwarning_body_selector``

  * Remove ``versionwarning_body_extra_selector``

  * Refactor the code to avoid potential circular imports

  * Filter Read the Docs versions by ``active=True`` when retrieving versions


0.2.0
-----

:Date: 2018-07-30

  * Use ``READTHEDOCS_PROJECT`` and ``READTHEDOCS_VERSION`` environment variables

  * Remove ``versionwarning_enabled`` config since it wasn't used and it's not necessary

  * Parse ``versionwarning_messages`` as reStructuredText (https://github.com/humitos/sphinx-version-warning/pull/7)

0.1.0
-----

:Date: 2018-07-29

 * Make banner more configurable (https://github.com/humitos/sphinx-version-warning/pull/6).
   New configs (api_url, banner_html, banner_id_div, body_default_selector, body_extra_selector) were added.

 * Compatibility with Sphinx 1.7.x added

0.0.1
-----

:Date: 2018-07-27

* Initial release
