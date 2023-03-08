from django.contrib import admin
from CSV_Backend.Users.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    """ Register MyUser model in admin panel """
    list_display = ('username', 'is_superuser', 'is_active')
    list_display_links = ('username',)
    search_fields = ('username',)
    save_on_top = True
