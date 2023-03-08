from django.contrib import admin

from CSV_Backend.Columns.models import Column


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    """ Register MyUser model in admin panel """
    list_display = ('schema', 'full_name', 'email')
    list_display_links = ('schema', 'full_name', 'email')
    search_fields = ('schema',)
    save_on_top = True
