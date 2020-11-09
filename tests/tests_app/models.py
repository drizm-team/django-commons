import uuid

from django.db import models

from drizm_django_commons.serializers.fields import (
    CollectionHrefField,
    EmbeddedSingularResourceField
)
from drizm_django_commons.serializers.super import HrefModelSerializer


class OneToOneTestModel(models.Model):
    title = models.CharField(max_length=255)
    value = models.IntegerField()


class TestingModel(models.Model):
    description = models.TextField()
    one_to_one = models.ForeignKey(
        to=OneToOneTestModel,
        on_delete=models.CASCADE,
        null=True
    )


class ManyToOneTestModel(models.Model):
    parent = models.ForeignKey(
        to=TestingModel,
        on_delete=models.CASCADE,
        related_name="children"
    )
    data = models.CharField(max_length=255)


class PrimitiveDataModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        editable=False
    )
    parent = models.ForeignKey(
        to=TestingModel,
        on_delete=models.CASCADE,
        related_name="comments"
    )


class OneToOneTestModelSerializer(HrefModelSerializer):
    class Meta:
        model = OneToOneTestModel
        fields = "__all__"
        self_view = "tests_app:one_viewset-detail"


class ManyToOneTestModelSerializer(HrefModelSerializer):
    class Meta:
        model = TestingModel
        fields = "__all__"
        self_view = "tests_app:many_viewset-detail"


class TestModelSerializer(HrefModelSerializer):
    # OneToOne should be nested
    one_to_one = EmbeddedSingularResourceField(
        serializer_instance=OneToOneTestModelSerializer()
    )
    children = CollectionHrefField(
        view_name="tests_app:many_viewset-list"
    )

    class Meta:
        model = TestingModel
        fields = "__all__"
        self_view = "tests_app:model_viewset-detail"


__all__ = [
    "OneToOneTestModel", "TestingModel", "ManyToOneTestModel",
    "TestModelSerializer", "OneToOneTestModelSerializer", "ManyToOneTestModelSerializer",
]
