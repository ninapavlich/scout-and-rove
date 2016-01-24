from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import *


class SiteProfileAdmin(VersionAdmin, admin.ModelAdmin):
    pass

class TestAdmin(VersionAdmin, admin.ModelAdmin):
    pass

class TestSettingAdmin(VersionAdmin, admin.ModelAdmin):
    pass

class TestResultSetAdmin(VersionAdmin, admin.ModelAdmin):
    pass

class TestResultAdmin(VersionAdmin, admin.ModelAdmin):
    pass
    

admin.site.register(SiteProfile, SiteProfileAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TestSetting, TestSettingAdmin)
admin.site.register(TestResultSet, TestResultSetAdmin)
admin.site.register(TestResult, TestResultAdmin)