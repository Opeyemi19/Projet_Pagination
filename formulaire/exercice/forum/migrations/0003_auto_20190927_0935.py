# Generated by Django 2.2.5 on 2019-09-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20190927_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videodash',
            name='url',
        ),
        migrations.AddField(
            model_name='videodash',
            name='url_video',
            field=models.URLField(null=True),
        ),
    ]
