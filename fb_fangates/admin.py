from django.contrib import admin
from django.utils.translation import ugettext as _


from begood_sites.admin import SiteModelAdmin
from fb_fangates.models import FanGate


class FanGateAdmin(SiteModelAdmin):
  fieldsets = [
    (None, {'fields': ['title', 'app_id', 'sites']}),
    (_('For non-fans'), {'fields': ['non_fan_article', 'non_fan_content']}),
    (_('For fans'), {'fields': ['show_fan_content', 'fan_article', 'fan_content']})
  ]
  search_fields = ['title', 'non_fan_content', 'fan_content']


admin.site.register(FanGate, FanGateAdmin)
