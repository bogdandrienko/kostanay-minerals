# Generated by Django 3.1.6 on 2021-02-27 09:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_rational', '0003_auto_20210227_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likerationalmodel',
            name='created',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now, verbose_name='дата создания'),
        ),
    ]
