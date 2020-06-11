from django.db import models


class WxUser(models.Model):
    USER_GENDER_CHOICES = (
        (0, '女'),
        (1, '男'),
    )

    id = models.AutoField(primary_key=True)
    nickname = models.CharField(verbose_name=u'昵称', max_length=50, blank=True)
    user_avatar = models.CharField(verbose_name=u'用户头像', max_length=500)
    user_phone = models.BigIntegerField(verbose_name=u'手机号', null=True, blank=True)
    user_sex = models.SmallIntegerField(choices=USER_GENDER_CHOICES, default=1, verbose_name="性别")
    openid = models.CharField(verbose_name=u'微信反馈id', max_length=50, unique=True)
    session_key = models.CharField(verbose_name=u'session', max_length=50, default='')
    uuid = models.CharField(verbose_name=u'自定义唯一标识', max_length=1024, default='')
    created_data = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        db_table = 'user_info'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname