# Generated by Django 3.2.7 on 2021-09-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sideinfo', '0003_auto_20210911_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='footersideinfo',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='headersideinfo',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
