# Generated by Django 3.1.3 on 2021-02-28 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_from_doc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
