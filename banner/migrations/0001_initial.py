# Generated by Django 2.2.3 on 2019-11-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=256)),
                ('b_img', models.CharField(max_length=256)),
                ('type', models.CharField(default='image', max_length=20)),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'Banner_imgs',
            },
        ),
    ]
