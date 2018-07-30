# -*- coding: utf-8 -*-

name = 'versionwarning'
version = '0.1.0'


def setup(app):
    import sphinx
    from .signals import process_version_warning_banner, generate_versionwarning_data_json

    default_message = 'You are not reading the most up to date version of this documentation. {newest} is the newest version.'

    banner_html = '''
    <div id="{id_div}" class="admonition warning">
        <p class="first admonition-title">{banner_title}</p>
            <p class="last">
                {message}
            </p>
    </div>'''.format(
        id_div='version-warning-banner',
        banner_title='Warning',
        message=default_message.format(newest='<a href="#"></a>'),
    )

    app.add_config_value('versionwarning_enabled', False, 'html')
    app.add_config_value('versionwarning_message_placeholder', '{newest}', 'html')
    app.add_config_value('versionwarning_default_admonition_type', 'warning', 'html')
    app.add_config_value('versionwarning_default_message', default_message, 'html')
    app.add_config_value('versionwarning_messages', {}, 'html')

    app.add_config_value('versionwarning_api_url', 'https://readthedocs.org/api/v2/', 'html')
    app.add_config_value('versionwarning_banner_html', banner_html, 'html')
    app.add_config_value('versionwarning_banner_id_div', 'version-warning-banner', 'html')
    app.add_config_value('versionwarning_body_default_selector', 'div.body', 'html')
    app.add_config_value('versionwarning_body_extra_selector', 'div.document', 'html')
    app.add_config_value('versionwarning_project_slug', None, 'html')

    app.connect('doctree-resolved', process_version_warning_banner)

    if sphinx.version_info >= (1, 8):
        # ``config-initied`` requires Sphinx >= 1.8
        app.connect('config-inited', generate_versionwarning_data_json)

        # ``add_js_file`` requires Sphinx >= 1.8
        app.add_js_file('js/versionwarning.js')
    else:
        app.connect('builder-inited', generate_versionwarning_data_json)
        app.add_javascript('js/versionwarning.js')

    return {
        'version': version,
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
