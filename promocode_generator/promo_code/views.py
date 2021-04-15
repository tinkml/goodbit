from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from promo_code.logic import add_promo_codes, get_all_promo_codes_data_from_json
from promo_code.serializers import PromoCodeRequest


class PromoCodeView(APIView):

    def get(self, request):
        return Response(data=get_all_promo_codes_data_from_json())

    def post(self, request):
        try:
            schema = PromoCodeRequest(**request.data)
        except ValidationError as err:
            return Response(data=err.errors(), status=400)

        add_promo_codes(schema)
        return Response(status=201)
