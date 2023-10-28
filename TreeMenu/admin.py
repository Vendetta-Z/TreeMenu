from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from TreeMenu.models import MenuItem


class MenuItemModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(MenuItem, MenuItemModelAdmin)