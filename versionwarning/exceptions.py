# -*- coding: utf-8 -*-


class ConfigError(Exception):
    """
    Incompatible config exception.

    This exception is risen when the extension detects configs that are
    incompatible or that depends each other.
    """

    NO_JSON_URL = (
        'No URL defined to retrieve JSON data. '
        'The URL is mandatory when "versionwarning_retrieve_data_from_api" '
        'is True'
    )
