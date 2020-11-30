from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status


class TestFields(APITestCase):
    def test010_self_href_field(self):
        # Just make sure this does not crash
        url_auto = reverse("tests_app:auto-detail", args=(1,))
        url_explicit = reverse("tests_app:explicit-detail", args=(1,))
        self.client.get(url_auto)
        self.client.get(url_explicit)

        # Try if the write works properly
        url_auto = reverse("tests_app:auto-list")
        url_explicit = reverse("tests_app:explicit-list")
        data = {"title": "Okay Mate how ya doin"}

        for uri in (url_auto, url_explicit):
            res = self.client.post(uri, data)
            assert res.status_code == status.HTTP_201_CREATED
