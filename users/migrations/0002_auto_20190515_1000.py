# Generated by Django 2.2.1 on 2019-05-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='images/defaultUser.png', upload_to='images/user_profile/'),
        ),
    ]