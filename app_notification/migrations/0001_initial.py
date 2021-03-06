# Generated by Django 3.1.6 on 2021-03-22 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_name', models.CharField(max_length=50, verbose_name='название')),
                ('notification_slug', models.CharField(max_length=50, verbose_name='ссылка')),
                ('notification_description', models.TextField(verbose_name='описание')),
                ('notification_date', models.DateTimeField(auto_now_add=True, verbose_name='дата и время')),
                ('notification_status', models.BooleanField(default=True, verbose_name='статус')),
                ('notification_author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='имя автора')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
                'db_table': 'notificationtable',
                'ordering': ('-notification_status', '-notification_date'),
            },
        ),
    ]
