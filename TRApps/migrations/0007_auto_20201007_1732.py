# Generated by Django 3.1.1 on 2020-10-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRApps', '0006_kuncijawaban_mata_kuliah'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoring',
            name='hasilScore',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scoring',
            name='tanggalUjian',
            field=models.DateField(default='1970-01-01'),
            preserve_default=False,
        ),
    ]
