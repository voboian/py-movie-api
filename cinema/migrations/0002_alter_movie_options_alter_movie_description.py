# Generated by Django 5.0.7 on 2024-07-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name_plural': 'movies'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
