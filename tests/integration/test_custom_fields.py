from rest_framework.test import APITestCase
from ..tests_app.models import TestingModel, OneToOneTestModel
from rest_framework.reverse import reverse


class TestCustomFields(APITestCase):
    def setUp(self) -> None:
        o = OneToOneTestModel.objects.create(
            title="Okay",
            value=5
        )
        TestingModel.objects.create(
            one_to_one=o,
            description="Listen, this is some stuff"
        )
        self.model_url = reverse(
            "tests_app:model_viewset-detail",
            args=(1,)
        )

    def test010_self_href(self):
        res = self.client.get(self.model_url)
        data = res.json()
