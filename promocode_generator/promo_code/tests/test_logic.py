import json
import os

from django.test import TestCase

from promo_code.logic import add_promo_codes, get_promo_code
from promo_code.serializers import PromoCodeRequest
from promo_code.settings import FILE_PATH


def add_promo_codes_to_json():
    pass


class LogicTestCase(TestCase):

    test_json_data_file_path = FILE_PATH + 'test_promo_codes.json'  # Путь к тестовому JSON
    test_group_name = 'Test'  # Тестовое название группы
    test_number_of_codes = 5  # Тестовое количество промо кодов

    @classmethod
    def setUpClass(cls):
        data = PromoCodeRequest(group_name=cls.test_group_name, promo_codes_amount=cls.test_number_of_codes)
        add_promo_codes(data, cls.test_json_data_file_path)  # Добавляем данные в файл

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_json_data_file_path)  # Удаляем тестовый JSON.

    def test_add_promo_codes(self):
        """Тестирование добавления группы с промокодами в JSON."""
        with open(self.test_json_data_file_path, 'r') as file:
            promo_code_data = json.loads(file.read())  # Получаем добавленные данные

        # Проверяем наличие и сверяем название группы, акже количество созданных кодов.
        self.assertEqual(promo_code_data["group_name"], self.test_group_name)
        self.assertEqual(len(promo_code_data["promo_codes"]), self.test_number_of_codes)

    def test_get_promocode(self):
        """Тестирование получения информации о промокоде по названию"""
        with open(self.test_json_data_file_path, 'r') as file:
            promo_code_data = json.loads(file.read())  # Получаем добавленные данные

        promo_code_name = promo_code_data["promo_codes"][0]
        required_promo_code_data = get_promo_code(promo_code_name, self.test_json_data_file_path)

        self.assertEqual(self.test_group_name, required_promo_code_data['group_name'])
        self.assertEqual(promo_code_name, required_promo_code_data['promo_code'])
