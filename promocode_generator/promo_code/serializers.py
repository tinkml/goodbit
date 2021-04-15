from typing import Union

from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    group_name: Union[int, str]


class PromoCodeData(PromoCodeBase):
    promo_codes: list


class PromoCodeRequest(PromoCodeBase):
    promo_codes_amount: int
