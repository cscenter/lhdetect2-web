# Generated by Django 2.1.2 on 2018-12-06 02:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='custom_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='gen_type',
            field=models.CharField(blank=True, choices=[('CLEAN_LINE', 'clean line'), ('HYBRID', 'hybrid')], max_length=10, verbose_name='Generation Type'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='generation',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='parent1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='parent2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='repetition',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='sharing',
            field=models.CharField(choices=[('PRIVATE', 'private'), ('PUBLIC', 'public')], default='PUBLIC', max_length=7),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='vegetation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
