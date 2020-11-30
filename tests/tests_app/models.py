from django.db import models
from drizm_django_commons.serializers import HrefModelSerializer


class TestModel(models.Model):
    title = models.CharField(max_length=255)


class AutoTestModelSerializer(HrefModelSerializer):
    class Meta:
        fields = "__all__"
        model = TestModel
        self_view = "tests_app:auto-detail"


class ExplicitTestModelSerializer(HrefModelSerializer):
    class Meta:
        fields = "__all__"
        model = TestModel
        extra_kwargs = {
            "self": {
                "view_name": "tests_app:explicit-detail"
            }
        }


__all__ = ["TestModel", "AutoTestModelSerializer", "ExplicitTestModelSerializer"]
