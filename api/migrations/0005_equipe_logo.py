# Generated by Django 4.0.1 on 2022-04-30 15:45

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_titres_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
    ]
