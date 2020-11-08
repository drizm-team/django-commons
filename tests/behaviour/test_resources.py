"""
Test that the implementations in this package,
correspond with the API Design requirements for resources
"""

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from drizm_commons.utils import uri_is_http
from ..tests_app.models import TestingModel, OneToOneTestModel


class TestResources(APITestCase):
    def setUp(self) -> None:
        o = OneToOneTestModel.objects.create(
            title="Okay",
            value=5
        )
        TestingModel.objects.create(
            one_to_one=o,
            description="Listen, this is some stuff"
        )
        TestingModel.objects.create(
            description="New thingy"
        )
        self.model_detail = "tests_app:model_viewset-detail"

    def test010_singular_resources(self):
        url = reverse(self.model_detail, args=(1,))
        res = self.client.get(url)
        data = res.json()
        assert "self" in data.keys() and "id" not in data.keys()
        self_ref = data.get("self")
        assert uri_is_http(self_ref.get("href"))

    def test020_embedded_resources(self):
        url = reverse(self.model_detail, args=(1,))
        res = self.client.get(url)
        data = res.json()
        assert type(data.get("one_to_one")) == dict

        url = reverse(self.model_detail, args=(2,))
        res = self.client.get(url)
        data = res.json()
        # The decoder will serialize 'null' to None
        assert data.get("one_to_one", False) is None
