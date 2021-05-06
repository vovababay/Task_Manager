# Generated by Django 3.2 on 2021-05-06 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Колонка',
                'verbose_name_plural': 'Колонки',
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Статус')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.column', verbose_name='Колонка')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметки',
                'ordering': ['date_created', 'id', 'title', 'content'],
            },
        ),
    ]