from django.db import models
from django.conf import settings

from scoutandrove.utils.models import BaseModel, BaseTitleModel


class BaseSiteProfile(BaseTitleModel):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 
        blank=True, null=True, related_name="owner")
    admin_access = models.ManyToManyField(settings.AUTH_USER_MODEL, 
        blank=True, related_name="administrators")
    readonly_access = models.ManyToManyField(settings.AUTH_USER_MODEL, 
        blank=True, related_name="viewers")

    class Meta:
        abstract = True

class SiteProfile(BaseSiteProfile):
    pass



class BaseTest(BaseTitleModel):
    description = models.TextField(null=True, blank=True)

    def test(profile, result_set):
        pass

    class Meta:
        abstract = True

class Test(BaseTest):    
    pass



class BaseTestSetting(BaseModel):
    test = models.ForeignKey(settings.SR_TEST_MODEL)
    profile = models.ForeignKey(settings.SR_SITE_PROFILE_MODEL)
    key = models.CharField(max_length=255)
    value = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

class TestSetting(BaseTestSetting):    
    pass




class BaseTestResultSet(BaseModel):

    profile = models.ForeignKey(settings.SR_SITE_PROFILE_MODEL)

    class Meta:
        abstract = True

class TestResultSet(BaseTestResultSet):    
    pass        



class BaseTestResult(BaseModel):

    set = models.ForeignKey(settings.SR_TEST_RESULT_SET_MODEL)  
    test = models.ForeignKey(settings.SR_TEST_MODEL)    
    value = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
    
class TestResult(BaseTestResult):    
    pass      


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