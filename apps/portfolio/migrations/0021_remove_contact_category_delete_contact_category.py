# Generated by Django 4.0.6 on 2022-08-24 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_remove_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='category',
        ),
        migrations.DeleteModel(
            name='Contact_category',
        ),
    ]
