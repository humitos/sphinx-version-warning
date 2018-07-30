# -*- coding: utf-8 -*-

from docutils import nodes, core
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

        if self._message_placeholder in message:
            message = message.replace(self._message_placeholder, '`{text} <url>`_'.format(
                text=newest_version.slug,
                url=newest_version.url,
            ))
        paragraph = core.publish_doctree(message)[0]

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
        return (
            os.environ.get('READTHEDOCS_VERSION', None) or
            self.app.config.versionwarning_project_version or
            self.app.config.version
        )

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
