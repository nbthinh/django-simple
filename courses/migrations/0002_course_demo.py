# Generated by Django 4.2.17 on 2025-01-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='demo',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
