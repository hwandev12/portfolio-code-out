# Generated by Django 4.0.6 on 2022-08-23 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
