# Generated by Django 4.2.4 on 2023-08-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConcentrateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fe', models.FloatField(verbose_name='Содержание железа')),
                ('si', models.FloatField(verbose_name='Содержание кремния')),
                ('al', models.FloatField(verbose_name='Содержание алюминия')),
                ('ca', models.FloatField(verbose_name='Содержание кальция')),
                ('s', models.FloatField(verbose_name='Содержание серы')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Качественные показатели железорудного концентрата',
                'verbose_name_plural': 'Качественные показатели железорудного концентрата',
                'ordering': ['-date'],
            },
        ),
    ]
