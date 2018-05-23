# -*- coding: utf-8 -*-

from docutils import nodes
import os


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

    def get_banner_node(self):
        current_version = self._get_current_doc_version()
        newest_version = self._get_latest_doc_version()
        message = self._get_message(current_version)
        banner = self._create_banner_node(message, newest_version)
        return banner

    def _create_banner_node(self, message, newest_version, admonition_type='warning'):
        """
        Return an admonition node to be inserted in the document.

        :rtype: docutils.nodes.admonition
        """

        node_class = self.ADMONITION_TYPES.get(
            admonition_type,
            self.ADMONITION_TYPES.get(self._get_default_admonition_type()),
        )

        paragraph = nodes.paragraph()
        if self._get_message_placeholder() in message:
            first_msg_part, second_msg_part = message.split('{newest}')
            reference = nodes.reference(
                newest_version,
                newest_version,
                # TODO: get a proper uri here that points to the real version
                refuri='http://readthedocs.org',
            )
            paragraph.append(nodes.Text(first_msg_part))
            paragraph.append(reference)
            paragraph.append(nodes.Text(second_msg_part))
        else:
            paragraph.append(nodes.Text(message))

        banner_node = node_class()
        banner_node.append(paragraph)
        return banner_node

    def _get_message_placeholder(self):
        return self.app.config.versionwarning_message_placeholder

    def _get_default_admonition_type(self):
        return self.app.config.versionwarning_default_admonition_type

    def _get_current_doc_version(self):
        return self.app.config.version

    def _get_latest_doc_version(self):
        if USE_READTHEDOCS_API:
            pass
        else:
            return self._get_current_doc_version()

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
    app.connect('doctree-resolved', process_version_warning_banner)

    return {'version': '0.1'}
