# Generated by Django 4.0.1 on 2022-04-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_equipe_titres_delete_match_equipe_titres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titres',
            name='SuperAF',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='titres',
            name='caf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='titres',
            name='conf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='titres',
            name='cup',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='titres',
            name='ligue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='titres',
            name='superDZ',
            field=models.IntegerField(),
        ),
    ]
