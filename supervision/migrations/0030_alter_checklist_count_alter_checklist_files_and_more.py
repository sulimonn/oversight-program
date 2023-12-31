# Generated by Django 4.2 on 2023-09-28 09:17

from django.db import migrations, models

import documents.models
import supervision.models


class Migration(migrations.Migration):

    dependencies = [
        ('supervision', '0029_alter_approval_options_alter_pkd_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='files',
            field=models.FileField(upload_to=documents.models.upload_to_checklist, verbose_name='Контрольная карта'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
