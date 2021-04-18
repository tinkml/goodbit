from drf_yasg.utils import swagger_auto_schema
from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from promo_code.logic import add_promo_codes, get_all_promo_codes_data_from_json, get_promo_code
from promo_code.serializers import PromoCodeRequest, PromoCodeRequestBody


class PromoCodeView(APIView):

    @swagger_auto_schema(operation_description='Get all promo codes in the system')
    def get(self, request):
        """Получаем все промокоды в системе"""
        promo_codes_data = get_all_promo_codes_data_from_json()
        if promo_codes_data is None:
            return Response(data='Promo codes does not exists', status=400)

        return Response(data=get_all_promo_codes_data_from_json(), status=200)

    @swagger_auto_schema(request_body=PromoCodeRequestBody, operation_description='Adds group and promo codes to the system')
    def post(self, request):
        """Добавляем группу с промокодами."""
        try:
            schema = PromoCodeRequest(**request.data)
        except ValidationError as err:
            return Response(data=err.errors(), status=400)

        promo_code_data = add_promo_codes(schema)
        return Response(data=promo_code_data, status=201)


class CheckPromoCodeView(APIView):

    @swagger_auto_schema(operation_description='Get promo code by promo code name')
    def get(self, request, promo_code_name):
        """Получаем промо код и его группу."""
        promo_code_data = get_promo_code(promo_code_name)
        if promo_code_data is None:
            return Response(data='Promo code does not exist', status=400)

        return Response(data=promo_code_data, status=200)
