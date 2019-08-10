Configuration
=============

Here is the list of configurations that you can change to make the banner behaves as you want.
You can customize these options in your ``conf.py`` file:

.. confval:: versionwarning_admonition_type

   Description: Admonition node type used to render the banner. ``warning``, ``admonition``, ``tip`` or ``note``.

   Default: ``'warning'``

   Type: string

.. confval:: versionwarning_banner_title

   Description: Title used in the banner.

   Default: ``'Warning'``

   Type: string

.. confval:: versionwarning_default_message

   Description: Default message shown in the banner.

   Default: ``'You are not reading the most up to date version of this documentation. {newest} is the newest version.'``

   Type: string

.. confval:: versionwarning_messages

   Description: Mapping between versions and a specific messages for its banners.

   Default: ``{}``

   Type: dict

.. confval:: versionwarning_message_placeholder

   Description: Text to be replaced by the version number link from the message

   Default: ``'newest'``

   Type: string

.. confval:: versionwarning_project_slug

   Description: Slug of the project under Read the Docs.

   Default: ``READTHEDOCS_PROJECT`` environment variable.

   Type: string

.. confval:: versionwarning_project_version

   Description: Slug of the version for the current documentation.

   Default: ``READTHEDOCS_VERSION`` environment variable.

   Type: string

.. confval:: versionwarning_api_url

   Description: API URL to retrieve all versions for this project.

   Default: ``https://readthedocs.org/api/v2/``

   Type: string

.. confval:: versionwarning_banner_html

   Description: HTML code used for the banner shown

   Default:

   .. code:: html

      <div id="{id_div}" class="admonition {admonition_type}">
        <p class="first admonition-title">{banner_title}</p>
        <p class="last">
          {message}
        </p>
      </div>

   Type: string


.. confval:: versionwarning_banner_id_div

   Description: HTML element ID used for the <div> inject as banner

   Default: ``version-warning-banner``

   Type: string

.. confval:: versionwarning_body_selector

   Description: jQuery selector to find the body element in the page and *prepend* the banner

   Default: ``div.body``

   Type: string
