from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from scoutandrove.utils.models import BaseModel, BaseTitleModel

from .manager import UserManager

class User(BaseModel, AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(_('email address'), unique=True, blank=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'

    @staticmethod
    def autocomplete_search_fields():
        return ("email__icontains", "first_name__icontains", "last_name__icontains")

    def get_short_name(self):
        if self.first_name:
            return self.first_name
        return self.email

    def get_public_name(self):
        if self.first_name:
            return self.first_name
        return 'Anonymous User'

    def get_full_name(self):
        if self.first_name and self.last_name:
            return u"%s %s" % (self.first_name, self.last_name)
        elif self.first_name:
            return u"%s (%s)" % (self.first_name, self.email)
        elif self.last_name:
            return u"%s (%s)" % (self.first_name, self.email)
        else:
            return self.email

    def __unicode__(self):
        return self.get_full_name()

class UserGroupMember(BaseModel):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
        blank=True, null=True)
    order = models.IntegerField(default=0)
    group = models.ForeignKey('account.UserGroup', 
        blank=True, null=True)

    class Meta:
        ordering = ['order'] 


class UserGroup(BaseTitleModel):

    member_class = UserGroupMember

    def get_members(self):
        return self.member_class.objects.filter(group=self).order_by('order')

