# Generated by Django 4.1.7 on 2023-04-07 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0018_possale_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='possale',
            name='date',
        ),
    ]
