from django.db import models


class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=256)
    b_img = models.CharField(max_length=256)
    type = models.CharField(max_length=20, default="image")

    class Meta:
        db_table = 'Banner_imgs'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

