from typing import ClassVar, Optional

from django.db import models
from rest_framework.reverse import reverse
from rest_framework import serializers


class HrefHyperlinkingField(serializers.HyperlinkedRelatedField):
    def to_representation(self, value):
        default_url = super(
            HrefHyperlinkingField, self
        ).to_representation(value)
        return {"href": default_url}


class SelfHyperlinkingField(serializers.Field):
    def __init__(self, view_name: Optional[str] = None, **kwargs) -> None:
        kwargs["read_only"] = True
        kwargs["source"] = "*"
        super(SelfHyperlinkingField, self).__init__(**kwargs)

        self.view_name = view_name

    def to_representation(self, value):
        return {
            "href": reverse(
                self.view_name, args=(value.id,)
            )
        }
