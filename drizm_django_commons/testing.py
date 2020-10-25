from rest_framework.test import APITestCase
from django.urls import reverse
from typing import ClassVar, Iterable


def exclude_keys(dictionary: dict, keys: Iterable) -> dict:
    return {
        k: v for k, v in dictionary.items() if k not in keys
    }


def all_keys_present(dictionary: dict, keys: Iterable) -> bool:
    return all(k in dictionary.keys() for k in keys)


class HttpAPITestCase(APITestCase):
    base: ClassVar[str]

    def __init__(self, *args, **kwargs) -> None:
        super(HttpAPITestCase, self).__init__(*args, **kwargs)
        if "%" not in self.base:
            raise ValueError(
                "self.base needs to be a preformatted string"
            )
        self.list = self.base % "list"
        self.detail = self.base % "detail"

    def post(self, payload: dict, url: str = None):
        url = url or self.list
        return self.client.post(
            reverse(url), payload, format="json"
        )


__all__ = ["exclude_keys", "all_keys_present", "HttpAPITestCase"]
