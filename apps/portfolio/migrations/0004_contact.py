# Generated by Django 4.0.6 on 2022-08-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_post_min_read_post_name_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=600)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
