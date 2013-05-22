from django.db import models
from django.utils.translation import ugettext as _

from begood.models import BeGoodModel

class FanGate(BeGoodModel):
  title = models.CharField(_('title'), max_length=255)
  non_fan_content = models.TextField(_('content for prospective fans'), blank=True)
  fan_content = models.TextField(_('content for fans'), blank=True)
  app_id = models.CharField(_('app ID'), max_length=255)
  
  def __unicode__(self):
   return self.title

  @models.permalink
  def get_absolute_url(self):
    return ('fb_fangate', [self.id])
