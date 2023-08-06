from django.http import HttpRequest, HttpResponse
from django.utils.functional import lazy
from drf_spectacular.utils import OpenApiParameter, extend_schema, OpenApiExample
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import *

from .enums import UIType
from .generator import UISchemaGenerator, get_schema, get_url_choices
from .serializers import FormGeneratorSerializer
from .convertors.base import UISchemaConvertor


class FormulatorAPI(GenericViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = FormGeneratorSerializer

    @extend_schema(
        description='form-generator proxy API',
        parameters=[
            OpenApiParameter(
                name="url",
                required=True,
                description="폼에 대응되는 API URL 입니다",
                enum=lazy(get_url_choices, list)()
            ),
            OpenApiParameter(
                name="method",
                required=True,
                description="폼에 대응되는 API 호출 메소드입니다",
                enum=serializer_class.get_declared_field_choices('method')
            ),
            OpenApiParameter(
                name="type",
                required=True,
                description="form-schema 가 생성될 타입입니다",
                enum=serializer_class.get_declared_field_choices('type')
            ),
        ],
        examples=[
            OpenApiExample(
                name="response_example",
                value="form-schema by type",

            ),
        ],
    )
    @action(detail=False, methods=['get'], url_path='form-generator', url_name='form_generator')
    def generator(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid()

        url = serializer.data['url']
        method = serializer.data['method']
        view_type = serializer.data['type']

        serializer = UISchemaGenerator().get_serializer_by_endpoint(url, method)
        json_schema = get_schema(serializer)
        ui_schema = UISchemaConvertor().convert(json_schema)
        form_schema = UIType[view_type].convertor.convert(ui_schema)


        # TODO: 오류가 생겼을때 각 오류별로 대응 필요

        return Response(form_schema, status=status.HTTP_200_OK)

