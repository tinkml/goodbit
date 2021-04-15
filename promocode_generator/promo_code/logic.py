import json
from typing import List

from promo_code.serializers import PromoCodeData, PromoCodeRequest
from promo_code.settings import JSON_DATA_FILE_PATH
from promo_code.utils import generate_random_promo_code, append_promo_code_data_to_json


def add_promo_codes(schema: PromoCodeRequest) -> None:
    """Генерируем и добавляем промокоды для группы в JSON."""
    promo_codes_list = []
    for _ in range(schema.promo_codes_amount - 1):
        promo_codes_list.append(generate_random_promo_code(prefix=schema.group_name, promo_code_length=5))

    promo_code_data_schema = PromoCodeData(group_name=schema.group_name, promo_codes=promo_codes_list)
    append_promo_code_data_to_json(promo_code_data_schema)


def get_all_promo_codes_data_from_json(json_file_path: str = JSON_DATA_FILE_PATH) -> List[PromoCodeData]:
    """
    Получаем список схем с данными о промокодах каждой группы.

    :param json_file_path - путь к json файлу.
    """
    promo_codes_data = dict()
    promo_codes_data_list = list()

    with open(json_file_path, 'r') as file:
        for string in file:
            promo_code_data = json.loads(string)  # Десериализуем JSON в объект python
            group_name = promo_code_data['group_name']

            if group_name not in promo_codes_data:
                promo_codes_data[group_name] = dict(group_name=group_name, promo_codes=promo_code_data['promo_codes'])
            else:
                promo_codes_data[group_name]['promo_codes'] += promo_code_data['promo_codes']  # Собираем все промокоды

    for value in promo_codes_data.values():
        promo_codes_data_list.append(PromoCodeData(**value))

    return promo_codes_data_list
