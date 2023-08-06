from rest_framework import serializers

from .enums import UIType, HttpMethod
from .generator import FORM_GENERATABLE_URLS


class FormGeneratorSerializer(serializers.Serializer):
    url = serializers.ChoiceField(choices=FORM_GENERATABLE_URLS)
    method = serializers.ChoiceField(choices=HttpMethod.choices)
    type = serializers.ChoiceField(choices=UIType.choices)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def get_declared_field_choices(cls, field_name):
        field = cls._declared_fields.get(field_name)
        choices = getattr(field, 'choices')
        return choices



