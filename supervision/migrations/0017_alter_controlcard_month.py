# Generated by Django 4.2 on 2023-09-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervision', '0016_remove_controlcard_name_controlcard_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlcard',
            name='month',
            field=models.IntegerField(),
        ),
    ]
