# Generated by Django 3.1.1 on 2020-10-06 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TRApps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jawaban', models.CharField(max_length=45)),
                ('dosen_pengampu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRApps.dosenpengampu')),
            ],
        ),
    ]
