from django.contrib import admin
from fb_fangates.models import FanGate

class FanGateAdmin(admin.ModelAdmin):
    pass

admin.site.register(FanGate, FanGateAdmin)
