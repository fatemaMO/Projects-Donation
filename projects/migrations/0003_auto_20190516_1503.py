# Generated by Django 2.2.1 on 2019-05-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190516_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_reported',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reportedproject',
            name='is_reported',
            field=models.IntegerField(default=0),
        ),
    ]