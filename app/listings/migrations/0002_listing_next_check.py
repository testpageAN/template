# Generated by Django 3.2.25 on 2025-01-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='next_check',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
