from django.contrib import admin
from report.models import HealthCenter, District, Block, Event
 
admin.site.register(HealthCenter)
admin.site.register(Event)
admin.site.register(District)
admin.site.register(Block)
