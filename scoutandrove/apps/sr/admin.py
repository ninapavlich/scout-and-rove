from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import *


class SiteProfileAdmin(VersionAdmin, admin.ModelAdmin):
    pass


class TestResultSetAdmin(VersionAdmin, admin.ModelAdmin):
    pass


admin.site.register(SiteProfile, SiteProfileAdmin)
admin.site.register(TestResultSet, TestResultSetAdmin)