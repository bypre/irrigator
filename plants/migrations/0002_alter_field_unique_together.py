# Generated by Django 4.0.3 on 2022-03-19 05:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='field',
            unique_together={('user', 'name')},
        ),
    ]
