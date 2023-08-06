from drf_spectacular.generators import SchemaGenerator
from drf_spectacular.openapi import *
from rest_framework.serializers import Serializer, ModelSerializer


class UISchemaGenerator(SchemaGenerator):

    def get_serializer_by_endpoint(self, api_url, api_method):
        api_serializer = None
        endpoints = self.get_all_endpoints()

        if api_method.upper() in ('PUT', 'PATCH', 'POST'):
            for path, path_regex, method, view in endpoints:
                if api_url == path and api_method.upper() == method:
                    api_serializer = view.schema.get_request_serializer()
                    break

        return api_serializer

    def get_all_endpoints(self):
        self._initialise_endpoints()
        return self._get_paths_and_endpoints()


class UIAutoSchema(AutoSchema):

    def __init__(self):
        super().__init__()
        self.registry = ComponentRegistry()

    def _map_serializer_field(self, field, direction, bypass_extensions=False):
        result = super()._map_serializer_field(field, direction, bypass_extensions)
        meta = self._get_serializer_field_meta(field)

        if is_list_serializer(field) and is_serializer(field.child):
            component = self.resolve_serializer(field.child, direction)
            result = append_meta(build_array_type(component.schema), meta) if component else None
        elif is_serializer(field):
            component = self.resolve_serializer(field, direction)
            result = append_meta(component.schema, meta) if component else None
        elif isinstance(field, serializers.MultipleChoiceField):
            result = append_meta(build_array_type(build_choice_field(field)), meta)
        elif isinstance(field, serializers.ChoiceField):
            result = append_meta(build_choice_field(field), meta)

        return result


def build_choice_field(field):
    one_of = [{'const': key, 'title': value} for key, value in field.choices.items()]
    schema = {
        'type': 'string',
        'oneOf': one_of
    }
    return schema


def get_schema(serializer_class: Serializer):
    serializer = force_instance(serializer_class)
    auto_schema = UIAutoSchema()
    component = auto_schema.resolve_serializer(serializer, direction='request')
    schema = getattr(component, 'schema', None)
    schema['title'] = get_serializer_title(serializer)

    return getattr(component, 'schema', None)


def get_serializer_title(serializer):
    title = ""

    serializer_meta = getattr(serializer, 'Meta', False)
    if getattr(serializer_meta, 'verbose_name', False):
        title = getattr(serializer_meta, 'verbose_name')
    elif type(serializer) == ModelSerializer:
        title = serializer_meta.model._meta.verbose_name
    else:
        title = type(serializer).__name__
        if title.endswith('Serializer'):
            title = title[:-10]

    return title


def get_url_choices():
    schema_generator = UISchemaGenerator()
    endpoints = schema_generator.get_all_endpoints()
    return set([
        endpoint[0]
        for endpoint in endpoints
        if endpoint[2] in ['PUT', 'PATCH', 'POST']
    ])


FORM_GENERATABLE_URLS = set()