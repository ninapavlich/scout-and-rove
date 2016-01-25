from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site

from scoutandrove.apps.sr.models import get_test_models

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):

        
        test_models = get_test_models()


        for model in test_models:
            model.initializeSettings()
        