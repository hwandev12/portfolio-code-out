# Generated by Django 4.0.6 on 2022-08-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_choices',
            field=models.CharField(choices=[('TK', 'Taklif'), ('SK', 'Shikoyat')], default='TK', max_length=2),
        ),
    ]
