# Generated by Django 3.2.5 on 2021-08-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0005_rename_power_dojo_power_force'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='power_force',
        ),
        migrations.AddField(
            model_name='ninja',
            name='power_force',
            field=models.IntegerField(default=12),
        ),
    ]
