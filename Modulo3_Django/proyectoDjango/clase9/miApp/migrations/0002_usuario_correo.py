# Generated by Django 5.0.2 on 2024-03-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.CharField(default='null', max_length=150),
            preserve_default=False,
        ),
    ]
