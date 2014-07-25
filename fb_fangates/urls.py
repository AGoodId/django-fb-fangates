from django.conf.urls import patterns, url, include
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic import TemplateView

from fb_fangates.models import FanGate
from fb_fangates.views import FanGateView

urlpatterns = patterns('',
    url(r'^channel/$', cache_page(60*60*24*365)(TemplateView.as_view(template_name='fb/channel.html')), name='fb_channel'),
    url(r'^(?P<pk>\d+)/$', xframe_options_exempt(csrf_exempt(FanGateView.as_view())), name='fb_fangate'),
)
