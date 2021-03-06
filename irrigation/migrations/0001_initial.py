# Generated by Django 4.0.3 on 2022-03-20 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plants', '0003_property_alter_field_unique_together_field_property_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekdays', models.JSONField(default=[False, False, False, False, False, False, False])),
                ('hours_start', models.JSONField(default=[22, 22, 22, 22, 22, 22, 22])),
                ('durations', models.JSONField(default=[0, 0, 0, 0, 0, 0, 0])),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.field')),
            ],
        ),
    ]
