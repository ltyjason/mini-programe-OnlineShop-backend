from django.contrib import admin

# Register your models here.
from user.models import WxUser

admin.site.site_title = "lty's shop后台管理"
admin.site.site_header = "lty's shop后台管理系统"


@admin.register(WxUser)
class WxUserAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'short_img', 'user_sex', 'created_data')
    list_display_links = None
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        if request.method not in ('GET', 'HEAD'):
            return False
        return super(WxUserAdmin, self).has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return False

    def short_img(self, obj):
        if len(str(obj.user_avatar)) > 20:
            return '{}...'.format(str(obj.user_avatar)[0:20])
        else:
            return str(obj.user_avatar)