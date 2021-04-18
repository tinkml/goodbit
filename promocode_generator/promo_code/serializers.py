from typing import Union

from pydantic import BaseModel
from rest_framework import serializers


class PromoCodeBase(BaseModel):
    group_name: Union[int, str]


class PromoCodeData(PromoCodeBase):
    promo_codes: list


class PromoCodeRequest(PromoCodeBase):
    promo_codes_amount: int


class PromoCodeRequestBody(serializers.Serializer):
    """Сериализатор для схемы swagger"""
    group_name = serializers.CharField(max_length=64)
    promo_codes_amount = serializers.IntegerField()
