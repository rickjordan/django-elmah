from django.contrib import admin
from blamo import models

@admin.register(models.BlamoHost)
class BlamoHostAdmin(admin.ModelAdmin):
    list_display = (
        'hostname',
        'username',
        'api_key',
        'active'
    )

@admin.register(models.BlamoLog)
class BlamoLogAdmin(admin.ModelAdmin):
    list_display = (
        'host',
        'path',
        'username',
        'datetime',
        'error_type',
        'status_code'
    )
