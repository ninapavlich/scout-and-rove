from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.utils import timezone

from .models import *

class SiteProfileListView(ListView):
    model = SiteProfile

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.get_profiles_for_user(self.request.user)

class SiteProfileDetailView(DetailView):
    model = SiteProfile

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SiteProfileDetailView, self).get_context_data(**kwargs)
        context['settings'] = self.object.get_settings()
        context['test_result_sets'] = self.object.get_test_result_sets()
        context['can_edit'] = self.object.can_user_edit(self.request.user)
        return context


class TestResultSetDetailView(DetailView):
    model = TestResultSet

