from django.db import models
from django.db.models import Q
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    from django.apps import apps
    get_model = apps.get_model
except:
    from django.db.models.loading import get_model

from scoutandrove.utils.models import BaseModel, BaseTitleModel


def get_test_models():
    import django.apps
    all_models = django.apps.apps.get_models()
    test_models = [model for model in all_models if issubclass(model, BaseTest)]
    return test_models



class BaseSiteProfile(BaseTitleModel):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
        blank=True, null=True, related_name="owner")
    admin_access = models.ManyToManyField(settings.AUTH_USER_MODEL, 
        blank=True, related_name="administrators")
    readonly_access = models.ManyToManyField(settings.AUTH_USER_MODEL, 
        blank=True, related_name="viewers")

    def get_settings(self):
        test_models = get_test_models()
        output = []
        for test_model in test_models:
            test_setting_model = test_model.get_settings_model()
            output += test_setting_model.objects.filter(profile=self)
        return output

    def get_test_result_sets(self):
        model = get_model(settings.SR_TEST_RESULT_SET_MODEL.split('.')[0], settings.SR_TEST_RESULT_SET_MODEL.split('.')[1])
        return model.objects.filter(profile=self)

    @classmethod
    def get_profiles_for_user(cls, user):
        return cls.objects.filter(Q(owner=user) | Q(admin_access__in=[user.id]) | Q(readonly_access__in=[user.id]))

    def can_user_edit(self, user):
        
        if self.owner == user or user in self.admin_access.all():
            return True
        return False

    class Meta:
        abstract = True

class SiteProfile(BaseSiteProfile):
    pass



class BaseTest(BaseTitleModel):

    description = models.TextField(null=True, blank=True)

    def needsToRun(self, profile):
        """
        This function should look at previous results and timing and whatnot and determine whether this test should be run.
        """
        raise ImproperlyConfigured( "needsToRun(self, profile) should be implemented in test.")

    def run(self, result_set):
        """
        This function should execute the test
        """
        raise ImproperlyConfigured( "run(self, result_set) should be implemented in test.")
   
    @classmethod
    def initializeSettings(cls):
        """
        This function should populate database with defaults ONLY if they are not already set
        """
        raise ImproperlyConfigured( "initializeSettings(self, profile) should be implemented in test.")        

    @classmethod
    def get_settings_model(cls, self):
        """
        This function should return the settings model for this test
        """
        raise ImproperlyConfigured( "get_settings_model(self) should be implemented in test.") 

    @classmethod
    def get_test_result_model(cls, self):
        """
        This function should return the test result model for this test
        """
        raise ImproperlyConfigured( "get_test_result_model(self) should be implemented in test.")     





    class Meta:
        abstract = True




class BaseTestSetting(BaseModel):
    
    """
    Implement test FK in baseclass:
    test = models.ForeignKey('sr_crawl.CrawlTest')
    """
    
    profile = models.ForeignKey(settings.SR_SITE_PROFILE_MODEL)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s Setting"%(self.test)

    def verifyTestSetting(self, value):
        """
        This function should verify that the user's configuration value is valid for this test
        """
        raise ImproperlyConfigured( "verifyTestSetting(self, value) should be implemented in test.")


    class Meta:
        abstract = True





class BaseTestResultSet(BaseModel):

    profile = models.ForeignKey(settings.SR_SITE_PROFILE_MODEL)

    def __unicode__(self):
        return "%s Test Result Set from %s"%(self.profile, self.created_date)

    class Meta:
        abstract = True

class TestResultSet(BaseTestResultSet):    
    pass        



class BaseTestResult(BaseModel):

    """
    Implement test FK in baseclass:
    test = models.ForeignKey('sr_crawl.CrawlTest')
    """

    set = models.ForeignKey(settings.SR_TEST_RESULT_SET_MODEL)  
    value = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "Test Result %s"%(self.test)

    class Meta:
        abstract = True


"""

SiteMap
- profile: Site Profile
- last started, last completed: DateTime


SiteLink
- map: SiteMap
- starting_page
- ending_page

SitePage
- map: SiteMap
- url

SitePageContent
- page: SitePage
- current_html: Text
- current_request_headers: Text
- current_response_headers: Text
- last updated
- last changed
- first found
- current response code
"""