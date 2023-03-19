from django.contrib import admin
from.models import Immunization, Mortality, Health, Economic, Social

# Register your models here.
admin.site.register(Immunization)
admin.site.register(Mortality)
admin.site.register(Health)
admin.site.register(Economic)
admin.site.register(Social)
