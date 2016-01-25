from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site

try:
    from django.apps import apps
    get_model = apps.get_model
except:
    from django.db.models.loading import get_model

from scoutandrove.apps.sr.models import get_test_models, TestResultSet

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        
        model = get_model(settings.SR_SITE_PROFILE_MODEL.split('.')[0], settings.SR_SITE_PROFILE_MODEL.split('.')[1])
        profiles = model.objects.all()
        test_models = get_test_models()
        
        for profile in profiles:
            profile_settings = profile.get_settings()
            profile_tests = list(set([profile_setting.test for profile_setting in profile_settings]))
            tests_to_run = [test for test in profile_tests if test.needsToRun(profile)]
            if tests_to_run > 0:
                print "Found %s test to run on profile %s"%(len(tests_to_run), profile)

                test_result_set = TestResultSet(profile=profile)
                test_result_set.save()
                
                for test in tests_to_run:
                    print "--- Running %s"%(test)
                    test.run(test_result_set)

        