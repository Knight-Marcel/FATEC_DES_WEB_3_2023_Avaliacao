from django.contrib import admin
from .models import Presenca


class PresencaModelAdmin(admin.ModelAdmin):
    list_display = ('nomealuno', 'nomeprofessor')
    search_fields = ('nomealuno', 'nomeprofessor')
admin.site.register(Presenca, PresencaModelAdmin)
