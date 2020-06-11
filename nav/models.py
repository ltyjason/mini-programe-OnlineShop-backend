from django.db import models


class NavMenu(models.Model):
    id = models.AutoField(primary_key=True)
    menuName = models.CharField(verbose_name=u'导航菜单', max_length=16, unique=True)
    n_img = models.CharField(u'菜单图片', max_length=256)

    class Meta:
        db_table = 'NavMenu'
        verbose_name = '分类导航'
        verbose_name_plural = verbose_name
