# Generated by Django 3.2.7 on 2021-09-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sideinfo', '0004_auto_20210911_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='headersideinfo',
            name='address',
            field=models.TextField(default='mahiu', max_length=255),
        ),
    ]
