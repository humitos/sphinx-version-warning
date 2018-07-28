# -*- coding: utf-8 -*-


def setup(app):
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

    # Requires Sphinx >= 1.8
    app.connect('config-inited', generate_versionwarning_data_json)

    # New in Sphinx 1.8: app.add_js_file
    app.add_javascript('js/versionwarning.js')

    return {'version': version}


name = 'versionwarning'
version = '0.0.1'
