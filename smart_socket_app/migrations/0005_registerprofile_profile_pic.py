# Generated by Django 3.1.3 on 2020-11-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_socket_app', '0004_auto_20201127_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pics'),
        ),
    ]
