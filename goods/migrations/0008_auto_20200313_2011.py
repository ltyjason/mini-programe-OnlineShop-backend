# Generated by Django 2.2.3 on 2020-03-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20200313_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='islike',
            name='like',
            field=models.BooleanField(choices=[(0, 'False'), (1, 'True')], default=0),
        ),
    ]
