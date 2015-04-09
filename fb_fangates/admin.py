from django.conf import settings
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _


from begood.contrib.admin.widgets import WysiwygTextarea
from begood.models import Article
from begood_sites.admin import SiteModelAdmin
from fb_fangates.models import FanGate
from outliner.forms import OutlinerChoiceField


class FanGateAdminForm(forms.ModelForm):
  """Admin form for Fan Gates.
  """
  class Meta:
    model = FanGate
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(FanGateAdminForm, self).__init__(*args, **kwargs)
    # Initiate non_fan_content and fan_content fields with Wysiwyg widgets
    content_features = getattr(settings, "WYSIHTML5_CONFIG", {})
    self.fields['non_fan_content'] = forms.CharField(
      widget=WysiwygTextarea(attrs={'cols': 86, 'rows': 30, 'features': content_features}),
      required=False
    )
    self.fields['fan_content'] = forms.CharField(
      widget=WysiwygTextarea(attrs={'cols': 86, 'rows': 30, 'features': content_features}),
      required=False
    )


class FanGateAdmin(SiteModelAdmin):
  """Fan Gate admin.
  """
  form = FanGateAdminForm
  fieldsets = [
    (None, {'fields': ['title', 'app_id', 'sites']}),
    (_('For non-fans'), {'fields': ['non_fan_article', 'non_fan_content']}),
    (_('For fans'), {'fields': ['show_fan_content', 'fan_article', 'fan_content']})
  ]
  search_fields = ['title', 'non_fan_content', 'fan_content']
  
  def formfield_for_dbfield(self, field, **kwargs):
    """Extends the default formfield_for_dbfield and makes sure the article FK
    widgets are rendered correctly.
    """
    # Special handling of article FK:s
    if field.name == 'fan_article' or field.name == 'non_fan_article':
      article_qs = Article.on_site.get_query_set()
      # Initiate field with a nested ModelChoice widget
      return OutlinerChoiceField(
        article_qs,
        level_indicator=u'&nbsp;&nbsp;&nbsp;',
        required=False,
        empty_label='---------'
      )
    # Default
    return super(FanGateAdmin, self).formfield_for_dbfield(field, **kwargs)


admin.site.register(FanGate, FanGateAdmin)
