# Generated by Django 4.2.10 on 2024-03-24 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kontak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kontakmodel',
            name='waktu_kirim',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
