from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from .slugify import unique_slugify

class BaseModel(models.Model):

    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, 
        blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
        blank=True, null=True, related_name='%(app_label)s_%(class)s_created_by',
        on_delete=models.SET_NULL)

    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, 
        blank=True, null=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
        blank=True, null=True, related_name='%(app_label)s_%(class)s_modified_by',
        on_delete=models.SET_NULL)

    admin_note = models.TextField(_('admin note'), blank=True, null=True)

    class Meta:
        abstract = True


    @property
    def edit_item_url(self):
        if self.pk:
            object_type = type(self).__name__
            url = reverse('admin:%s_%s_change' %(self._meta.app_label,  self._meta.model_name),  args=[self.id] )
            return url
        return None

   

class BaseTitleModel(BaseModel):

    title = models.CharField(_('Title'), max_length=255, blank=True, null=True)

    slug = models.CharField(_('Slug'), max_length=255, blank=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['title']

    def __unicode__(self):
        return self.title


    @staticmethod
    def autocomplete_search_fields():
        return ("title__icontains","slug__icontains")

    def generate_title(self):
        return 'Untitled %s'%(self.__class__.__name__)
        
    def generate_slug(self):
        unique_slugify(self, self.title)
        return self.slug

    def verify_title_and_slug(self):
        if not self.title:
            self.title = self.generate_title()

        if not self.slug or not self.pk:
            self.slug = self.generate_slug()
        
    def save(self, *args, **kwargs):
        self.verify_title_and_slug()
        super(BaseTitleModel, self).save(*args, **kwargs)
