# Generated by Django 4.2 on 2023-10-06 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervision', '0044_moved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moved',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supervision.checkarea'),
        ),
        migrations.AlterField(
            model_name='moved',
            name='month',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supervision.checkmonth'),
        ),
    ]
