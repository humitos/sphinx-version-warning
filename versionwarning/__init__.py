# -*- coding: utf-8 -*-

from docutils import nodes
import os

from munch import Munch

from .readthedocs import ReadTheDocsAPI


USE_READTHEDOCS_API = os.environ.get('USE_READTHEDOCS_API', False)


class VersionWarningBanner(object):

    ADMONITION_TYPES = {
        'warning': nodes.warning,
        'note': nodes.note,
        'admonition': nodes.admonition,
    }

    def __init__(self, app, doctree):
        self.app = app
        self.doctree = doctree
        self.api = self._get_api()


    def get_banner_node(self):
        current_version_slug = self._current_doc_version_slug
        newest_version = self._latest_doc_version
        message = self._get_message(current_version_slug)
        banner = self._create_banner_node(message, newest_version)
        return banner

    def _get_api(self):
        if USE_READTHEDOCS_API:
            return ReadTheDocsAPI(self._project_slug)

    def _create_banner_node(self, message, newest_version, admonition_type='warning'):
        """
        Return an admonition node to be inserted in the document.

        :rtype: docutils.nodes.admonition
        """

        node_class = self.ADMONITION_TYPES.get(
            admonition_type,
            self.ADMONITION_TYPES.get(self._default_admonition_type),
        )

        paragraph = nodes.paragraph()
        if self._message_placeholder in message:
            first_msg_part, second_msg_part = message.split('{newest}')
            reference = nodes.reference(
                newest_version.slug,
                newest_version.slug,
                refuri=newest_version.url,
            )
            paragraph.append(nodes.Text(first_msg_part))
            paragraph.append(reference)
            paragraph.append(nodes.Text(second_msg_part))
        else:
            paragraph.append(nodes.Text(message))

        banner_node = node_class()
        banner_node.append(paragraph)
        return banner_node

    @property
    def _project_slug(self):
        return self.app.config.versionwarning_project_slug

    @property
    def _message_placeholder(self):
        return self.app.config.versionwarning_message_placeholder

    @property
    def _default_admonition_type(self):
        return self.app.config.versionwarning_default_admonition_type

    @property
    def _current_doc_version_slug(self):
        return self.app.config.version

    @property
    def _latest_doc_version(self):
        if USE_READTHEDOCS_API:
            return self.api.newest_version()
        else:
            return Munch(
                url='.',
                slug=self._current_doc_version_slug,
            )

    def _get_message(self, version):
        return self.app.config.versionwarning_messages.get(
            version,
            self.app.config.versionwarning_default_message,
        )


def process_version_warning_banner(app, doctree, fromdocname):
    """
    Insert an ``admonition`` with a custom/general message.
    """

    banner = VersionWarningBanner(app, doctree)
    for document in doctree.traverse(nodes.document):
        banner = banner.get_banner_node()
        document.insert(0, banner)


def setup(app):
    default_message = 'You are not reading the most up to date version of this documentation. {newest} is the newest version.'

    app.add_config_value('versionwarning_enabled', False, 'html')
    app.add_config_value('versionwarning_message_placeholder', '{newest}', 'html')
    app.add_config_value('versionwarning_default_admonition_type', 'warning', 'html')
    app.add_config_value('versionwarning_default_message', default_message, 'html')
    app.add_config_value('versionwarning_messages', {}, 'html')
    app.add_config_value('versionwarning_project_slug', None, 'html')
    app.connect('doctree-resolved', process_version_warning_banner)

    return {'version': '0.1'}
