# Generated by Django 4.2.10 on 2024-04-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_artikel_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='penerbit',
            field=models.CharField(default='sumantris', max_length=50),
            preserve_default=False,
        ),
    ]