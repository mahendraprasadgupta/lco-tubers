# Generated by Django 3.2.7 on 2021-09-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
