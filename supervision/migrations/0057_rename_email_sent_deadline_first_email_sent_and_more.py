# Generated by Django 4.2.7 on 2023-11-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("supervision", "0056_rename_deadlines_deadline"),
    ]

    operations = [
        migrations.RenameField(
            model_name="deadline",
            old_name="email_sent",
            new_name="first_email_sent",
        ),
        migrations.AddField(
            model_name="deadline",
            name="second_email_sent",
            field=models.BooleanField(default=False),
        ),
    ]