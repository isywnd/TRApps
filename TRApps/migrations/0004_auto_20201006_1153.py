# Generated by Django 3.1.1 on 2020-10-06 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TRApps', '0003_auto_20201006_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='jawaban',
        ),
        migrations.RemoveField(
            model_name='test',
            name='point',
        ),
    ]
