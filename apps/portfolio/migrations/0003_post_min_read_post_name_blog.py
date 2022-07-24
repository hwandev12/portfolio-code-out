# Generated by Django 4.0.6 on 2022-07-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='min_read',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='post',
            name='name_blog',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
