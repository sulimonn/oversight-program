# Generated by Django 4.2 on 2023-09-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervision', '0012_rename_month_checkmonth'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkmonth',
            name='period',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
