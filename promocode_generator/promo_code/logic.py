import json
import os
from typing import List, Optional

from promo_code.serializers import PromoCodeData, PromoCodeRequest
from promo_code.settings import JSON_DATA_FILE_PATH
from promo_code.utils import generate_random_promo_code, append_promo_code_data_to_json


def add_promo_codes(data: PromoCodeRequest, json_file_path: str = JSON_DATA_FILE_PATH) -> PromoCodeData:
    """Генерируем и добавляем промокоды для группы в JSON."""
    promo_codes_list = []
    for _ in range(data.promo_codes_amount):
        promo_codes_list.append(generate_random_promo_code(prefix=data.group_name, promo_code_length=5))

    promo_code_data = PromoCodeData(group_name=data.group_name, promo_codes=promo_codes_list)
    append_promo_code_data_to_json(promo_code_data, json_file_path)

    return promo_code_data


def get_promo_code(promo_code: str, json_file_path: str = JSON_DATA_FILE_PATH) -> Optional[dict]:
    """
    Получаем промокод и его группу по названию промо кода.

    :param promo_code - Названиепромо кода.
    :param json_file_path - путь к JSON файлу с группами промо кодов.
    """
    if not os.path.exists(json_file_path):  # Проверяем, существует ли такой файл.
        return None

    group_name = promo_code.split('_')[0] if '_' in promo_code else promo_code

    with open(json_file_path, 'r') as file:
        for string in file:
            promo_codes_data = json.loads(string)  # Десериализуем JSON в объект python

            if promo_codes_data['group_name'] == group_name:
                promo_codes_list = promo_codes_data['promo_codes']

                if promo_code in promo_codes_list:
                    return dict(group_name=group_name, promo_code=promo_code)


def get_all_promo_codes_data_from_json(json_file_path: str = JSON_DATA_FILE_PATH) -> Optional[List[PromoCodeData]]:
    """
    Получаем список схем с данными о промокодах каждой группы.

    :param json_file_path - путь к json файлу.
    """

    if not os.path.exists(json_file_path):  # Проверяем, существует ли такой файл.
        return None

    promo_codes_data = dict()
    promo_codes_data_list = list()

    with open(json_file_path, 'r') as file:
        for string in file:  # Читаем файл построчно.
            promo_code_data = json.loads(string)  # Десериализуем JSON в объект python
            group_name = promo_code_data['group_name']

            if group_name not in promo_codes_data:
                promo_codes_data[group_name] = dict(group_name=group_name, promo_codes=promo_code_data['promo_codes'])
            else:
                promo_codes_data[group_name]['promo_codes'] += promo_code_data['promo_codes']  # Собираем все промокоды

    for value in promo_codes_data.values():
        promo_codes_data_list.append(PromoCodeData(**value))

    return promo_codes_data_list
