# Generated by Django 3.1.1 on 2020-10-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRApps', '0002_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='dosen_pengampu',
            new_name='mata_kuliah',
        ),
        migrations.AddField(
            model_name='test',
            name='point',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='tanggalUjian',
            field=models.DateField(default='1970-01-01'),
            preserve_default=False,
        ),
    ]