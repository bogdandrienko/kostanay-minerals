# Generated by Django 3.1.6 on 2021-02-19 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_auto_20210219_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-id',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-id',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]