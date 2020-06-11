from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from banner.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):

    list_display = ('id', 'b_name', 'img')
    list_display_links = ['id', 'b_name', 'img']
    readonly_fields = ['img']
    ordering = ['id']

    def img(self, obj):
        return format_html(
            '<img src="{}" width="100px"/>',
            obj.b_img
        )
