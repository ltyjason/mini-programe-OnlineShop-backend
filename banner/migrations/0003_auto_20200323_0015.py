# Generated by Django 2.2.3 on 2020-03-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_auto_20200322_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='b_img',
            field=models.CharField(max_length=256),
        ),
    ]