# Generated by Django 3.1.3 on 2020-12-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_socket_app', '0009_smartsocket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartsocket',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]