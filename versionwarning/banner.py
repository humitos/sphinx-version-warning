# -*- coding: utf-8 -*-

from docutils import nodes
from munch import Munch
import os

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

        if (
            (
                (USE_READTHEDOCS_API and self.api.is_highest_version(self._current_doc_version_slug)) or
                newest_version.slug == self._current_doc_version_slug
            ) and self._current_doc_version_slug not in self.app.config.versionwarning_messages
        ):
            return None

        node_class = self.ADMONITION_TYPES.get(
            admonition_type,
            self.ADMONITION_TYPES.get(self._default_admonition_type),
        )

        paragraph = nodes.paragraph()
        if self._message_placeholder in message:
            first_msg_part, second_msg_part = message.split(self._message_placeholder)
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

        banner_node = node_class(ids=[self._banner_id_div])
        banner_node.append(paragraph)
        return banner_node

    @property
    def _banner_id_div(self):
        return self.app.config.versionwarning_banner_id_div

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
