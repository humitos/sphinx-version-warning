# -*- coding: utf-8 -*-

from docutils import nodes


def process_version_warning_banner(app, doctree, fromdocname):
    """
    Insert an ``admonition`` with a custom/general message.
    """

    # TODO: make this a conf
    admonition_type = 'WARNING'

    for document in doctree.traverse(nodes.document):
        # paragraph = nodes.paragraph()
        # TODO: get the current version being built and insert the message from the
        # ``versionwarning_messages`` conf. If there is no specific message for this
        # version, check if not the latest stable using the Read the Docs API and
        # use the ``default`` keyword.
        # paragraph += nodes.Text('Holo Mundo')
        warning = nodes.warning()
        # title = nodes.title()
        # title += nodes.Text('Warning!')
        paragraph = nodes.paragraph()
        paragraph += nodes.Text('Hey you!')
        warning += paragraph
        # section += paragraph
        document.insert(0, warning)

        # TODO: create a reference (link) to the version and insert it as a node
        # content.append(paragraph)

        # TODO: we don't need to ``replace_self`` but to add a sibling node to it
        # document.replace_self(content)
        # import pdb; pdb.set_trace()


def setup(app):
    app.add_config_value('versionwarning_enabled', False, 'html')
    app.add_config_value('versionwarning_messages', {}, 'html')
    app.connect('doctree-resolved', process_version_warning_banner)

    return {'version': '0.1'}
