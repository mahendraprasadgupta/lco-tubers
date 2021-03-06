# Generated by Django 3.2.7 on 2021-09-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSideinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec1_msg1', models.CharField(max_length=255)),
                ('sec1_button', models.CharField(max_length=255)),
                ('sec2_msg2', models.CharField(max_length=255)),
                ('copyrightmsg', models.CharField(max_length=100)),
                ('fb_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderSideinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('signin', models.CharField(max_length=10)),
                ('signup', models.CharField(max_length=10)),
            ],
        ),
    ]
