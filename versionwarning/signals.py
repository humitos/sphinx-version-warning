# -*- coding: utf-8 -*-

from docutils import nodes
import json
import os

from .banner import VersionWarningBanner

STATIC_PATH = os.path.join(os.path.dirname(__file__), '_static')


def process_version_warning_banner(app, doctree, fromdocname):
    """
    Insert an ``admonition`` with a custom/general message.
    """

    banner = VersionWarningBanner(app, doctree)
    for document in doctree.traverse(nodes.document):
        banner = banner.get_banner_node()
        if isinstance(banner, nodes.Admonition):
            document.insert(0, banner)


def generate_versionwarning_data_json(app, config):
    data = json.dumps({
        'meta': {
            'api_url': config.versionwarning_api_url,
        },
        'banner': {
            'html': config.versionwarning_banner_html,
            'id_div': config.versionwarning_banner_id_div,
            'body_default_selector': config.versionwarning_body_default_selector,
            'body_extra_selector': config.versionwarning_body_extra_selector,
        },
        'project': {
            'slug': config.versionwarning_project_slug,
        },
        'version': {
            'slug': config.version,
            'url': '.',
        },
    })

    data_path = os.path.join(STATIC_PATH, 'data')
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    with open(os.path.join(data_path, 'versionwarning-data.json'), 'w') as f:
        f.write(data)

    # Add the path where ``versionwarning-data.json`` file and
    # ``versionwarning.js`` are saved
    config.html_static_path.append(STATIC_PATH)
