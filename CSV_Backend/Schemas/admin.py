from django.contrib import admin
from CSV_Backend.Schemas.models import Schema


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    """ Register Schema model in admin panel """
    list_display = ('name', 'created_at')
    list_display_links = ('name',)
    search_fields = ('name',)
    save_on_top = True
