# -*- coding: utf-8 -*-

import slumber
from munch import Munch


class ReadTheDocsAPI(object):

    API_V2_URL = 'https://readthedocs.org/api/v2/'

    api = slumber.API(API_V2_URL)

    footer_html_endpoint = (
        API_V2_URL + 'footer_html/'
        '?project={project}&version={version}&format=json'
    )

    def __init__(self, project_slug):
        self.project_slug = project_slug
        response = Munch(self.api.project.get(slug=self.project_slug))
        self.project = Munch(response.results[0])

    def _get_footer_html_data(self, version):
        footer_html_data = Munch(self.api.footer_html().get(
            project=self.project.slug,
            version=version,
        ))
        footer_html_data.version_compare = Munch(footer_html_data.version_compare)
        return footer_html_data

    def is_highest_version(self, version):
        try:
            footer_html_data = self._get_footer_html_data(version)
            return footer_html_data.version_compare.is_highest
        except Exception:
            # if a 404 happens it means that we are trying to build a version
            # that doesn't exist yet in Read the Docs
            return True

    def newest_version(self):
        # TODO: use a proper API endpoint to get a specific version (slug) for a
        # Project (slug)
        footer_html_data = self._get_footer_html_data('latest')
        # newest_version_slug = footer_html_data.version_compare.version
        return Munch(
            url=footer_html_data.version_compare.url,
            slug=footer_html_data.version_compare.version,
        )
