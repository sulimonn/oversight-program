# Generated by Django 4.2 on 2023-09-16 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_delete_check_area'),
        ('supervision', '0011_month'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Month',
            new_name='CheckMonth',
        ),
    ]
