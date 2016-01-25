from django.conf.urls import url

from .views import SiteProfileListView, SiteProfileDetailView

urlpatterns = [
    url(r'^$', SiteProfileListView.as_view(), name='site_profile_list'),

    url(r'^profiles/$', SiteProfileListView.as_view(), name='site_profile_list'),

    url(r'^profiles/(?P<slug>[\w-]+)/$', SiteProfileDetailView.as_view(), name = 'site_profile_detail'),
]