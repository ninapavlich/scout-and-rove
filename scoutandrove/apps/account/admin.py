from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import *


class UserAdmin(VersionAdmin, admin.ModelAdmin):
    pass
    

class UserGroupAdmin(VersionAdmin, admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(UserGroup, UserGroupAdmin)