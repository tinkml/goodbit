import json
import os
import random
import string
from typing import Union

from promo_code.serializers import PromoCodeData


def generate_random_promo_code(promo_code_length: int, prefix: Union[str, int] = None) -> str:
    """
    Генерирует промо код указанной длины из рандомных символов ASCII.

    :param promo_code_length - количество символов, из которых должен состоять промокод.
    :param prefix - начальная, статичная часть промокода.
    :return - промокод, формата "prefix_promocode", при наличии префикса, либо "promocode".
    """
    symbols_for_promo_code = string.ascii_letters + string.digits  # Строка из букв и цифр ASCII
    promo_code = ''  # Генерируемый промо код.
    for _ in range(promo_code_length):
        promo_code += random.choice(symbols_for_promo_code)  # Рандомно выбираем символ, добавляем к промо коду.

    return promo_code if prefix is None else str(prefix) + '_' + promo_code


def append_promo_code_data_to_json(
        promo_code_data: PromoCodeData,
        json_file_path: str
) -> None:
    """
    Добавляет JSON структуру в файл, не перезаписывая его полностью.

    :param promo_code_data - схема с данными о группе и промокодах
    :param json_file_path - путь к json файлу.
    """

    if not os.path.exists(json_file_path):  # Проверякм, существует ли такой файл.
        os.mknod(json_file_path)  # Если нет, создаем.

    with open(json_file_path, 'a') as file:
        json_data = json.dumps(promo_code_data.dict())
        file.write(json_data + '\n')
