from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import *




class CrawlTestAdmin(VersionAdmin, admin.ModelAdmin):
    pass

class CrawlTestSettingAdmin(VersionAdmin, admin.ModelAdmin):
    pass

class CrawlTestResultAdmin(VersionAdmin, admin.ModelAdmin):
    pass

    

admin.site.register(CrawlTest, CrawlTestAdmin)
admin.site.register(CrawlTestSetting, CrawlTestSettingAdmin)
admin.site.register(CrawlTestResult, CrawlTestResultAdmin)

