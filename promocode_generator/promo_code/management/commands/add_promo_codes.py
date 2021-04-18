from django.core.management.base import BaseCommand

from promo_code.logic import add_promo_codes
from promo_code.serializers import PromoCodeRequest
from promo_code.settings import JSON_DATA_FILE_PATH


class Command(BaseCommand):
    help = 'Adds a group with generated promo codes'

    def handle(self, *args, **options):
        if options:
            data = PromoCodeRequest(
                group_name=options['group_name'],
                promo_codes_amount=options['promo_codes_amount']
            )
            return str(add_promo_codes(data=data, json_file_path=options['path']))

    def add_arguments(self, parser):
        parser.add_argument('-gn', '--group_name', action='store', required=True, help='Group name for promo codes')
        parser.add_argument('-pa', '--promo_codes_amount', action='store', type=int, required=True, help='Number of promo codes to create')
        parser.add_argument('-p', '--path', action='store', default=JSON_DATA_FILE_PATH, help='Output JSON file path')
