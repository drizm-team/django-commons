from typing import Any


class ModelSerializerReadWriteMixin:
    class Meta:
        response_serializer_class: Any

    def to_representation(self, instance):
        return self.Meta.response_serializer_class(
            context={
                "request": self.context.get("request")  # noqa super attr
            }
        ).to_representation(instance)