from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from nav.models import NavMenu


@admin.register(NavMenu)
class NavMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'menuName', 'show_img')
    list_display_links = ['id', 'menuName']
    readonly_fields = ['show_img']
    ordering = ['id']

    def show_img(self, obj):
        return format_html(
            '<img src="{}" width="50px"/>',
            obj.n_img
        )

    show_img.short_description = u'菜单图片'


