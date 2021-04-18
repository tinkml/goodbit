from django.core.management.base import BaseCommand

from promo_code.logic import get_promo_code
from promo_code.settings import JSON_DATA_FILE_PATH


class Command(BaseCommand):
    help = 'Adds a group with generated promo codes'

    def handle(self, *args, **options):
        if options:
            promo_code_data = get_promo_code(promo_code=options['name'], json_file_path=options['path'])
            if promo_code_data is not None:
                return f'Promo code exists {promo_code_data}'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', action='store', required=True, help='Promo code name')
        parser.add_argument('-p', '--path', action='store', default=JSON_DATA_FILE_PATH, help='Output JSON file path')
