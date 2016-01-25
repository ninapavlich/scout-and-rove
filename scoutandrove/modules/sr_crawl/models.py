from django.db import models
from django.db.models import Q
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    from django.apps import apps
    get_model = apps.get_model
except:
    from django.db.models.loading import get_model

from scoutandrove.apps.sr.models import BaseTest, BaseTestSetting, BaseTestResult



class CrawlTest(BaseTest):    
    
    def needsToRun(self, profile):
        #TODO
        return True  

    def run(self, set):
        print 'TODO: Run crawling test...'

        result = CrawlTestResult(test=self,set=set,value="Gadzooks!")
        result.save()
    

    @classmethod
    def initializeSettings(cls, reset=False):

        default_settings = {
            'settings_title':"Crawl Test",
            'settings_description': "Crawls sitemap",
            'settings_key': 'site-crawl',
            'settings_value': ''
        }
        
        test, created = cls.objects.get_or_create(slug='crawl-test', defaults={'title': default_settings['settings_title'], 'description': default_settings['settings_description']})
        print "Test: %s created: %s"%(test, created)

        if reset:
            test.title = default_settings['settings_title']
            test.description = default_settings['settings_description']
            test.save()
        
        model = get_model(settings.SR_SITE_PROFILE_MODEL.split('.')[0], settings.SR_SITE_PROFILE_MODEL.split('.')[1])
        profiles = model.objects.all()
        settings_model = cls.get_settings_model()
        for profile in profiles:

            test_setting, created = settings_model.objects.get_or_create(test=test, profile=profile, key=default_settings['settings_key'], defaults={'value': default_settings['settings_value']})
            print "Setting: %s created: %s"%(test_setting, created)

            if reset:
                test.value = default_settings['settings_value']
                test.save()



    @classmethod
    def get_settings_model(cls):
        return CrawlTestSetting

    @classmethod
    def get_test_result_model(cls):
        return CrawlTestResult    


class CrawlTestSetting(BaseTestSetting):    
    
    test = models.ForeignKey('sr_crawl.CrawlTest')

    def verifyTestSetting(self, value):
        return True



class CrawlTestResult(BaseTestResult):

    test = models.ForeignKey('sr_crawl.CrawlTest')
    