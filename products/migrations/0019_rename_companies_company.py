# Generated by Django 4.2 on 2023-09-18 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervision', '0020_rename_ischeck_checkmonth_checking'),
        ('products', '0018_alter_companies_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Companies',
            new_name='Company',
        ),
    ]
