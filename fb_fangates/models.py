from django.db import models
from django.utils.translation import ugettext_lazy as _


from begood.models import BeGoodModel, Article


class FanGate(BeGoodModel):
  """A model for Facebook Fan Gates, for use in Facebook Fan Page Tabs.
  """
  title = models.CharField(_('title'), max_length=255)
  non_fan_content = models.TextField(_('content for prospective fans'),
    blank=True)
  fan_content = models.TextField(_('content for fans'), blank=True)
  non_fan_article = models.ForeignKey(Article,
    verbose_name=_('article for prospective fans'),
    related_name='non_fan_articles', blank=True, null=True)
  fan_article = models.ForeignKey(Article,
    verbose_name=_('article for fans'),
    related_name='fan_articles', blank=True, null=True)
  show_fan_content = models.BooleanField(_('show fan specific content'),
    default=False)
  app_id = models.CharField(_('app ID'), max_length=255)

  class Meta:
    verbose_name = _('Facebook Fan Gate')
    verbose_name_plural = _('Facebook Fan Gates')

  def __unicode__(self):
   return self.title

  @models.permalink
  def get_absolute_url(self):
    return ('fb_fangate', [self.id])
