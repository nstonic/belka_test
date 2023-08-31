from django.contrib import admin

from concentrate.models import ConcentrateData


@admin.register(ConcentrateData)
class ConcentrateDataAdmin(admin.ModelAdmin):
    list_display = [
        'date'
    ]
