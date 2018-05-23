# -*- coding: utf-8 -*-

import slumber
from munch import Munch


class APIObject(object):
    """
    Convert any API object into a Python object.
    """

    def __init__(self, obj):
        # TODO: iterate over the object and convert each dictionary into a Munch
        # instance
        pass


class ReadTheDocsAPI(object):

    api = slumber.API('https://readthedocs.org/api/v2/')

    # TODO: remove all the usage of the APIv1
    api_v1 = slumber.API('https://readthedocs.org/api/v1/')

    footer_html_endpoint = (
        'https://readthedocs.org/api/v2/footer_html/'
        '?project={project}&version={version}&format=json'
    )

    def __init__(self, project_slug):
        # self.project_slug = project_slug

        # TODO: use APIv2 here
        # project_data = self.api_v1.project.get(slug=project_slug)
        # self.project = Munch(project_data['objects'][0])
        self.project = Munch(self.api_v1.project(project_slug).get())
        # self.project = self.api.project.get(slug=self.project_slug)

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
