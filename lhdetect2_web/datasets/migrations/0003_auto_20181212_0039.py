# Generated by Django 2.1.2 on 2018-12-11 17:39

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0002_auto_20181206_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=sorl.thumbnail.fields.ImageField(upload_to='images/'),
        ),
    ]
