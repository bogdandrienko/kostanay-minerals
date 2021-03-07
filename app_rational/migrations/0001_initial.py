# Generated by Django 3.1.6 on 2021-03-07 06:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryRationalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True, verbose_name='название')),
                ('category_slug', models.SlugField(unique=True, verbose_name='ссылка')),
                ('category_description', models.TextField(blank=True, verbose_name='описание')),
                ('category_image', models.ImageField(blank=True, upload_to='uploads/rational/category', verbose_name='картинка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categoryrationaltable',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='RationalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rational_date_certification', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now, verbose_name='дата получения удостоверения на предложение')),
                ('rational_date_registrated', models.DateTimeField(auto_created=True, blank=True, default=django.utils.timezone.now, verbose_name='дата регистрации')),
                ('rational_structure_from', models.CharField(blank=True, max_length=50, verbose_name='имя подразделения')),
                ('rational_id_registrated', models.IntegerField(blank=True, default=0, verbose_name='номер регистрации')),
                ('rational_name', models.CharField(max_length=50, verbose_name='название статьи')),
                ('rational_place_innovation', models.CharField(blank=True, max_length=100, verbose_name='место внедрения')),
                ('rational_description', ckeditor.fields.RichTextField(blank=True, verbose_name='описание')),
                ('rational_addition_file_1', models.FileField(blank=True, upload_to='uploads/rational/%d_%m_%Y/%H_%M_%S', verbose_name='приложение 1')),
                ('rational_addition_file_2', models.FileField(blank=True, upload_to='uploads/rational/%d_%m_%Y/%H_%M_%S', verbose_name='приложение 2')),
                ('rational_addition_file_3', models.FileField(blank=True, upload_to='uploads/rational/%d_%m_%Y/%H_%M_%S', verbose_name='приложение 3')),
                ('rational_offering_members', ckeditor.fields.RichTextField(blank=True, default='<table align="left" border="2" cellpadding="2" cellspacing="2" style="width:1000px"><thead><tr><td><p>Фамилия, имя, отчество авторов</p></td><td><p>Место работы</p></td><td><p>Должность</p></td><td><p>Доля (%) участия*</p></td><td><p>Год рождения</p></td><td><p>Подпись**</p></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table>', verbose_name='предложившие участники')),
                ('rational_conclusion', ckeditor.fields.RichTextField(blank=True, default='<table align="left" border="2" cellpadding="2" cellspacing="2" style="width:1000px"><thead><tr><td><p>Название Структурного подразделения</p></td><td><p>Заключение</p></td><td><p>Должность, название отдела</p></td><td><p>Подпись</p></td></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table>', verbose_name='заключения по предложению')),
                ('rational_change_documentations', ckeditor.fields.RichTextField(blank=True, default='<table align="left" border="2" cellpadding="2" cellspacing="2" style="width:1000px"><thead><tr><td><p>Наименование документа</p></td><td><p>№ извещения</p></td><td><p>Дата изменения</p></td><td><p>Должность и название отдела</p></td><td><p>Подпись</p></td></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table>', verbose_name='изменение нормативной и тех. документации')),
                ('rational_resolution', models.CharField(blank=True, max_length=200, verbose_name='принятое решение')),
                ('rational_responsible_members', ckeditor.fields.RichTextField(blank=True, default='<table align="left" border="2" cellpadding="2" cellspacing="2" style="width:1000px"><thead><tr><td><p>ФИО сотрудника</p></td><td><p>Задачи, мероприятия</p></td><td><p>Сроки выполнения</p></td><td><p>Название подразделения, должность</p></td><td><p>Подпись ответственного сотрудника или его руководителя</p></td><td><p>Отметка о выполнении</p></thead><tbody><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table>', verbose_name='ответственные участники')),
                ('rational_date_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('rational_addition_image', models.ImageField(blank=True, upload_to='uploads/rational/%d_%m_%Y/%H_%M_%S', verbose_name='картинка к предложению')),
                ('rational_status', models.BooleanField(blank=True, default=True, verbose_name='статус')),
                ('rational_autor_name', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='имя автора')),
                ('rational_category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_rational.categoryrationalmodel', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Рационализаторское предложение',
                'verbose_name_plural': 'Рационализаторские предложения',
                'db_table': 'rationaltable',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='LikeRationalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_status', models.BooleanField(default=False, verbose_name='лайк/дизлайк')),
                ('like_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('like_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_rational.rationalmodel', verbose_name='предложение')),
                ('like_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
                'db_table': 'likerationaltable',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='CommentRationalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='текст')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_rational.rationalmodel', verbose_name='предложение')),
                ('comment_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'commentrationaltable',
                'ordering': ('-id',),
            },
        ),
    ]
