from typing import Iterable

from django.conf import settings

settings.REST_FRAMEWORK['TEST_REQUEST_DEFAULT_FORMAT'] = 'json'


def exclude_keys(dictionary: dict, keys: Iterable) -> dict:
    return {
        k: v for k, v in dictionary.items() if k not in keys
    }


def all_keys_present(dictionary: dict, keys: Iterable) -> bool:
    return all(k in dictionary.keys() for k in keys)


def uri_is_http(uri: str) -> bool:
    return True if uri.startswith("http") else False


__all__ = [
    "exclude_keys", "all_keys_present", "uri_is_http"
]
