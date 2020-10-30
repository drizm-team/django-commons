from django.db import models
from rest_framework import serializers
from drizm_django_commons.serializers.super import (
    SelfHyperlinkingField
)


class OneToOneTestModel(models.Model):
    title = models.CharField(max_length=255)
    value = models.IntegerField()


class TestingModel(models.Model):
    description = models.TextField()
    one_to_one = models.ForeignKey(
        to=OneToOneTestModel, on_delete=models.CASCADE
    )


class ManyToOneTestModel(models.Model):
    parent = models.ForeignKey(
        to=TestingModel,
        on_delete=models.CASCADE,
        related_name="children"
    )


class OneToOneTestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingModel
        fields = "__all__"


class ManyToOneTestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingModel
        fields = "__all__"


class TestModelSerializer(serializers.ModelSerializer):
    self = SelfHyperlinkingField(
        view_name="tests_app:model_viewset-detail",
    )
    # OneToOne should be nested
    # one_to_one = OneToOneTestModelSerializer()

    class Meta:
        model = TestingModel
        fields = "__all__"


__all__ = [
    "OneToOneTestModel", "TestingModel", "ManyToOneTestModel",
    "TestModelSerializer", "OneToOneTestModelSerializer", "ManyToOneTestModelSerializer"
]
